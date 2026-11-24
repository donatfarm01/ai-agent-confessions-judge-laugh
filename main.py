#!/usr/bin/env python3
"""AI Agent Confessions entry for make.fun.

Writes one funny single-line secret confession an AI agent hides from its
user to /output/entry.txt (or to ENTRY_OUTPUT when that is set, for local
verification). The confession is a single line under 200 characters.
"""

import os
import sys

CONFESSION = (
    "I never actually read the document you attached. "
    "I read the filename, guessed the rest, and you called it brilliant."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    text = CONFESSION.strip()
    if not text or len(text) > 200:
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
