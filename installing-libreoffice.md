# Installing LibreOffice

One install gets you the whole suite —
all six components share the engine
(chapter 2), so there is nothing to
pick and choose at install time on a
normal computer. The exception, which
matters to this guide's later chapters,
is the **headless build**: a packaging
variant with the windows left out, made
for servers. Know which one you have.

## Windows and macOS

Download the installer from
**libreoffice.org** — not from a
lookalike site; the genuine article is
free, so anyone charging for the
download is selling you something else.
On Windows it is a standard installer
(MSI); on macOS, a disk image you drag
to Applications (the build is signed,
so Gatekeeper lets it through). A
Java runtime is optional: a few corners
(Base's built-in database, some
assistive tools) use it, and the
program will tell you if it ever wants
one. The lab's full install pulled a
JRE in on its own and, in doing so,
silenced a warning that had ridden
along on every earlier conversion —
before that, each run began
`Warning: failed to launch javaldx -
java may not function correctly`, and
everything in this guide worked anyway.
That is the right spirit to read it in
if you ever meet it: a grumble, not a
stop sign.

## Linux

Your distribution's package manager
has it:

```
sudo apt install libreoffice      # Debian, Ubuntu
sudo dnf install libreoffice      # Fedora
```

The pieces arrive as several packages
(the lab's machine ended with twenty
`libreoffice-*` packages: a common
core, one per component, the help and
the theme). Flatpak and Snap builds
exist and are official; they keep the
program in its own compartment, which
mostly matters when chapter 10's
profile tricks need to find the real
profile folder — inside the
compartment's home, not the obvious
one.

## The headless variant, and how to tell

Servers and containers often carry the
**-nogui** packages instead
(`libreoffice-core-nogui`,
`libreoffice-writer-nogui` and kin on
Debian/Ubuntu). Same version, same
engine, same conversions — no windows.
The lab's sandbox arrived exactly like
that: every conversion in chapters 9
and 10 ran on the nogui build of
24.2.7 before the full suite was
installed beside the work. The tell is
in the package list:

```
$ dpkg -l 'libreoffice*' | grep ^ii
```

Names ending `-nogui` mean the engine
without the face. On such a machine,
`soffice` with no `--headless` flag
has nothing to show you; with the
flag, it is complete. Neither shape is
a lesser LibreOffice — they are the
same program with the lights off or on.

## Prove the install

Two checks, thirty seconds:

```
$ soffice --version
LibreOffice 24.2.7.2 420(Build:2)

$ soffice --headless --convert-to pdf --outdir /tmp any-letter.docx
```

The first proves the program answers;
the second proves the engine works —
a PDF appears, or chapter 17 has your
symptom. GUI people can simply start
the program and meet the Start Center
(chapter 4).

## Keeping it current

The community build releases a new
series roughly twice a year, with
monthly corrections between. Linux
distributions trail that by their own
schedule — the lab's 24.2.7 was Ubuntu
24.04's build of the 24.2 series, and
that lag is normal and mostly harmless.
Formats do not expire; a three-year-old
LibreOffice still reads today's files.
Update for security and for conversion
quality, not out of panic.
