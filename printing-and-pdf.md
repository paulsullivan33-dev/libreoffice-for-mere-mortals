# Printing and PDF

PDF is LibreOffice's second native
tongue: the export the lab proved end
to end, the format documents retire
into, and — one step removed — the
print path, since a modern print
system is a PDF pipeline wearing a
printer's name. The lab owned no
printer and printed nothing; this
chapter says what that leaves
unproven, and it is mostly the
direction *paper*.

## Exporting to PDF

File → Export As → Export as PDF in
the window; on the command line it is
chapter 9's flagship conversion:

```
soffice --headless --convert-to pdf letter.docx
```

The lab's proof (transcript t02):
`pdfinfo` reported one page, Letter
size, **Producer: LibreOffice 24.2**,
and — the detail that matters most for
documents other people must *use* —
**Tagged: yes**. A tagged PDF carries
the document's structure (headings,
reading order, table shape) inside it,
which is what screen readers navigate
by and what text extraction reads in
order; `pdftotext` walked the lab
letter top to bottom without a stumble
because the tags said where everything
lived. Tagging is on by default in the
full export dialog (PDF/A and
accessibility options live there too,
including archiving-grade PDF/A for
documents that must open in twenty
years).

Choices in the dialog that earn their
keep:

- **Range** — whole document or pages;
  irrelevant to most, vital to a
  300-page report's chapter three.
- **Images** — lossless or JPEG at a
  quality: the difference between a
  40 MB PDF and a 2 MB one is usually
  sitting in this panel.
- **Export outlines** — your headings
  become the PDF's bookmarks (chapter
  5's machinery paying out).
- **PDF/A** — the archiving variant;
  embeds fonts, forbids the fragile
  features, costs a little size.

## Fonts again, one last time

A PDF embeds its fonts (subsetted),
which is why it looks the same
everywhere — and why it is the honest
way to send a document whose layout
you care about. What it embeds is
what the *converting* machine had:
convert on a machine missing the
document's font and the PDF faithfully
preserves the substitute's layout,
wraps and all. Chapter 10's profile
discipline has a machine-room twin:
convert on a machine whose fonts match
the document's home.

## Printing

File → Print (Ctrl+P) opens the print
dialog over the same rendering engine:
choose the printer, the range, copies,
and — in the LibreOffice panel —
*print to file* as PDF or PostScript,
the GUI cousin of `--print-to-file`.
Page styles carry the paper facts
(size, orientation, margins) per
document or per Calc sheet, and the
spreadsheet case needs them most: a
wide sheet's Page Style is where
landscape and fit-to-width live, and
more spreadsheet print grief is born
there than at any printer.

What the lab could not do is the last
yard: no paper moved. Printer quirks —
a driver that scales to 97%, a duplex
unit that flips the wrong edge — are
yours and your printer's, and no guide
can pre-live them. The check that
travels: **export the PDF first and
look at it**. If the PDF is right,
the fault is between the print dialog
and the paper, and you have halved
the world the fault can live in.
