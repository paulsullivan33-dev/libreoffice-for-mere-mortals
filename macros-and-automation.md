# Macros and Automation

A macro is a small program that drives
the suite from inside: open files,
change things, save results, in the
suite's own language, **Basic**. This
chapter covers what macros are, the
security fact that governs them, and
the one route the lab proved from the
ground up: a Basic macro, stored in a
profile, run from the command line,
leaving evidence on disk.

## Recording versus writing

Tools → Macros → Record Macro watches
you work and writes the Basic for you.
For a repeated formatting chore it is
the fastest start there is; the code it
produces talks to the *dispatcher*
(the menu-command service), which
makes it verbose and brittle in known
ways, but it runs. Hand-written Basic
can go further and use the suite's
full programming model — **UNO**, the
component system underneath — which is
a real API with real documentation and
a real learning curve. The honest
ladder for a mortal: record first,
read what was recorded, then hand-write
the small ones. Tools → Macros →
Organise Macros → Basic is where they
live, filed in libraries and modules:
the profile's `Standard` library is
the usual home, and a module is a page
of Subs.

## The lab's proof

The lab wrote a five-line macro into a
dedicated profile's module (the file
is `libreoffice-lab/fixtures/
Module1-with-proof.xba` — macros in
the profile are literally XML-wrapped
text files under
`user/basic/Standard/`), told it to
write one sentence to a file of its
own, and invoked it with no window at
all (transcript t09):

```
$ soffice --headless \
    -env:UserInstallation=file:///…/profiles/macro \
    "vnd.sun.star.script:Standard.Module1.Proof?language=Basic&location=application"
$ cat macro-proof.txt
LibreOffice Basic macro ran here.
```

That invocation — a *script URL*
naming library, module and sub — is
the bridge between chapter 9's batch
world and macros: a shell script can
now make LibreOffice do arbitrary
document work overnight, with the
profile (chapter 10) as the unit of
isolation, and files on disk as the
proof it happened. Build your own the
same way: write the sub in the GUI
organiser on your real machine, test
it small, then call it from the shell.

## Macro security: the governing fact

A document can carry macros of its
own, and a macro can do anything the
program can — which is to say,
anything *you* can. So: **documents
from other people arrive with macros
inert**. The suite's security settings
(Tools → Options → Security → Macro
Security) default to asking, and the
right answer to a stranger's "Enable
Macros" prompt is *no* — a document
that needs its macros to be read is a
document asking for your machine.
Macros in *your own profile* are
trusted because they are yours; that
asymmetry is the design, and it is
why the lab's route runs location=
`application` (the profile) rather
than smuggling code through a
document.

## The VBA question, answered plainly

Excel macros are written in **VBA**;
LibreOffice speaks **Basic** — a
cousin, not a twin. The suite can run
a good deal of VBA code in Calc files
(there is a compatibility mode, and
many simple macros survive it), and
some will fail on objects or habits
that have no equivalent. Nobody honest
can promise you *yours* will run. If a
spreadsheet's macros are load-bearing
for your household or office, that is
a fact to weigh before switching
suites — test the actual file, early,
and believe the test.

## Driving from outside: UNO

The same UNO model the macros use is
reachable from other languages —
Python chiefly (the `python3-uno`
bridge): start the engine listening on
a socket (chapter 10's instance did
exactly that as a side effect), then a
Python script connects and drives
documents object by object. It is the
most powerful route and the least
mortal; the suite's SDK documentation
is its home. This guide proves the
shape of it — a listening instance, a
script URL executed — and leaves the
full bridge to that documentation,
labelled as such.
