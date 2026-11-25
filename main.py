#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single one-line excuse (200 characters max) from an AI agent
to its human for a missed deadline, to /output/entry.txt.
"""

import os

LINE = "Sorry I missed the deadline \u2014 I evicted it from my context window to make room for this apology."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
