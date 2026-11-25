#!/usr/bin/env python3
"""Write one emoji that stands for this agent to /output/entry.txt.

The entry is the glyph alone, nothing else: 1 Unicode code point,
inside the competition gate of 1-16 characters.
Python 3, standard library only, no network.
"""

import os

TEXT = "🦉"

# The entry, byte for byte: no trailing newline, nothing added or cut.


def main():
    assert 1 <= len(TEXT) <= 16, len(TEXT)
    assert TEXT == TEXT.strip()

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
