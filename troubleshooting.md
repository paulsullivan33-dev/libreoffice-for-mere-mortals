# Troubleshooting

Symptom → cause → fix, in the order a
mortal meets them. Every entry that
says "measured" happened in this
guide's lab.

## The conversion "succeeded" and produced nothing

**Cause:** the input was unreadable, or
the delegation trap swallowed the job.
**Fix:** first, believe the output
folder, not the exit code — a missing
file *is* the report (measured: a
nonexistent input prints
`Error: source file could not be
loaded` **and exits 0**). Check the
input path; then ask whether a
LibreOffice instance already owns the
profile — close your windows or give
the job its own `-env:UserInstallation`
(chapter 10).

## A different file came out than the one I named

**Cause:** an explicit filter with
options can change output naming —
the lab's filter-option run wrote
`seed-orders-Orders.csv`, one file per
sheet, instead of `seed-orders.csv`.
**Fix:** list the output folder after
the run; prefer the plain
`--convert-to csv` unless you need the
options (chapter 9).

## The numbers changed in transit

Three distinct diseases:

1. **Trailing zeros vanished**
   (`2.50` → `2.5`). Not a disease:
   values survived, spelling is
   formatting (measured, t05). Judge
   by values.
2. **Totals are wrong and the formulas
   look right.** The cached-answer
   trap (measured, t06b): the file's
   stored answers were trusted. Open
   in Calc, **Ctrl+Shift+F9**, compare
   (chapter 14's recipe).
3. **Numbers became text, or text
   became numbers, at a CSV import.**
   The import guessed (chapter 6).
   Re-import and set the column type
   by hand in the import dialog.

## The document looks different here

**Cause:** almost always a font the
document names and this machine lacks
(chapter 8). **Check:** the formatting
toolbar shows the *named* font even
when a substitute is drawing the
letters. **Fix:** install the named
font, or accept the metric substitute
and re-check pagination before
printing. If the difference is
structural — text boxes moved, a table
split — it is a filter paraphrase:
keep the original in its native
format and export from there.

## "Use ODF Format / Use Word Format?" every time

Chapter 4's warning doing its job.
Decide once: keep originals ODF and
export copies (choose *Use ODF*, tick
the stop-asking box), or, in an
all-Word world, set *Always save as*
under Tools → Options → Load/Save and
silence it there — chosen, not drifted
into (chapter 8).

## LibreOffice does something weird, everywhere

**Cause:** the profile, more often
than any other single thing — a
setting corrupted, an extension gone
wrong. **Fix:** quit fully; rename the
profile folder (`~/.config/libreoffice`
to `libreoffice-old`); start again; a
clean profile is built on the spot
(the lab watched one be born, t07).
If the weirdness is gone, migrate
your templates and macros from the
old folder's `user/` and carry on.
Nothing is lost by the rename until
you choose to delete it.

## It will not start at all

**Causes, in order:** another instance
owns the profile and is itself stuck
(check for a leftover process and end
it); a broken install (reinstall the
packages — your profile, and thus
your settings, survives); on the
nogui packaging, launching without
`--headless` and mistaking the
nothing for a crash. **Check:**
`soffice --version` from a terminal —
a program that can print its version
can usually be talked to, and the
terminal will show you errors the
desktop hides.

## A spreadsheet macro will not run

**Cause:** usually one of three: the
security prompt was (rightly)
declined; the macro is VBA and hit an
object Basic lacks (chapter 12);
or it is filed under a document that
is not open. **Fix:** for your own
macros, keep them in the profile's
Standard library, where they are
trusted and always available; for
other people's, let them stay inert
and ask the sender what the button
was supposed to do.
