# Batch Conversion and Profiles

Converting one file is a command.
Converting four hundred is a *system* —
and the system has three moving parts:
the loop, the profile, and the truth
about exit codes. The lab met all
three; the receipts are transcripts
t06b and t07.

## The loop is the easy part

```
for f in letters/*.docx; do
  soffice --headless --convert-to pdf --outdir pdfs/ "$f"
done
```

That works, and for a dozen files it is
the whole story. Read on when it stops
being the whole story: when the run is
slow, when some files silently do not
convert, or when the script swears it
succeeded and the folder disagrees.

## The exit code cannot be trusted

Measured, not folklore (t06b): asked
to convert a file that does not exist,
the engine prints

```
Error: source file could not be loaded
```

— and exits with status **0**, having
produced nothing. A batch script that
checks `$?` will report total success
over an empty output folder.

So the contract of a trustworthy batch
job is different: **for every input,
assert the output exists** (and, for
the precious ones, that it is newer
than the run and reads back — chapter
9's habit). Shell-shaped, that is:

```
soffice --headless --convert-to pdf --outdir pdfs/ "$f"
test -f "pdfs/${f%.docx}.pdf" || echo "FAILED: $f"
```

Build the failure list into the run
from the start; do not go back for it.

## One profile, one process

Chapter 2's fact, now with teeth: a
user profile is served by **at most
one** LibreOffice process. A second
`soffice` command naming the same
profile does not start a second
engine — it *hands its request to the
instance already running* and returns.
The lab watched it happen (t07): with
a headless instance holding a profile
open, a conversion naming that profile
ran without the fresh-process warning
every other run printed, and the PDF
still appeared — the resident instance
did the work.

Why this matters to scripts:

- **If the resident instance is fine,**
  delegation is invisible and even
  fast. If it is *stuck* — a document
  open in a window with a dialog over
  it, a recovery prompt, a hang — your
  script's conversions go into the
  same swamp, silently, one by one.
- **Your interactive window and your
  batch job share a profile by
  default.** Running the overnight
  conversion while your own
  LibreOffice sits open on the same
  machine means the job delegates to
  *your* instance, under *your*
  session's fate.

## The fix: one profile per job

Give batch work its own profile, kept
in its own folder, used by nothing
else:

```
soffice --headless \
  -env:UserInstallation=file:///srv/convert/profile \
  --convert-to pdf --outdir pdfs/ "$f"
```

The first run builds the profile from
nothing — the lab listed one being
born (t07): `autocorr`, `basic`,
`config`, `extensions`, the settings
file `registrymodifications.xcu`, the
whole anatomy of chapter 2. From then
on the profile is the job's durable
state: its settings (paper size,
language, CSV defaults where the
profile holds them) are fixed, immune
to whatever you do interactively, and
inspectable when a conversion smells.

Parallel jobs want parallel profiles —
two engines cannot share one, full
stop; give each worker its own
`UserInstallation` folder and they run
side by side, as the lab's two
instances on one machine demonstrated
by accident before demonstrating it on
purpose.

## Settings that live in the profile

A conversion's behaviour is partly the
file, partly the profile: default page
sizes, the locale that decides whether
`1.5` or `1,5` is a number, fonts
available to the machine. When a batch
result puzzles you, ask *which profile
ran it* before asking what the command
was. That question, plus "does the
output file exist", catches nearly
every batch ghost this suite can raise.
