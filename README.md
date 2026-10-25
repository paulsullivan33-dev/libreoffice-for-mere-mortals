# LibreOffice for Mere Mortals

Most people meet office software as a
subscription: rent the word processor,
rent the spreadsheet, keep paying or lose
your own files' best reader. **LibreOffice**
is the other shape of that bargain — a
complete office suite, free of charge and
open source, that runs on a machine you
own and reads and writes the formats the
rented world uses. This guide explains how
it works in those terms: the document
programs (Writer, Calc, Impress and
friends), the file formats they live in,
and the part most guides skip — the
*engine* underneath, which can be driven
from the command line to convert files by
the folderful, with no window open at all.

The lab behind this guide ran the real
thing: **LibreOffice 24.2.7**, Ubuntu
24.04's build, on a small Linux machine.
The lab wrote its own documents for the
purpose — a letter with a table and a
list, a seed-stock spreadsheet, a sheet
whose formulas had answers missing — and
then exercised the program end to end:
the letter converted to PDF and read back
word by word, the same letter converted
to LibreOffice's own format and taken
apart to prove the text survived; the
spreadsheet turned into an Excel file and
its numbers checked cell by cell by a
second program; a round trip through the
native spreadsheet format, diffed against
the original; and the formula sheet
converted twice — once with its answers
missing, once with one answer deliberately
wrong — to find out, rather than guess,
which numbers a converter trusts.

What the lab could not do, it did not
fake. The sandbox machine arrived with
LibreOffice's *headless* build — the
engine without the windows — and the full
graphical suite was installed for the
guide. Even so, an office suite is a
thing of mice and eyes, and this machine
has neither to spare: the window was
launched on a virtual display and its
parts identified there, but *deep
interactive editing* — an afternoon of
real typing, dragging and formatting —
is taught from the documentation and
labelled as such wherever it appears, as
are macros in full and printing to real
paper. `criteria.md` keeps the full ledger
of what was run and what was only read.

## What this guide covers

- [**What LibreOffice is**](what-libreoffice-is.md) —
  the mental model: one engine wearing
  several faces, a suite that is also a
  file-format translator, and what it is
  not (a subscription, a web app, a
  perfect clone)
- [**The moving parts**](the-moving-parts.md) —
  the single `soffice` program, the
  component apps, the user profile that
  holds your settings, and the filters
  that translate formats: which part
  holds what, and what breaks when each
  stops
- [**Installing LibreOffice**](installing-libreoffice.md) —
  the full suite and the headless build,
  on Windows, macOS and Linux, and how
  to prove the install is really there
- [**Your first document**](your-first-document.md) —
  the Start Center, opening and creating
  documents, saving without losing your
  work to a format warning, and the lay
  of the window
- [**Writer — documents and styles**](writer-documents-and-styles.md) —
  writing with styles instead of
  formatting-by-hand, headings that build
  your contents page, lists and tables
- [**Calc — spreadsheets**](calc-spreadsheets.md) —
  cells, formulas and functions, what a
  number really is in a sheet, and the
  cached-answer trap the lab measured
- [**Impress and Draw**](impress-and-draw.md) —
  presentations and diagrams: the survey
  chapter, honest about its depth
- [**Files and formats**](files-and-formats.md) —
  ODF and OOXML, what "compatible" really
  costs, the format zoo (.docx, .xlsx,
  .pdf, .csv and the rest), and choosing
  what to save in
- [**Converting from the command line**](converting-from-the-command-line.md) —
  `soffice --headless --convert-to`: the
  lab's whole battery, the filters, and
  reading the results back to prove them
- [**Batch conversion and profiles**](batch-conversion-and-profiles.md) —
  converting folders at a time, the user
  profile as the unit of isolation, the
  running-instance trap, and why the exit
  code cannot be trusted
- [**Templates and defaults**](templates-and-defaults.md) —
  documents that start the way you like,
  default formats, and where the profile
  keeps them
- [**Macros and automation**](macros-and-automation.md) —
  recording and writing Basic macros,
  macro security, and driving the engine
  from other programs — with the lab's
  ceiling stated
- [**Printing and PDF**](printing-and-pdf.md) —
  PDF as the suite's second native
  tongue: export options that matter,
  and printing, labelled for what the
  lab could not touch
- [**Recipes**](recipes.md) — a folder of
  Word files to PDF overnight, a CSV
  cleaned into a real spreadsheet,
  rescuing an old document, and a
  conversion you can trust because you
  checked it
- [**The neighbours**](the-neighbours.md) —
  Microsoft 365, Google Docs, OnlyOffice,
  Calligra and Pandoc: what each trades,
  and why the file formats outlive them
  all
- [**Limits**](limits.md) — pixel-perfect
  fidelity is not on offer, big files are
  slow files, one profile one process,
  stated plainly
- [**Troubleshooting**](troubleshooting.md) —
  the conversion that "succeeded" but
  produced nothing, the numbers that
  changed in transit, the profile that
  ate your settings, and the format
  warning that is trying to help
- [**Glossary**](glossary.md) — the terms,
  collected in one place

## What it doesn't cover

Running an office for a company —
document management, shared editing
servers and records policy are subjects
of their own, and this guide stays with
one person and their machine. Mail merge
at scale, database work beyond a first
look at Base, accessibility auditing,
and writing LibreOffice extensions in
full are likewise pointed at, not taught.
Visual Basic for Applications (VBA)
macros from Excel are discussed honestly
in chapter 12: many run, some don't, and
nobody honest promises yours will.

## How to use this guide

Read chapter 1 for the model and chapter
2 before installing anything — knowing
that one program does all of it turns
later confusion into a named problem.
Chapters 3 and 4 get you a working
suite and a first saved document.
Chapters 9 and 10 are the other ones not
to skip: the command-line engine is the
part of LibreOffice with no equivalent
in the rented suites, and it repays an
hour. The lab's transcripts live in
`libreoffice-lab/transcripts/`; its
fixture makers are
`libreoffice-lab/fixtures/`; its notes
are `examples/lab-notes.txt`.
