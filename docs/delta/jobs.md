# 5. Submitting Jobs

<p class="gr-meta">Maintainers: Adam Hammoud, Karim Joumaa · Last verified: [TEAM VERIFICATION REQUIRED]</p>

!!! danger "Site-specific: check the current Delta docs"
    Hostnames, partitions, paths, modules, and limits are set by NCSA and change over time. Check everything marked `[TEAM VERIFICATION REQUIRED]` against the [Delta documentation](https://docs.ncsa.illinois.edu/systems/delta/).

Delta uses the **SLURM** scheduler. You describe the resources you need in a job script, submit it, and it runs when resources are free.

## Submit

```bash
cd <code repo on Delta>
sbatch scripts/delta/train.slurm
```

Our script: [SLURM Job Template](slurm-template.md).

## Requesting GPUs and resources

| Directive | What it controls | Our value |
|---|---|---|
| `--account` | Which allocation gets charged | [TEAM VERIFICATION REQUIRED] |
| `--partition` | Which group of nodes (GPU type) | [TEAM VERIFICATION REQUIRED]: check current partitions in Delta docs |
| GPU request (e.g. `--gpus-per-node`) | Number of GPUs | [TEAM VERIFICATION REQUIRED]: confirm Delta's preferred form |
| `--cpus-per-task` | CPU cores for data loading | [TEAM VERIFICATION REQUIRED] |
| `--mem` | RAM | [TEAM VERIFICATION REQUIRED] |
| `--time` | Max walltime (job gets killed after) | [TEAM VERIFICATION REQUIRED]: partition limit |

!!! tip "Ask for what you need"
    Bigger requests wait longer in the queue and use up the allocation faster. Start small, measure, and then scale.

## Interactive sessions (for debugging)

```bash
# [INSERT VERIFIED COMMAND]: srun / salloc for a short interactive GPU session
```

Use these to debug environment problems before wasting a full batch job.
