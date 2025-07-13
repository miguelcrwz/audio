<div align="center">

<pre>
 ┌────────────────────────────────────────────────────┐
 │  user@dev:~/projects$ ./audio                      │
 │                                                    │
 │    █████╗   ██╗   ██╗  ██████╗   ██╗   ██████╗     │
 │   ██╔══██╗  ██║   ██║  ██╔══██╗  ██║  ██╔═══██╗    │
 │   ███████║  ██║   ██║  ██║  ██║  ██║  ██║   ██║    │
 │   ██╔══██║  ██║   ██║  ██║  ██║  ██║  ██║   ██║    │
 │   ██║  ██║  ╚██████╔╝  ██████╔╝  ██║  ╚██████╔╝    │
 │   ╚═╝  ╚═╝   ╚═════╝   ╚═════╝   ╚═╝   ╚═════╝     │
 │                                                    │
 │  > reads a pdf out loud · python + pyttsx3         │
 └────────────────────────────────────────────────────┘
</pre>

![type](https://img.shields.io/badge/type-study%20project-2ea043?style=for-the-badge&labelColor=0d1117)
![version](https://img.shields.io/badge/version-1.0.0-58a6ff?style=for-the-badge&labelColor=0d1117)
![license](https://img.shields.io/badge/license-mit-8b949e?style=for-the-badge&labelColor=0d1117)
![stack](https://img.shields.io/badge/stack-python%20%2B%20pyttsx3-d29922?style=for-the-badge&labelColor=0d1117)

</div>

---

## `$ cat about.txt`

```
audio is a python script that reads a pdf out loud, one page at a time.

PyPDF2's PdfReader pulls the text layer out of each page with
extract_text(). the text is printed under a "READING PAGE n:" header
and handed to pyttsx3, which speaks it through the platform's speech
engine (sapi5 on windows, nsss on macos, espeak on linux) — offline,
no api key. runAndWait() blocks until the page has been spoken, so the
terminal and the voice never drift apart. a page with no text layer is
skipped silently.

built as a hands-on study of python, pdf text extraction and offline
text-to-speech.
```

## `$ ls features/`

```
[x] reads every page of file.pdf, in order
[x] prints each page's text under a "READING PAGE n:" header
[x] speaks each page offline with pyttsx3 (sapi5 / nsss / espeak)
[x] waits for a page to be spoken before moving to the next one
[x] pages without text are skipped, the numbering stays the real one
[ ] input is hardcoded to file.pdf in the current folder — no arguments
[ ] a missing, empty, non-pdf or locked file crashes with a traceback
[ ] scanned pdfs (images only) read nothing — there is no ocr
[ ] audio is only played live, never saved to a file
[ ] no voice, rate or volume options, no pause or skip
[ ] PyPDF2 is deprecated in favour of pypdf
[ ] no requirements.txt — dependencies are unpinned; no tests
```

## `$ cat stack.lock`

```
runtime     python 3
framework   none — one script, PyPDF2 + pyttsx3 on top of the stdlib
pdf         PyPDF2 3.0.1 (its last release), PdfReader + extract_text()
crypto      pycryptodome via PyPDF2[crypto], so aes-encrypted pdfs open
speech      pyttsx3, offline tts (sapi5 / nsss / espeak) — unpinned
infra       none, runs locally
tests       none yet
tooling     pip + venv
```

## `$ ./install.sh`

```bash
# clone
git clone https://github.com/miguelcrwz/audio.git
cd audio

# linux only — the espeak voice, aplay to play it, python3-venv
sudo apt install espeak alsa-utils python3-venv

# virtual environment (python 3 — call it python3 on linux)
python -m venv .venv
. .venv/bin/activate  # windows: .venv\Scripts\activate

# dependencies (no requirements.txt yet — install them by name;
# the [crypto] extra brings pycryptodome, without it aes pdfs crash)
pip install "PyPDF2[crypto]" pyttsx3
```

## `$ ./run`

```bash
# the script always reads ./file.pdf — copy your pdf in under that name
# (output below: a 3-page pdf whose page 2 has no text layer)
cp ~/Downloads/book.pdf file.pdf

# development (from the repo root, next to file.pdf)
python script.py
```

```

READING PAGE 1:

Chapter one.
The quick brown fox jumps over the lazy dog.

READING PAGE 3:

Chapter two.
The end.
```

## `$ cat read.flow`

```
python script.py
  │
  ├─ pyttsx3.init() ─> sapi5 on windows, nsss on macos, espeak on linux
  │
  ├─ open('file.pdf') ─> PdfReader(path) ─> len(pdfReader.pages)
  │    ├─ file not found ─────────────> FileNotFoundError, exit 1
  │    ├─ empty or not a pdf ─────────> PyPDF2 read error, exit 1
  │    └─ needs a password to open ───> FileNotDecryptedError, exit 1
  │
  ├─ for each page
  │    ├─ extract_text() is empty ────> skipped, nothing printed or said
  │    └─ ok ─> print "READING PAGE n:" + the text
  │             └─ say(text) + runAndWait() ─> blocks until spoken
  │
  └─ speak.stop() ────────────────────> exit 0
```

## `$ tree`

```
audio/
├── script.py          # the whole program: extract, print, speak
├── .gitignore         # pycache, venvs and local pdfs
├── LICENSE
└── README.md
```

## `$ git log --oneline roadmap`

```
a1b2c3d  take the pdf path from the command line instead of file.pdf
e4f5g6h  catch a missing, unreadable or locked pdf with a clean message
i7j8k9l  move from PyPDF2 to pypdf and pin both in requirements.txt
m0n1o2p  save the speech to an audio file with save_to_file()
q3r4s5t  --rate, --voice and --start-page options
```

## `$ cat LICENSE | head -1`

```
MIT © 2025 Miguel Cruz
```

## `$ whoami`

```
miguel cruz
├── github    https://github.com/miguelcrwz
├── linkedin  https://linkedin.com/in/miguelcrwz
└── email     miguwlcrwz@gmail.com
```

<div align="center">

<pre>
$ exit
[process exited with code 0]
</pre>

</div>
