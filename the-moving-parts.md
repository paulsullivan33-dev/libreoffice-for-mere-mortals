# The Moving Parts

Five parts do all of LibreOffice's work.
Knowing which part holds what — which
part to blame — is most of getting along
with it.

## The one program: `soffice`

Everything starts as a single program,
named `soffice` (a fossil from its
ancestor, StarOffice). Start it plainly
and you get the Start Center; start it
with a document and the right component
opens on that document; start it with
flags and no document and it becomes
the command-line engine of chapters 9
and 10. The component commands you may
meet — `libreoffice --writer`, and on
Linux the separate-looking `swriter`,
`scalc` and friends — are signposts to
the same door.

Check: the program will tell you its
own version, and the version matters
when a recipe misbehaves:

```
$ soffice --version
LibreOffice 24.2.7.2 420(Build:2)
```

One process means one process: while a
LibreOffice window is open under your
user profile, further `soffice`
commands do not start new programs —
they *talk to the one already running*.
Mostly that is a convenience. In batch
conversion it is a trap, and chapter 10
takes it apart with the lab's receipts.

## The components

Writer, Calc, Impress, Draw, Base and
Math (chapter 1's table) are components
of the one program: separate workshops,
one building. They share the menus' lay
of the land, the spell-checker, the
style system, and the *filters* — the
translators described next. Learning one
component's habits — how styles work,
how Save behaves, where Options hides —
teaches you most of the others'.

## The filters: where translation happens

A **filter** is the code that reads or
writes one format. When you open a
`.docx`, the Word filter reads it into
the engine's own model of a document;
when you save as PDF, the PDF filter
renders that model out. Filters are
named, and the names surface where it
counts — the command line prints the
filter it used:

```
convert letter.docx as a Writer document -> letter.pdf using filter : writer_pdf_Export
```

That line, from the lab's first
conversion, is the whole architecture
in one sentence: *in* through one
filter, *out* through another, the
document itself living between them in
the engine's terms. Two consequences
follow and both are chapters: fidelity
is a property of the *pair* of filters
(chapter 8), and the command line lets
you choose and tune filters explicitly
(chapter 9).

## The user profile: where "you" live

Everything that makes LibreOffice
*yours* — settings, dictionaries,
autocorrect entries, templates, macros,
recent documents, window positions —
lives in one folder: the **user
profile**. On Linux it is
`~/.config/libreoffice/4/user`; on
Windows, `%APPDATA%\LibreOffice\4\user`;
on macOS, `~/Library/Application
Support/LibreOffice/4/user`.

The lab created one from nothing to
prove the point: pointing the program
at a fresh, empty folder with
`-env:UserInstallation=...` and running
one conversion caused a complete
profile to appear — `autocorr`,
`autotext`, `basic` (the macro home),
`config`, `database`, `extensions`,
`gallery`, and the great settings file
`registrymodifications.xcu` — transcript
t07 in `libreoffice-lab/transcripts/`.

Hold three facts about the profile:

1. **One profile, one process.** The
   running-instance trap of chapter 10
   is this fact wearing a disguise.
2. **It is the backup that matters.**
   Program files are reinstallable; the
   profile holds your templates and
   macros. Chapter 11 returns to this.
3. **It is the reset button.** A
   corrupted profile is the classic
   cause of "LibreOffice does something
   weird", and renaming the folder so
   the program builds a fresh one is
   the classic cure (chapter 17).

## The help and the version surface

The program is self-describing, up to a
point. `soffice --help` prints the full
list of command-line flags — the lab
kept all of it in transcript t00 —
and `--version` prints the build. The
installed help is a separate package on
some Linux distributions; without it,
F1 takes you to the online help, which
is the same text on the web.

## What breaks when each part stops

| Symptom | Part to suspect |
|---|---|
| Everything odd, everywhere | the user profile |
| One format opens garbled | that format's filter |
| A conversion "works" but no file | the running instance (ch. 10) |
| Settings won't stick | profile permissions, or two processes fighting over one profile |
| Nothing starts at all | the install itself (ch. 3) |

With the parts named, the next chapter
puts the program on a machine.
