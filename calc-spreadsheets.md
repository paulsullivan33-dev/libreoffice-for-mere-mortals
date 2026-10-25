# Calc — Spreadsheets

Calc is the spreadsheet: a grid of
cells, each holding a value or a
formula, and a calculation engine
underneath that keeps the answers
current. Lists, budgets, stock counts,
the household ledger — if it has rows
and anything is summed, it belongs
here. This chapter explains the grid's
few deep facts, including the one the
lab caught red-handed.

## Cells hold two things

A cell shows a **value** — but it may
*store* either a literal (the number
42, the text "Tomato") or a **formula**
(`=B2*C2`) whose value the engine
calculates. The grid displays values;
the formula bar shows what is really
stored. Everything else in Calc is
commentary on that sentence.

Functions are formulas with staff:
`=SUM(D2:D4)` totals a range, and there
are hundreds more (AVERAGE, VLOOKUP and
its modern cousin XLOOKUP, IF for
decisions). Type `=` and start writing;
the engine suggests as you go.

## Numbers are not text

The lab's first spreadsheet test was a
plain CSV — text lines, nothing more:

```
Tomato,Gardener's Delight,42,2.50
```

Converted to a real spreadsheet
(chapter 9, transcript t04), a second
program read the cells back and
reported their *types*: the words came
back as text, `42` as an **integer**,
`2.50` as a **number** — and summing
the Packets column gave 252, the true
total. That detection — *this column is
numbers, that one is words* — is the
difference between a sheet and a photo
of a sheet. It is also the classic CSV
trap in reverse: values that merely
*look* numeric (phone numbers, codes
with leading zeros, dates in a foreign
order) can be "helpfully" converted on
import. The CSV import dialog, which
appears whenever Calc opens a `.csv`,
exists so you can mark a column **Text**
before the engine guesses. Guess is the
operative word: check what the import
did, especially to anything with a
leading zero or a slash in it.

## The cached-answer trap, measured

Here is the deep fact, and the lab
measured it rather than believing it.
Spreadsheet files do not store only
formulas — they store each formula's
**last calculated answer** beside it
(the *cached value*), so a file can be
displayed without calculating. When
another program converts the file, what
does it do with the answers — trust the
cache, or calculate afresh?

The lab built a sheet whose formulas
had **no cached answers at all** (the
generator library writes formulas only;
transcript t06). Converted to CSV, out
came true answers — 15, 7.8, 6.5, total
**29.3**. Missing cache: the engine
calculates. Then the lab hand-edited a
copy, giving one formula a **wrong**
cached answer — 999 for a product that
is really 15 — and converted again
(transcript t06b). Out came **999**,
trusted verbatim; and the total, whose
cache was empty, was calculated over
the poisoned cell — **1013.3**. The
rule, as measured on 24.2:

> A stored answer is trusted exactly as
> stored. A missing answer is
> calculated. The engine does not check
> the stored ones for sanity.

In ordinary life the cache is written
by the spreadsheet itself and is
honest. It bites when files are
*made by programs* — generated reports,
exports from other systems, anything
that writes formulas without a
calculation engine behind it, or with
a buggy one. The defences are two:
open the file in Calc and force a
recalculation (Ctrl+Shift+F9) before
trusting totals, or convert and then
check one sum by hand, as the lab did.
Chapter 10 returns to this from the
batch side.

## Round trips keep values, not spellings

Converted CSV → ODS → CSV (transcript
t05), the sheet's values survived
untouched — but the *text* changed:
`2.50` came home as `2.5`, `1.80` as
`1.8`. No data was lost; the trailing
zero was punctuation, and punctuation
belongs to formatting, not value. Judge
a spreadsheet conversion by its values
(as t04 did, cell by cell), never by
diffing the text files and panicking —
or celebrating — at the difference.

## Sheets, printing, and the rest

A file holds many sheets (tabs along
the bottom); formulas can reach across
them (`=Sheet2.A1`). Freeze panes,
filters on column headings, and charts
from selected ranges are the everyday
ninety percent after formulas. Printing
a wide sheet is its own small art —
landscape, fit-to-page, repeating
header rows — under Format → Page
Style, and chapter 13 covers the print
path in general. Data → Sort and the
AutoFilter are where lists turn into
answers; both operate on values, which
is why the text-versus-number fact
above decides whether your sort puts
10 before 2 or after it.
