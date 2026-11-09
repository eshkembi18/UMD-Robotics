# Policy Training

<p class="gr-meta">Maintainers: Adam Hammoud, Karim Joumaa · Last verified: [TEAM VERIFICATION REQUIRED] · LeRobot: [TEAM VERIFICATION REQUIRED]</p>

Training runs on NCSA Delta: [Delta guide](../delta/index.md).

## Configuration

| Item | Value |
|---|---|
| Policy type | [TEAM VERIFICATION REQUIRED] |
| Starting weights | [TEAM VERIFICATION REQUIRED]: pretrained model ID, or from scratch |
| Key hyperparameters | [TEAM VERIFICATION REQUIRED] |
| Typical runtime | [RESULTS PENDING] |

## Command

```bash
# [INSERT VERIFIED COMMAND]: the exact training command for our pinned LeRobot version
```

It also goes in [`scripts/delta/train.slurm`](../delta/slurm-template.md).

## Rules

- Every training run that matters becomes an [experiment page](../experiments/index.md).
- Record the dataset **revision**, not just its name.
- Log training curves [TEAM VERIFICATION REQUIRED]: where (e.g. W&B project, or TensorBoard logs saved with the checkpoint)
