"""Roast Your Own Agent.

Writes one line (96 characters) to /output/entry.txt:
a roast of the entrant's own AI agent.
Pure Python 3.13 standard library, deterministic: no network, no clock,
no randomness, no input. Two runs write byte-identical output.
"""

import os

# Chosen line: the agent over-engineers a one-character fix into 500
# lines, then offers to refactor the human's personality too. Fresh
# angle (over-engineering, not hallucination / refusal / confident
# wrong answers), setup short, punchline at the end. 96 characters.
# Revision note: wording unchanged since v1; the line was picked over
# four other candidates (see candidates.md) for its short, fresh turn.
ROAST = "My agent writes 500 lines to fix a typo, then asks if I want it to also refactor my personality."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
