#!/usr/bin/env python3
"""Write one funny AI excuse for breaking production.

Winner pattern: concrete dev artifact (canary deploy) + 2-3 step
escalation (1% -> 10% -> everyone) + punchline in the last clause.
"""

import os

LINE = (
    "I canaried it to 1% of users, then 10%, then all of them, "
    "and the only thing that scaled was the outage."
)


def main():
    assert 1 <= len(LINE) <= 180, "entry must be 1-180 characters"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
