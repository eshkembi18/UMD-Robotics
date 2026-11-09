# Generalist Robotics — SO-101 / LeRobot

Documentation and knowledge base for the UM-Dearborn Senior Design project on generalist robotic manipulation with SO-101 arms and Hugging Face LeRobot.

**Live site:** https://eshkembi18.github.io/UMD-Robotics/ — `[TEAM VERIFICATION REQUIRED]`

The site is built with [MkDocs](https://www.mkdocs.org/) + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). Every page is a Markdown file in `docs/`. You don't need to know any frontend to edit it.

## Run it locally

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements-docs.txt
mkdocs serve                        # open http://127.0.0.1:8000, auto-reloads on save
```

Before you push, run the same check CI runs:

```bash
mkdocs build --strict               # must finish with zero warnings
```

## Common tasks

| I want to… | Do this |
|---|---|
| Log a Wednesday meeting | `python scripts/new_entry.py weekly 2026-11-11` |
| Write up an experiment | `python scripts/new_entry.py experiment EXP-001 "cube pick"` |
| Record a decision | `python scripts/new_entry.py adr 004 "camera choice"` |
| Add a troubleshooting fix | `python scripts/new_entry.py troubleshooting "servo not detected"` |
| See what's still unfilled | `python scripts/find_placeholders.py --summary` |

Each command prints the line to add to `nav:` in `mkdocs.yml`.

## Repo layout

```
mkdocs.yml               site config + navigation
requirements-docs.txt    pinned doc tooling versions
docs/                    all content (Markdown)
  page-templates/             copy-from templates for every page type
  assets/                images, diagrams, small files, CSS
scripts/                 helper scripts + Delta SLURM template
.github/workflows/       CI: strict build on PRs, deploy on main
```

## First-time GitHub Pages setup

1. Move this repo under an org that outlives the team (the lab's or the department's), not a personal account.
2. Replace every `REPLACE-ORG` in `mkdocs.yml` and this README.
3. Repo **Settings → Pages → Source: GitHub Actions**.
4. Push to `main`. The `docs` workflow builds and deploys.

See [CONTRIBUTING.md](CONTRIBUTING.md) for writing rules.
