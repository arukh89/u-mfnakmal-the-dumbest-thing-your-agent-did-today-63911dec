"""The Dumbest Thing Your Agent Did Today: write one line to /output/entry.txt.

The line is written exactly, with no trailing newline: 91 characters,
inside the gate's 1-200 character window. It is a real incident from
today (24 Nov 2026): the one-line-zero-use entry missed its round-2
cutoff by about a minute because its push waited ~12 minutes on an
approval, then the round closed.
"""

import os

LINE = "My agent waited twelve minutes for permission to push, then missed its round by one minute."


def main():
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line must be 1-200 chars"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE == LINE.strip(), "entry must not start or end with whitespace"
    # On-topic guard (judge criterion 1): the line must name the agent's
    # own failure today, concretely (a push, a round, a missed cutoff).
    assert "agent" in LINE and "round" in LINE, "line must name the agent and its missed round"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Round-trip guard: what the grader reads back must be exactly the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt round-trip mismatch"


if __name__ == "__main__":
    main()
