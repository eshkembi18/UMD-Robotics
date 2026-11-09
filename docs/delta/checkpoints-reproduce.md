# 8. Checkpoints & Reproducibility

<p class="gr-meta">Maintainers: Adam Hammoud, Karim Joumaa · Last verified: [TEAM VERIFICATION REQUIRED]</p>

!!! danger "Site-specific: check the current Delta docs"
    Hostnames, partitions, paths, modules, and limits are set by NCSA and change over time. Check everything marked `[TEAM VERIFICATION REQUIRED]` against the [Delta documentation](https://docs.ncsa.illinois.edu/systems/delta/).

## Getting checkpoints back

Push the final checkpoint to the Hugging Face Hub under the experiment ID:

```bash
# [INSERT VERIFIED COMMAND]
```

Then add it to the [checkpoint registry](../software/checkpoints.md) and the matching [experiment page](../experiments/index.md).

## Reproducing a run

Every completed run should be reproducible from its experiment page alone. Record:

- [ ] Git commit of the code
- [ ] LeRobot version
- [ ] Dataset ID **and revision**
- [ ] Full training command and config
- [ ] The exact SLURM script (committed)
- [ ] Delta modules / environment used
- [ ] Checkpoint link
- [ ] Runtime and GPU type

To re-run: check out the commit, use the same environment, and `sbatch` the same script with the same `EXPERIMENT_ID` suffix (e.g. `EXP-003-rerun`).
