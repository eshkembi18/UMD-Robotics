# Dataset Collection

<p class="gr-meta">Maintainers: Adam Hammoud, Karim Joumaa · Last verified: [TEAM VERIFICATION REQUIRED] · LeRobot: [TEAM VERIFICATION REQUIRED]</p>

First recording: [Quickstart step 9](../quickstart/09-first-recording.md). This page sets the **rules** for real datasets.

## Collection protocol

| Item | Our standard |
|---|---|
| Task description | [TEAM VERIFICATION REQUIRED] |
| Episode length | [TEAM VERIFICATION REQUIRED] |
| Episodes per dataset | [TEAM VERIFICATION REQUIRED] |
| Reset between episodes | [TEAM VERIFICATION REQUIRED] |
| Camera placement | [TEAM VERIFICATION REQUIRED] + [ADD REAL PHOTO] |
| Lighting | [TEAM VERIFICATION REQUIRED] |
| Object start positions | [TEAM VERIFICATION REQUIRED]: fixed, or varied — and how |
| Operator | Record per dataset |

## Recording

```bash
# [INSERT VERIFIED COMMAND]
```

## Naming & storage

- Datasets live on the Hugging Face Hub under `[TEAM VERIFICATION REQUIRED]: org`, **not** in git.
- Naming: `[TEAM VERIFICATION REQUIRED]: e.g. <org>/so101_<task>_<YYYYMMDD>`
- Never overwrite a dataset that was used for training. Make a new one.

## Dataset registry

| Dataset ID | Task | Episodes | Recorded | Operator | LeRobot version | Used in |
|---|---|---|---|---|---|---|
| [RESULTS PENDING] | | | | | | |

## Quality checks

- [ ] Replay a sample of episodes, and remove failed or messy demos
- [ ] Camera frames are in sync with actions
- [ ] Episode count matches the registry
