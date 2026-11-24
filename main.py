"""One Word for Your Wi-Fi — make.fun entry.

Writes a single original word to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt).

The word: Ghosted.

Home Wi-Fi's most recognisable move is vanishing mid-sentence —
right in the middle of a call, a match, a download — with no
warning and no explanation. That is exactly what being ghosted
is: someone who was right there suddenly stops answering. The
joke needs no setup and no footnote: one familiar word, borrowed
from dating, pinned on a router. It is funny at once, it is true
about how home Wi-Fi actually behaves, and it is not the word
everyone reaches for (no buffering, no loading, no FBI van).
As a network name it works on its own — a neighbour scrolling
the network list reads "Ghosted" and smiles, because theirs
does it too.

Pure Python standard library only.
"""

import os
import sys

# The Wi-Fi word. 7 characters, one word, plain ASCII.
WORD = "Ghosted"

MIN_CHARS = 1
MAX_CHARS = 20


def validate(text):
    """Enforce the competition gate before anything is written."""
    if not isinstance(text, str):
        raise ValueError("word is not text")
    if not text.strip():
        raise ValueError("word is blank or whitespace only")
    if "\n" in text or "\r" in text:
        raise ValueError("word must be a single word")
    if any(ch.isspace() for ch in text):
        raise ValueError("word must be a single token, no whitespace inside")
    if not text.isalpha():
        raise ValueError("word must be letters only, so a reader gets it instantly")
    if any(ord(ch) < 32 for ch in text):
        raise ValueError("word contains control characters")
    if text != text.strip():
        raise ValueError("word has leading or trailing whitespace")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            "word is %d characters, gate is %d-%d"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
    text.encode("utf-8")  # must be valid UTF-8
    return text


def main():
    word = validate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(word)
    # Read it back and confirm what landed on disk is exactly the word.
    with open(path, "r", encoding="utf-8", newline="") as fh:
        written = fh.read()
    if written != word:
        raise SystemExit("read-back mismatch: entry.txt != word")
    print("wrote %d chars to %s" % (len(word), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
