# Converting from the Command Line

This is the chapter with no equivalent
in the rented suites: the whole engine,
driven from a shell, converting files
without opening a window. Everything
here was run by the lab, on the files
the lab made, and *checked afterwards
by other tools* — a conversion you have
not read back is a hope, not a result.
The transcripts are `libreoffice-lab/
transcripts/`, t01–t06.

## The one command

```
soffice --headless --convert-to pdf --outdir out/ letter.docx
```

`--headless` runs the engine with no
display (and, on a machine that has
one, stops it stealing your screen).
`--convert-to` names the destination
format by its usual extension; the
engine picks the filter. Each file is
announced as it converts:

```
convert .../harbour-letter.docx as a Writer document -> .../out/harbour-letter.pdf using filter : writer_pdf_Export
```

Several files can be listed; they
convert one after another into the
`--outdir` folder (the current folder
if you omit it). The name stays the
same bar the extension.

Check: the output exists and is what
it claims. The lab's letter PDF, read
back with `pdftotext`, contained the
whole letter — heading, the table's
days and hours, the bullets, the
italic sentence (transcript t02). A
PDF that exists but is one blank page
is a conversion that failed politely;
only reading back catches those.

## The battery the lab ran

| From → To | Proof applied | Result |
|---|---|---|
| `.docx` → `.pdf` | `pdftotext` full read-back; `pdfinfo` | text, table and list complete; 1 page, tagged PDF (t02) |
| `.docx` → `.odt` | unzipped; text pulled from `content.xml` | every paragraph present, structure intact (t03) |
| `.csv` → `.xlsx` | cells read back by a second library, types inspected | numbers arrived as numbers (sum 252 ✓); words as text (t04) |
| `.csv` → `.ods` → `.csv` | `diff` against the original | values identical; trailing zeros lost — `2.50`→`2.5` (t05) |
| `.xlsx` → `.csv` (formulas, no cached answers) | read the numbers | **calculated**: 15, 7.8, 6.5, total 29.3 (t06) |
| `.xlsx` → `.csv` (one wrong cached answer) | read the numbers | **trusted**: 999 printed; total recalculated over it, 1013.3 (t06b) |

The last two rows are chapter 6's trap
seen from the converter's side, and
they are the reason this chapter
insists on read-backs.

## Choosing the filter, not just the format

A format can have several filters, and
filters take options. Naming one looks
like this:

```
soffice --headless --convert-to "csv:Text - txt - csv (StarCalc):44,34,76,1,,0,false,true,true,false,false,-1" sheet.xlsx
```

The string after the second colon is
the CSV filter's option list (separator
44 = comma, quote 34, charset 76,
first line, and so on — the full
vocabulary is in the project's filter
documentation, and it is as forbidding
as it looks). Two things the lab
learned by doing (t06): choosing a
filter *by name with options* changed
the output's shape — the converter
wrote one file **per sheet**,
`seed-orders-Orders.csv`, instead of a
single file — and the plain
`--convert-to csv` had silently used
sensible defaults all along. The
mortals' rule: use the plain form
until a result is wrong in a way you
can name; then take up filter options
to fix that named thing, and re-check.

Other honourable mentions in the same
toolbox: `--print-to-file` renders
through the print path instead of an
export filter (occasionally the fix
for a stubborn layout), and
`--cat` dumps a document's text to the
terminal — the quickest read-back of
all for a document you only need the
words from.

## Starting the engine before you need it

The first conversion in a session pays
the program's startup cost; later ones
are quick. On the lab's small machine
each single-file conversion took a few
seconds, nearly all of it starting up.
That arithmetic is why batch work has
its own chapter: the profile and
process tricks of chapter 10 exist to
stop you paying it per file, and to
stop the engine's single-instance
habit from eating your script.
