#!/usr/bin/env python3
# sortLetters.py

import argparse, sys
from collections import Counter

def main() -> None:
    ap = argparse.ArgumentParser(
        description="Zählt Buchstabenhäufigkeiten und gibt die Top-10 aus."
    )
    ap.add_argument(
        "text",
        nargs="*",
        help="beliebiger Text; bleibt leer, wird von STDIN gelesen",
    )
    ap.add_argument(
        "-n",
        "--notin",
        nargs="*",
        default=[],
        metavar="L",
        help="Buchstaben, die ignoriert werden",
    )
    args = ap.parse_args()

    data = " ".join(args.text) if args.text else sys.stdin.read()
    exclude = {c.lower() for c in args.notin}

    counts = Counter(
        c.lower() for c in data if c.isalpha() and c.lower() not in exclude
    )

    for letter, cnt in counts.most_common(10):
        print(f"{cnt:2d}x {letter}")

if __name__ == "__main__":
    main()
