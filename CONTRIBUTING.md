# Contributing

This site is how the next team learns everything we figured out. Keep it accurate first, complete second, pretty third.

## Workflow

1. Branch from `main`: `git checkout -b docs/servo-calibration`
2. Edit Markdown in `docs/`. Preview with `mkdocs serve`.
3. Run `mkdocs build --strict`. Fix any warning.
4. Open a PR. One teammate reviews. The page owner reviews if it's their page.
5. Merge. CI deploys.

Tie docs to real work: a Jira ticket isn't done until the docs it touches are updated.

## Page owners

| Area | Owners |
|---|---|
| Quickstart steps 1–5, Hardware | Era Shkembi, Tristan Elizalde |
| Quickstart steps 6–9, Software & ML, NCSA Delta | Adam Hammoud, Karim Joumaa |
| Experiments, Troubleshooting, Decisions, Weekly Log, Handoff | Whole team |

## Writing rules

**Never make things up.** If you don't have the real value, use a placeholder:

| Placeholder | Use when |
|---|---|
| `[TEAM VERIFICATION REQUIRED]` | a fact or value nobody has confirmed yet |
| `[INSERT VERIFIED COMMAND]` | a command nobody has run successfully on our setup yet |
| `[ADD REAL PHOTO]` / `[ADD REAL DIAGRAM]` / `[ADD REAL VIDEO]` | media to come |
| `[RESULTS PENDING]` | an experiment not run or not analyzed yet |

`python scripts/find_placeholders.py` lists everything left.

**Mark status honestly.** Use these badges:

```html
<span class="status planned">Planned</span>
<span class="status progress">In progress</span>
<span class="status done">Implemented</span>
<span class="status validated">Validated</span>
```

"Implemented" means it works. "Validated" means it was tested with recorded results in an experiment page.

**Commands:** only paste commands you actually ran on our setup. Note the LeRobot version / commit hash you ran them against. LeRobot's CLI changes between versions.

**Every how-to page** starts with a meta line and ends with a "Last verified" date:

```html
<p class="gr-meta">Maintainer: Name · Last verified: YYYY-MM-DD · LeRobot: version/commit</p>
```

**Secrets never go in this repo.** No tokens, passwords, SSH keys, allocation credentials, or personal contact info. Describe *where* access lives and *who* to ask, not the access itself.

**Big files stay out of git.** Datasets and checkpoints go to Hugging Face. Videos go to YouTube (unlisted) or the HF repo. Link to them. Small images and GIFs (under ~5 MB) can go in `docs/assets/`.

## Style

- Short sentences. Steps are numbered. One action per step.
- Say what the reader should *see* after important steps.
- Use the same names everywhere: "leader arm", "follower arm", "STS3215", "LeRobot", "NCSA Delta".
- Link to other pages with relative paths, e.g. `[calibration](../quickstart/06-calibration.md)`. The strict build catches broken ones.
