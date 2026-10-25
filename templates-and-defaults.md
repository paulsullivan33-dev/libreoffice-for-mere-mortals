# Templates and Defaults

A template is a document that knows
what it is for: open one and you get an
*untitled copy*, pre-built — the
letterhead in place, the styles set,
the spreadsheet's headings and formulas
waiting. Everything in this chapter
lives in the user profile (chapter 2),
which is what makes defaults a profile
story rather than an install story.

## Using and making templates

File → New → Templates shows the
library — a few ship with the suite;
yours are the point. Making one needs
no new skills: build the document as
you want every future one to start
(styles per chapter 5, headers, the
table shape), then **File → Templates →
Save as Template**, name it, and it is
on the shelf from then on. The Start
Center's Templates entry (chapter 4)
is the same shelf from the lobby side.

Good candidates are documents you
re-create: the club newsletter, the
invoice, the meeting minutes, the
stock sheet with its columns and sums
already standing. The rule of thumb:
if you have saved-as from an old copy
three times, the fourth should be a
template — a saved-as copy carries the
old document's accidents (and its
forgotten paragraph in the middle);
a template carries only what you
deliberately put in it.

## The default template

One template can be marked **default**
(File → Templates → right-click → Set
as Default Template): every new Writer
document then starts from it — your
house font, your margins, your heading
style — instead of the program's bare
page. This is the single highest-value
customisation for someone who writes
often, and the one nobody finds,
because it lives two menus deep.

## Defaults that are settings, not templates

Under Tools → Options sit the other
defaults, all profile property:

- **Load/Save → General:** the format
  new documents save in (chapter 8's
  *Always save as*), and whether the
  format warning asks (chapter 4).
- **Language Settings:** the document
  language and, quietly crucial for
  spreadsheets, the locale that parses
  `1,5` versus `1.5` (chapter 10).
- **Writer / Calc pages:** default
  fonts, measurement units, grid and
  print defaults per component.

Change them once, in the profile, and
both the window and the command-line
engine (chapter 9, when it uses that
profile) follow. That shared obedience
is why chapter 10 gives batch jobs
their own profile: your defaults are
yours; the job's are the job's.

## Backing up the profile

Templates, macros (chapter 12),
dictionaries and every setting above
are files in one folder. Back up the
folder — `~/.config/libreoffice` on
Linux, `%APPDATA%\LibreOffice` on
Windows, `~/Library/Application
Support/LibreOffice` on macOS — and a
new machine becomes yours in one copy.
The lab generated a profile from
nothing and watched its anatomy appear
(transcript t07); the anatomy is
portable, and nothing in it is secret
beyond your own recent-documents list.
Exclude the profile's cache and lock
dross if you like; keep `user/` whole
and you keep everything that matters.
