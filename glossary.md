# Glossary

**Basic** — the suite's built-in macro
language, a BASIC dialect. Macros in
the user profile's Basic libraries are
trusted; macros in documents are not
(chapter 12).

**Cached value** — the answer a
spreadsheet file stores beside each
formula. Converters trust a stored one
exactly as stored, and calculate only
where none is stored (measured, chapter
6).

**Component** — one face of the suite:
Writer, Calc, Impress, Draw, Base or
Math, all running on the one engine.

**CSV** — comma-separated values: one
table as plain text lines. Cargo, not
documents (chapter 8).

**Direct formatting** — appearance
applied to selected text by hand,
instead of by a style. Works; scales
badly (chapter 5).

**Filter** — the code that reads or
writes one format. Conversions are a
filter in and a filter out (chapter 2).

**Headless** — running the engine with
no window: `--headless`, the mode the
whole conversion story hangs on. Also
a packaging variant (*-nogui*) with
the windows omitted entirely.

**Macro** — a small program, usually
Basic, that drives the suite from
inside (chapter 12).

**ODF / OpenDocument Format** —
LibreOffice's native formats (`.odt`,
`.ods`, `.odp`, `.odg`), an ISO
standard, each file a zip of XML.

**OOXML** — Microsoft's formats
(`.docx`, `.xlsx`, `.pptx`); the
world's default by population, a
translation for this suite (chapter 8).

**PDF/A** — the archiving variant of
PDF: fonts embedded, fragile features
forbidden, meant to open in twenty
years (chapter 13).

**Profile (user profile)** — the one
folder holding a user's settings,
templates, dictionaries and macros;
one profile is served by at most one
running instance (chapters 2 and 10).

**Start Center** — the lobby window
offering Open File, Recent Documents,
Templates, and one Create line per
component (chapter 4).

**Style** — a named, reusable
definition of what a paragraph, page,
cell or slide *is*, which carries its
appearance with it (chapter 5).

**Tagged PDF** — a PDF carrying the
document's structure inside it, so
screen readers and text extractors
follow the reading order (chapter 13).

**UNO** — the component model beneath
the suite; the API macros use, and
outside programs can drive through a
bridge (chapter 12).

**UserInstallation** — the
`-env:UserInstallation=…` flag naming
which profile folder an invocation
uses; the batch converter's isolation
tool (chapter 10).

**VBA** — Visual Basic for
Applications, Excel's and Word's macro
language. A cousin of Basic, not the
same tongue (chapter 12).
