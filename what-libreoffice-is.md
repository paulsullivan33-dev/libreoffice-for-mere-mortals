# What LibreOffice Is

LibreOffice is a suite of office programs
— a word processor, a spreadsheet, a
presentation program and several more —
that you install on your own computer,
keep forever, and never pay rent on. It
is **free and open-source software**:
the program itself costs nothing, its
source code is published for anyone to
inspect, and a foundation (The Document
Foundation) and a crowd of contributors
maintain it. It runs on Windows, macOS
and Linux, in dozens of languages.

That is the plain description. The mental
model underneath it has three parts, and
each one explains something that
otherwise looks like a quirk.

## One engine, several faces

There is really only one program. The
word processor (Writer), the spreadsheet
(Calc), the presentation tool (Impress),
the drawing tool (Draw), the database
front-end (Base) and the formula editor
(Math) are **components of a single
application**, sharing one engine for
opening, editing, saving and printing.
You can launch any face directly — the
Start Center offers each — but underneath
it is one program with one settings
store, one set of fonts, one dictionary,
one everything. Chapter 2 names the
parts; the practical consequence lands
early: when LibreOffice misbehaves, it
usually misbehaves as *one* program, and
the fix is usually in one place.

## A translator that also types

Every office program edits documents,
but documents live as *files*, and files
come in formats: Word's `.docx`, Excel's
`.xlsx`, the open ODF formats `.odt` and
`.ods`, PDF, plain-text CSV, and dozens
more. LibreOffice's second job — the one
this guide spends unusual time on — is
translating between those formats. It
does this so central a job that the
suite's engine can be run **with no
window at all**, purely as a converter:

```
soffice --headless --convert-to pdf letter.docx
```

That one capability — measured, prodded
and occasionally caught out in chapters
9 and 10 — is what makes LibreOffice
worth having even if you do all your
typing somewhere else. Folders of files
change format overnight. A rented suite
will not do that for you at any price;
it is not in the shop window.

## A guest in other formats' houses

LibreOffice's *native* formats are the
**OpenDocument Format** (ODF) family —
an ISO standard, designed in the open,
and the formats its components save most
completely. The Microsoft formats
(OOXML: `.docx`, `.xlsx`, `.pptx`) are
someone else's standard: LibreOffice
reads and writes them well — well enough
that millions of people use it as their
only word processor in a Word world —
but "well" is not "perfectly", and the
difference shows up exactly where the
documents get fancy. Chapter 8 is honest
about what compatibility costs. The
working rule this guide teaches is
simple: **write in whatever format the
occasion demands, but know which one is
the original** — the copy you keep, and
the copy you send, may need to be
different files.

## What it is not

- **Not a subscription.** There is no
  account, no activation, no monthly
  fee, and nothing stops working if a
  payment does. Companies sell support
  and polished editions (Collabora
  Office is the best known); the
  program in this guide is the free
  community build, and it is the whole
  thing, not a trial.
- **Not a web app.** It runs on your
  machine and works on a train with the
  Wi-Fi off. (A separate project,
  LibreOffice Online, puts the engine
  behind a browser for shared editing;
  it is a neighbour, chapter 15, not
  this guide's subject.)
- **Not a perfect clone.** It covers
  the same ground as Microsoft 365 and
  mostly the same features, but buttons
  live in different places, some polish
  is missing, and a few Microsoft
  features (and fonts — chapter 8) have
  no exact twin. People who switch
  spend a week mildly annoyed and then
  stop noticing; plan for the week.
- **Not magic with other people's
  files.** A document built on features
  LibreOffice lacks will arrive changed.
  The program will open almost anything;
  chapter 16 is plain about the gap
  between *opens* and *opens intact*.

## The shape of the thing

| Face | The job | Native file |
|---|---|---|
| Writer | documents, letters, reports | `.odt` |
| Calc | spreadsheets, lists, sums | `.ods` |
| Impress | presentations | `.odp` |
| Draw | diagrams, posters, simple DTP | `.odg` |
| Base | a front door to databases | `.odb` |
| Math | typeset formulas | `.odf` |

One engine, six faces, and a command
line that can drive the lot without
opening a single window. The next
chapter takes the engine apart.
