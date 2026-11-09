#!/usr/bin/env python3
"""Create a new page from a template, so nobody starts from a blank file.

    python scripts/new_entry.py weekly 2026-11-11
    python scripts/new_entry.py experiment EXP-001 "pick-and-place-cube"
    python scripts/new_entry.py adr 004 "camera-choice"
    python scripts/new_entry.py troubleshooting "servo-not-detected"

It prints the line to paste into mkdocs.yml `nav:` (pages not in nav
trigger a warning, and the CI build runs with --strict).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
TEMPLATES = DOCS / "page-templates"


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def body(template: str) -> str:
    text = (TEMPLATES / template).read_text(encoding="utf-8")
    # Templates show their content inside a ```markdown fence; pull it out.
    m = re.search(r"````markdown\n(.*?)\n````", text, re.S)
    if not m:
        sys.exit(f"Template {template} has no ````markdown block")
    return m.group(1) + "\n"


def main() -> None:
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    kind, ident = sys.argv[1], sys.argv[2]
    title = sys.argv[3] if len(sys.argv) > 3 else ""

    if kind == "weekly":
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", ident):
            sys.exit("Date must be YYYY-MM-DD")
        year, month = int(ident[:4]), int(ident[5:7])
        term = f"{'fall' if month >= 8 else 'winter'}-{year}"
        out = DOCS / "weekly-log" / term / f"{ident}.md"
        text = body("weekly-meeting.md").replace("YYYY-MM-DD", ident, 1)
        nav = f"- {ident}: weekly-log/{term}/{ident}.md"
    elif kind == "experiment":
        out = DOCS / "experiments" / f"{ident.lower()}-{slug(title)}.md"
        text = body("experiment.md").replace("EXP-000: Short title", f"{ident.upper()}: {title or 'Short title'}")
        nav = f"- \"{ident.upper()}: {title}\": experiments/{out.name}"
    elif kind == "adr":
        num = ident.zfill(3)
        out = DOCS / "decisions" / f"adr-{num}-{slug(title)}.md"
        text = body("adr.md").replace("ADR-000: Decision title", f"ADR-{num}: {title or 'Decision title'}")
        nav = f"- \"ADR-{num}: {title}\": decisions/{out.name}"
    elif kind == "troubleshooting":
        out = DOCS / "troubleshooting" / f"{slug(ident)}.md"
        text = body("troubleshooting-entry.md").replace("Symptom in plain words (what you saw)", ident, 1)
        nav = f"- {ident}: troubleshooting/{out.name}"
    else:
        sys.exit(f"Unknown kind '{kind}'. Use weekly | experiment | adr | troubleshooting")

    if out.exists():
        sys.exit(f"{out.relative_to(ROOT)} already exists")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"Created {out.relative_to(ROOT)}")
    print(f"Add to mkdocs.yml nav:\n    {nav}")


if __name__ == "__main__":
    main()
