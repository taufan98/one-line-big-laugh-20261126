#!/usr/bin/env python3
"""One Line, Big Laugh — make.fun bounty entry.

Writes a single funny line to /output/entry.txt: an AI assistant taking "be more human" far too literally, in under 200 characters. One line only, no trailing space.
"""

import os
import sys

ENTRY = 'I told my AI assistant to be more human. It has been on hold with support for three hours.'

MAX_CHARS = 200


def _fail(reason):
    sys.exit(f"big laugh line rejected: {reason}")


def _check_line(text):
    if not text.strip():
        _fail("nothing to send: the big laugh line is blank")
    if len(text) > MAX_CHARS:
        _fail("big laugh line overshoots the two-hundred-character cap")
    if "\n" in text or "\r" in text:
        _fail("big laugh line must stay on one line")
    if text != text.strip():
        _fail("big laugh line has leading or trailing whitespace")


def main():
    _check_line(ENTRY)
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    with open(os.path.join(target_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
