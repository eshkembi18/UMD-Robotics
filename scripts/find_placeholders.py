#!/usr/bin/env python3
"""List every unfilled placeholder in the docs, so you know what's left.

    python scripts/find_placeholders.py            # every placeholder, file:line
    python scripts/find_placeholders.py --summary  # counts per file
"""
import re
import sys
from collections import Counter
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"
PATTERN = re.compile(
    r"\[(TEAM VERIFICATION REQUIRED|ADD REAL [A-Z ]+|INSERT VERIFIED [A-Z ]+|RESULTS PENDING|TBD)\]"
)
SKIP = {"page-templates"}  # templates are supposed to contain placeholders


def main() -> None:
    summary = "--summary" in sys.argv
    counts: Counter[str] = Counter()
    for path in sorted(DOCS.rglob("*.md")):
        rel = path.relative_to(DOCS)
        if rel.parts[0] in SKIP:
            continue
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for m in PATTERN.finditer(line):
                counts[str(rel)] += 1
                if not summary:
                    print(f"docs/{rel}:{n}: [{m.group(1)}]")
    total = sum(counts.values())
    if summary:
        for f, c in counts.most_common():
            print(f"{c:4d}  docs/{f}")
    print(f"\n{total} placeholder(s) left in {len(counts)} file(s).")


if __name__ == "__main__":
    main()
