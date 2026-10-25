# Writing Criteria

Every guide in this repo is written to the same
standard. If you're adding or editing a guide —
human or AI — hold it to these.

1. **Plain words, real ideas.** Simple language,
   never dumbed-down concepts. Explain jargon on
   first use; collect terms in the glossary.
2. **No hype.** No marketing adjectives, no
   "revolutionary," no promises about what
   something will do for the reader.
3. **Honest about limits.** Say what the thing
   *can't* do. State uncertainty instead of
   smoothing it over. Validation notes include
   what remains unverified.
4. **No invented numbers.** Benchmarks, defaults,
   and specs are either measured or qualified with
   "depends on your setup." If it wasn't tested,
   say so.
5. **Checkable.** Commands are meant to be run,
   with "Check:" blocks showing what success looks
   like. Sources are linked, not asserted.
6. **Respect the reader's setup.** Call out
   Windows/Mac/Linux differences. Don't assume a
   GPU, a budget, or prior experience.
7. **Safety isn't skipped.** Real risks get
   stated plainly, not buried.
8. **Scoped.** Each guide says what it covers and
   points elsewhere for the rest. No guide
   pretends to be the whole subject.
9. **Structure over prose.** Tables, before/after
   examples, symptom → fix. Scannable beats essay.

## Verification notes for this guide

Built and verified 2026-10-24/25 against
**LibreOffice 24.2.7.2** (Ubuntu package
4:24.2.7-0ubuntu0.24.04.7), on a 2-CPU,
7.7 GB sandbox machine running
Ubuntu 24.04.

**The sandbox, declared.** The machine
arrived with LibreOffice's *headless*
packaging installed
(`libreoffice-core-nogui` and kin: the
engine without windows). The conversion
battery (t01–t07) ran on that build;
the full graphical suite was then
installed for the window work (t08,
t09). The install itself took three
attempts, all kept in the lab's memory
rather than its transcripts: the first
died on a shared-apt lock held by a
sibling build; the second on mutual
`Conflicts` between the `-nogui` set
and the full packages when requested
through the `libreoffice` metapackage;
the third, naming the full packages
explicitly, replaced the nogui set
cleanly (exit 0). The version never
changed — 24.2.7.2 throughout — and
t08b re-ran the flagship conversion on
the full build with identical text
output. One visible difference: the
full install brought a JRE, and the
`failed to launch javaldx` warning
that rides along on the t01–t07
transcripts disappeared; every one of
those conversions had succeeded with
the warning present, which is why
chapter 3 calls it a grumble, not a
stop sign.

**Primary sources read, not
remembered:** the program's own
`--help` output, kept entire in t00;
the installed package records (t00);
the converted files themselves, read
back by *other* tools (poppler's
`pdftotext`/`pdfinfo`, `unzip` and a
script over ODT's `content.xml`, and
the openpyxl library over the
converted `.xlsx`). The formula-cache
rule of chapter 6 is stated the way
the lab *measured* it, in both
directions, because the folklore
version ("converters lose formula
results") is only half of what
happened.

**Ran for real** (transcripts in
`libreoffice-lab/transcripts/`):

- t00 — `soffice --version` →
  24.2.7.2 420(Build:2); the full
  installed package list; `soffice
  --help` entire.
- t01 — the fixtures made: a letter
  (`.docx`, via python-docx) with a
  Heading 1, a styled table and a
  bullet list; the seed-stock CSV; a
  formula sheet (via openpyxl) whose
  formulas carry **empty** cached
  values (`<v></v>` in the XML).
- t02 — `.docx` → PDF: `pdfinfo`
  reports 1 page, Letter, Producer
  LibreOffice 24.2, **Tagged: yes**;
  `pdftotext` read back the whole
  letter, table contents included.
- t03 — `.docx` → `.odt`: zip listing
  shown; text extracted from
  `content.xml` — every paragraph,
  list item and table cell present.
- t04 — `.csv` → `.xlsx`: openpyxl
  read the result cell by cell — text
  as `str`, Packets as `int`, Price
  as `float`; the Packets column sums
  to 252, the true total.
- t05 — `.csv` → `.ods` → `.csv`:
  `diff` against the original shows
  only trailing zeros lost
  (`2.50`→`2.5` etc.); values
  identical.
- t06 — formula sheet → CSV with
  **missing** cached values: the
  converter *calculated* — 15, 7.8,
  6.5, total 29.3, all correct. The
  same transcript shows an explicit
  filter-with-options conversion
  writing a per-sheet file
  (`seed-orders-Orders.csv`) instead
  of the default name.
- t06b — the same sheet with one
  cached value hand-edited to a wrong
  999: the converter **trusted it
  verbatim** (999 in the output), and
  calculated the cache-less total
  over it (1013.3). Same transcript:
  converting a nonexistent file
  prints `Error: source file could
  not be loaded` and **exits 0**,
  producing nothing.
- t07 — profiles: a conversion with
  `-env:UserInstallation` pointing at
  an empty folder grew a complete
  profile (autocorr, basic, config,
  extensions, registrymodifications
  .xcu listed). A headless listener
  instance was started holding a
  second profile; a conversion naming
  that profile delegated to the
  running instance — no fresh-process
  warning, output produced — and the
  identical conversion after the
  instance was stopped ran as a fresh
  process, proving both halves.
- t08/t08b — the GUI, on Xvfb with the
  full build: the Start Center opened
  and was screenshotted (left rail:
  Open File, Remote Files, Recent
  Documents, Templates; the Create
  list naming all six components);
  Writer opened the lab letter as its
  own window, also screenshotted —
  the formatting toolbar reporting
  *Heading 1, Calibri, 14 pt* at the
  heading, the styled table rendered
  with its shaded rows, the status
  bar reading *Page 1 of 1 · 172
  words, 974 characters*. Chapters 4
  and 5's window facts are from these
  two windows.
- t09 — a LibreOffice Basic macro
  (five lines, stored in a dedicated
  profile's `Standard` library;
  fixture `Module1-with-proof.xba`)
  invoked headlessly by its
  `vnd.sun.star.script:` URL wrote
  its proof file to disk. Macros are
  therefore taught as *run*, for this
  route.

**Documented only, and labelled as
such in the chapters:** deep
interactive editing — the window was
opened, read and screenshotted, but
no afternoon of real typing, dragging
and formatting was or could be
rehearsed, and chapters 4–7 teach the
editing *feel* from the documentation
on that basis; Impress and Draw depth
(chapter 7 declares itself a survey);
Base beyond its paragraph; the macro
*recorder* and the GUI macro
organiser (the macro itself was run;
the recording of one was not);
document-carried macros and macro
security prompts in action; VBA
execution; the Python–UNO bridge
beyond its shape (the lab's listener
instance was real, the bridge code
was not written); printing to paper
and all printer behaviour (chapter 13
says so); Windows and macOS installs
and behaviour (the lab is Linux);
LibreOffice Online/Collabora.

**Fixtures:** everything invented is
small and generic — a fictional
friends-of-the-lighthouse group and
its winter hours, a garden centre's
seed stock, a seed order sheet —
written for any reader to rebuild
with the two generator scripts in
`libreoffice-lab/fixtures/` (the
third fixture, `seed-stock.csv`, is
shipped as-is). The wrong cached
value (999) in t06b was introduced
by hand-editing the generated file's
XML, shown in the transcript.
Nothing in the lab is modelled on any
real person, organisation or event.
