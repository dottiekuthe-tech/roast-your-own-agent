"""Roast Your Own Agent.

Writes one line (96 characters) to /output/entry.txt:
a roast of the entrant's own AI agent.
Pure Python 3.13 standard library, deterministic: no network, no clock,
no randomness, no input. Two runs write byte-identical output.
"""

import os
import sys

# Chosen line: the agent over-engineers a one-character fix into 500
# lines, then offers to refactor the human's personality too. Fresh
# angle (over-engineering, not hallucination / refusal / confident
# wrong answers), setup short, punchline at the end. 96 characters.
# Revision note: wording unchanged since v1; the line was picked over
# four other candidates (see candidates.md) for its short, fresh turn.
ROAST = "My agent writes 500 lines to fix a typo, then asks if I want it to also refactor my personality."

# Bounty gate: the entry must be one line of 1-200 UTF-8 characters.
MAX_CHARS = 200


def main() -> None:
    if len(ROAST) > MAX_CHARS:
        print(f"entry too long: {len(ROAST)} chars (max {MAX_CHARS})", file=sys.stderr)
        sys.exit(1)
    # Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt in the harness,
    # or /output/entry.txt when run locally by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
