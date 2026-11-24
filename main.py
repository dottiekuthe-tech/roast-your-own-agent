#!/usr/bin/env python3
"""Roast Your Own Agent — one line to /output/entry.txt.

Writes a single self-roast line (<=200 chars) to the output file.
Pure stdlib, offline, deterministic: no network, no clock, no randomness.
"""
import os

LINE = "My agent writes 500 lines to fix a typo, then asks if I want it to also refactor my personality."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
