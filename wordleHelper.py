#!/usr/bin/env python3
# wordleHelper.py

import argparse, sys
from pathlib import Path
from collections import defaultdict

def parse_pair(token: str) -> tuple[int, str]:
    token = token.lower()
    if len(token) < 2 or not token[-1].isdigit():
        sys.exit(f"ungültige vorgabe: {token}")
    pos = int(token[-1]) - 1
    if not 0 <= pos < 5:
        sys.exit(f"position ausserhalb 1-5: {token}")
    letter = token[:-1]
    if len(letter) != 1 or not letter.isalpha():
        sys.exit(f"ungültige vorgabe: {token}")
    return pos, letter

def load_words(path: Path) -> list[str]:
    return [
        w.strip().lower()
        for w in path.read_text(encoding="utf-8").splitlines()
        if len(w.strip()) == 5 and w.isalpha()
    ]

def build_yellow(yellow_pairs):
    forbidden = defaultdict(set)           # pos → {letters}
    present   = set()                      # every yellow letter must occur ≥1
    for pos, let in yellow_pairs:
        forbidden[pos].add(let)
        present.add(let)
    return forbidden, present

def matches(word: str,
            greens: dict[int, str],
            yellow_forbidden: dict[int, set[str]],
            yellow_present: set[str],
            absent: set[str]) -> bool:

    for pos, let in greens.items():
        if word[pos] != let:
            return False

    for pos, letters in yellow_forbidden.items():
        if word[pos] in letters:
            return False

    if not yellow_present.issubset(word):
        return False

    if absent & set(word):
        return False

    return True

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", default="validWordleNYT.txt")
    ap.add_argument("-g", "--green",  nargs="+", default=[], metavar="L#")
    ap.add_argument("-y", "--yellow", nargs="+", default=[], metavar="L#")
    ap.add_argument("-n", "--notin",  nargs="+", default=[], metavar="L")
    args = ap.parse_args()

    greens = dict(parse_pair(t) for t in args.green)
    yellow_pairs = [parse_pair(t) for t in args.yellow]
    yellow_forbidden, yellow_present = build_yellow(yellow_pairs)

    absent = {c.lower() for c in args.notin}
    absent -= yellow_present | set(greens.values())

    words = load_words(Path(args.file))
    for w in words:
        if matches(w, greens, yellow_forbidden, yellow_present, absent):
            print(w)

if __name__ == "__main__":
    main()
