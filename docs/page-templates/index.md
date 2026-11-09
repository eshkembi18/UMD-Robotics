# Templates

Start every new page from a template so the site stays consistent. Two ways to do it:

**Script (recommended):**

```bash
python scripts/new_entry.py weekly 2026-11-11
python scripts/new_entry.py experiment EXP-001 "cube pick"
python scripts/new_entry.py adr 004 "camera choice"
python scripts/new_entry.py troubleshooting "servo not detected"
```

**By hand:** copy the Markdown block from the page below into a new file, then add the file to `nav:` in `mkdocs.yml`.

| Template | For |
|---|---|
| [Procedure Guide](procedure.md) | Any how-to page (Quickstart steps, setup guides) |
| [Experiment Report](experiment.md) | Every experiment or training run that matters |
| [Troubleshooting Entry](troubleshooting-entry.md) | Each problem we hit and solved (or didn't) |
| [Decision Record (ADR)](adr.md) | Any choice the next team might question |
| [Weekly Meeting](weekly-meeting.md) | Wednesday meetings |
