# Files and Formats

An office document is a file, and the
file's **format** decides what of the
document survives saving, sending and
the years. This chapter is the map of
the formats LibreOffice lives among,
and the rules for choosing.

## The two great families

**ODF (OpenDocument Format)** —
`.odt` (text), `.ods` (spreadsheets),
`.odp` (presentations), `.odg`
(drawings). An ISO standard (ISO/IEC
26300), designed in public, and
LibreOffice's native tongue: every
feature of the suite has a home in it.
An ODF file is a zip of XML — the lab
opened its converted letter (chapter
9, transcript t03) and read the words
straight out of `content.xml`, which
is the practical meaning of *open*: no
permission needed, no reverse
engineering, your words in a labelled
bag.

**OOXML (Office Open XML)** —
`.docx`, `.xlsx`, `.pptx`. Microsoft's
formats, also an ISO standard on paper
(ISO/IEC 29500), and the world's
default by population: most documents
arriving in your inbox are these.
LibreOffice's filters for them are the
most-used translation code in the
project, and they are good. They are
also, permanently, a translation:
OOXML models documents slightly
differently (styles, sections, text
boxes, chart data), so a round trip
through it is a paraphrase — usually
faithful, never guaranteed verbatim.

## What "compatible" costs, concretely

- **Fonts are the biggest single
  cause.** A document is laid out in
  the fonts it names. If your machine
  lacks Calibri (a Microsoft font), a
  metric understudy stands in — Windows
  machines reading your files have the
  mirror problem with Liberation
  fonts. Text reflows; a page can gain
  or lose a line; a tight table can
  spill. The understudies are
  metric-compatible (same widths), so
  the damage is usually small — but
  "usually" is the load-bearing word.
- **Features without twins.** Some
  objects exist in one suite only —
  certain SmartArt, text effects, Calc
  functions Word's world lacks and
  vice versa. They arrive flattened,
  substituted, or not at all.
- **Macros do not translate.** Chapter
  12: Basic is not VBA, whatever the
  file format.

## The rest of the zoo

| Format | What it is | Reach for it when |
|---|---|---|
| `.pdf` | finished pages, frozen | sending to be read or printed (ch. 13) |
| `.csv` | one table as plain text lines | moving data between programs; the spreadsheet's cargo form |
| `.txt` | words, nothing else | the content with all furniture removed |
| `.rtf` | an elderly interchange format | almost never, these days |
| `.html` | a web page | publishing to the web, roughly — see Limits |
| `.doc`, `.xls` | the pre-2007 Microsoft formats | receiving antiques; save forward into `.docx`/`.xlsx` or ODF |
| `.wpd`, `.wps`… | WordPerfect and other ancestors | the rescue recipe in chapter 14 |

Two cargo rules cover most days:
**CSV is for data, not documents** — it
carries one sheet's values, no formulas,
no formatting, no second sheet, and the
cached-answer lesson of chapter 6 rides
along. **PDF is for readers, not
editors** — it is the end of a
document's journey, not the middle.

## Choosing what to save in

Answer three questions, in order:

1. **Who must open it, with what?** A
   Word-only office gets `.docx`; the
   general public gets PDF; your
   future self gets ODF.
2. **Is it the original or a copy?**
   Keep *one* original — normally in
   the native format of the program
   doing the work — and export copies
   for audiences. Two editable versions
   of one document is how versions
   fork and truth gets lost.
3. **Will it still need to change?**
   Frozen and final → PDF as well as
   the original. Still alive → never
   let the PDF become the only copy.

And the default-setting corollary:
LibreOffice can be told to always save
in Word formats (Tools → Options →
Load/Save → *Always save as*), and
chapter 4's format warning can be
silenced there too. For a machine whose
documents all live in a Word world,
that is a rational setting — as long as
it is chosen, not drifted into, and
chapter 6's trap is known by heart:
the less native the format, the more
the filters are paraphrasing for you.
