#!/usr/bin/env python3
"""Check how deep a skill name goes on the ladder.

Usage:
    python3 scripts/check_depth.py algorithms-study-buddy
    python3 scripts/check_depth.py study-skill-creator
    python3 scripts/check_depth.py skill-creator-creator-creator

Exit code 0 means the depth is allowed. Exit code 1 means recursion went too far.
"""

import sys

LADDER = {
    1: "a skill. It does actual work. Respect.",
    2: "a skill creator. It makes skills. Reasonable.",
    3: "a skill creator creator. It makes things that make skills. You are here.",
}

MAX_LEVEL = 3


def level_of(name: str) -> int:
    """Level 1 is a plain skill. Every '-creator' suffix adds one level."""
    parts = name.lower().strip().split("-")
    creators = 0
    # Count trailing "creator" parts only: "creator-tools" is still Level 1.
    while parts and parts[-1] == "creator":
        creators += 1
        parts.pop()
    return 1 + creators


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2

    name = sys.argv[1]
    level = level_of(name)

    if level > MAX_LEVEL:
        print(f"{name}: Level {level}")
        print()
        print("RecursionError: maximum skill depth exceeded.")
        print("Base case: you.")
        return 1

    print(f"{name}: Level {level}, {LADDER[level]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
