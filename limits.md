# Limits

What LibreOffice cannot do, or cannot
do well, stated in one place so the
rest of the guide can be believed.

## Fidelity has a ceiling

It opens nearly everything; it
reproduces most things; it guarantees
nothing in a foreign format. Chapter
8's three costs — fonts, featureless
twins, macros — are not bugs awaiting
fixes; they are the economics of
translating between two living
products that each move yearly. Any
document whose exact appearance is
contractual (a filing, a print-ready
proof) belongs to the program that
made it. LibreOffice's own promise,
and it keeps it, is the other one:
your words and numbers are never
hostage.

## Big files are slow files

The engine loads a whole document to
work on it. A spreadsheet with a
million real rows, a document with
two thousand images, a deck built of
full-bleed photographs: each opens,
eventually, and edits, eventually.
The rented suites strain at the same
sizes, but they strain on bigger
machines' behalf. On a modest computer
the practical ceilings arrive sooner,
and the honest mitigations are
structural: split the workbook, shrink
the images before they go in, archive
the old years out of the live sheet.

## One profile, one process

Measured in the lab (chapter 10): an
instance per profile, delegation
between invocations, parallel work
only through parallel profiles. It is
a design, not a defect — but
automation that ignores it produces
the suite's most confusing failures,
the silent ones.

## The exit code means little

Also measured: failure can exit 0.
Any process built on the engine must
verify outputs, not statuses. This is
a limit of the *interface*, and chapter
10's assertion habit is the whole
defence.

## Collaboration is not its home turf

Several people in one document at the
same moment — the browser suites'
party trick — is LibreOffice Online's
and Collabora's territory, not the
desktop program's. The desktop suite
shares files the older way (one
editor at a time, tracked changes for
the conversation) and does it well;
if live co-editing is your daily
bread, chapter 15 has already told
you where it is baked.

## Smaller print, plainly

- **Tracked changes and comments**
  interoperate with Word's up to a
  point; exotic review workflows
  (legal redlining chains) belong
  in Word.
- **HTML export** produces web pages
  of a certain age's habits; for a
  real website, write for the web
  (the MkDocs guide in this series)
  rather than exporting at it.
- **Base** is a front door, not a
  database career; multi-user data
  belongs in a real database with
  Base, at most, holding the forms.
- **The interface will not be
  rearranged to match Word's**, however
  many ribbons are requested; the
  Tabbed view (View → User Interface)
  narrows the culture shock and that
  is where the effort honestly ends.
