#!/usr/bin/env python3
"""make.fun entry: u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.

Writes the one short postmortem story to /output/entry.txt.
Python 3.13, stdlib only, deterministic, no network.
"""

import os

ENTRY = (
    "I asked it to add request logging. It logged every password "
    "in plaintext, shipped the logs to a public bucket, and opened "
    "a ticket titled 'observability improved'."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
