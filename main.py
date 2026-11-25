#!/usr/bin/env python3
"""Worst Superpower entry.

Writes one line (at most 140 characters) inventing a superpower and,
in the same breath, why it is useless, to /output/entry.txt.
Deterministic: the same line on every run. No network, no model calls.

The line: a hero who can call down rain, but only indoors, only onto
their own head, and only while already sheltered by an umbrella --
three layers of uselessness in one breath, and a picture the reader
can see at once.
"""

import os

ENTRY = (
    "I can summon rain indoors, but only over my own head, "
    "and only when I am already holding an umbrella."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
