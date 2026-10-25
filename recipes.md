# Recipes

Each recipe is small, complete, and
built from parts the earlier chapters
proved. Where a step relies on the
window rather than the engine, it
says so.

## A folder of Word files becomes PDFs, overnight

The job chapter 10 exists for:

```
mkdir -p pdfs
for f in letters/*.docx; do
  soffice --headless \
    -env:UserInstallation=file:///srv/convert/profile \
    --convert-to pdf --outdir pdfs/ "$f"
  test -f "pdfs/$(basename "${f%.docx}").pdf" \
    || echo "FAILED: $f" >> failures.txt
done
```

A dedicated profile (nothing else
uses it), an output folder, and an
assert per file — because the exit
code cannot be trusted (t06b). In the
morning, `failures.txt` is either
absent or an honest list. Spot-check
one PDF with `pdftotext` (t02's
habit) before declaring victory.

## A CSV becomes a real spreadsheet

```
soffice --headless --convert-to xlsx messy-export.csv
```

Then *open the result and look at the
columns* (chapter 6): numbers should
be numbers — right-aligned, summable.
If a code column lost its leading
zeros in transit, the fix is at the
door: open the CSV in the window
instead, and in the import dialog set
that column's type to **Text** before
confirming; the engine guessed, and
the dialog is where you overrule the
guess. Verify with one sum by hand or
by script, as the lab did with a
second library (t04).

## Rescue an antique document

A `.wpd`, an old `.doc`, a Works file
from a machine long recycled:

```
soffice --headless --convert-to odt antique.wpd
```

— then open the `.odt` and *read it*.
Rescue conversions aim at the words:
expect the layout to need an hour of
kindness, expect the text to be all
there. Save the rescued file forward
into ODF as the new original (chapter
8's one-original rule) and keep the
antique untouched, in case a second
rescue with a different tool does
better at the part this one mangled.

## A sheet whose totals you do not trust

For any spreadsheet that arrived from
another program or a generator script
(chapter 6's trap):

1. Open it in Calc.
2. **Ctrl+Shift+F9** — force a full
   recalculation; the cached answers
   are replaced by computed ones.
3. Read the totals again. If they
   moved, the file's cache was stale
   or poisoned; save (in ODF, as the
   new original) before using them.

The lab's poisoned file would have
moved by 984 under this treatment —
the cell from 999 back to 15, and the
total from 1013.3 back to 29.3.

## The letter you send twice

Write once in Writer, in ODF, with
styles (chapter 5). When the office
that runs Word needs it, File → Save
a Copy as `.docx`; when anyone at all
needs to *read* it, export the PDF
(chapter 13). Three files, one
original, no version fork — chapter
8's whole doctrine in one habit.
