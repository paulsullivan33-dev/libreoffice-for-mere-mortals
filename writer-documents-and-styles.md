# Writer — Documents and Styles

Writer is the component most people
mean by "LibreOffice": letters,
reports, a book if you are stubborn.
This chapter teaches the one idea that
separates documents that behave from
documents that fight: **styles**.

## The idea: say what it is, not how it looks

A paragraph in Writer is never just
text — it always *is* something: a
**paragraph style** (Heading 1, Text
Body, List Bullet, Quotation…) decides
its font, size, spacing and numbering
in one appointment. You can also paint
appearances directly — select words,
press Bold, pick 14 pt — and that
*direct formatting* works, until the
document grows: then the heading that
was bolded by hand is not a heading,
the contents page cannot find it, the
PDF cannot bookmark it, and changing
"all headings" means hunting them one
by one.

Say what it is instead:

- Headings get **Heading 1, 2, 3** —
  in order, without skipping, because
  the numbering and the contents page
  believe the ladder.
- Ordinary prose gets **Text Body**.
- Quotations, captions and lists each
  have their style; the lab's letter
  used Heading 1, List Bullet and a
  table, and every part survived two
  format conversions with its role
  intact — the PDF and the ODT both
  kept heading, bullets and table as
  heading, bullets and table (chapter
  9's transcripts, t02 and t03), which
  is what *structure* buys you:
  translators can carry roles even when
  they argue about fonts.

**Character styles** are the smaller
tool for a few words inside a
paragraph — Emphasis, Strong Emphasis,
Source Text — preferred over hand-bold
for the same reason, and just as often
skipped by everyone, including people
writing guides. Direct formatting is
not a sin; it is a loan. Small
documents never feel the interest.

## Changing your mind once

Redefine the style and every paragraph
in it follows: right-click the style in
the Styles deck (F11) → Edit Style, or
Modify the paragraph style from the
Format menu. This is the payoff that
converts people: a 200-page report
changes its heading font in one place.
The lab's window showed the other half
of the system — the formatting toolbar
reporting *Heading 1, Calibri, 14 pt*
for the cursor's paragraph: the style
decides, the toolbar reports.

## Headings are machinery

A document styled with headings gets,
nearly free:

- a **table of contents** (Insert →
  Table of Contents and Index) that
  lists headings with page numbers and
  updates on a right-click;
- **bookmarks in exported PDFs** —
  readers navigate by your headings;
- the **Navigator** (F5), an outline
  you can jump and rearrange by;
- sane conversion: other programs'
  filters map Heading 1 to Heading 1
  across formats, as the lab letter
  proved in both directions of chapter
  9's battery.

## Lists and tables, briefly

Lists are styles too: List Bullet and
List Number carry the bullet and the
counting, and the toolbar buttons are
shortcuts onto them. Tables (Insert
Table, Ctrl+F12) are their own country:
cells, rows that repeat as headers on
every page, and a Table Styles picker
that gave the lab letter its shaded
rows. Two habits prevent most table
grief: let the table style do the
decoration, and never fake a table
with tabs and spaces — spaces lie
about alignment the moment a font
changes.

## What this chapter cannot show you

Typing feel, drag-and-drop, the exact
dance of the styles deck — these the
lab could not rehearse (see the
README's honesty note). They are also,
truthfully, the parts that teach
themselves in the first hour. The
ideas above are the parts that do not:
*naming what text is*, once, is the
whole craft of Writer.
