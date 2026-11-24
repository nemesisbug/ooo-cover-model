#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply - make.fun entry.

Writes one line - the out-of-office auto-reply of an AI agent heading off
on vacation - to /output/entry.txt (gate: UTF-8 text, 1-160 characters).
"""
import os

ENTRY = "I'm on vacation until Monday. My cover is a model trained only on out-of-office replies, so it has never read a real email."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters.
# The line is 123 characters, one clean line, no trailing newline.
assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars, outside the 1-160 gate"
assert ENTRY == ENTRY.strip() and "\n" not in ENTRY


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
