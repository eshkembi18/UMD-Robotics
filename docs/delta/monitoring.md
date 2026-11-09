# 7. Monitoring & Failed Jobs

<p class="gr-meta">Maintainers: Adam Hammoud, Karim Joumaa · Last verified: [TEAM VERIFICATION REQUIRED]</p>

!!! danger "Site-specific: check the current Delta docs"
    Hostnames, partitions, paths, modules, and limits are set by NCSA and change over time. Check everything marked `[TEAM VERIFICATION REQUIRED]` against the [Delta documentation](https://docs.ncsa.illinois.edu/systems/delta/).

## Watching jobs

```bash
squeue -u $USER                 # your jobs and their state
scancel <jobid>                 # cancel a job
sacct -j <jobid>                # accounting info after a job ends
tail -f logs/gr-train-<jobid>.out
```

Delta-specific tools for job efficiency / allocation usage: [TEAM VERIFICATION REQUIRED]

## Reading logs

Our template writes:

- `logs/<job-name>-<jobid>.out`: normal output
- `logs/<job-name>-<jobid>.err`: errors and tracebacks. **Read this first** when a job fails.

## Failed jobs

| Symptom | Where to look | Likely cause | Fix |
|---|---|---|---|
| Stuck in pending | `squeue` reason column | Waiting for resources, or the request can't be satisfied | Shrink the request, or check partition limits |
| Killed at the time limit | `.err`, `sacct` state | Walltime too short | Raise `--time`, or resume from a checkpoint |
| CUDA out of memory | `.err` | Batch too large for the GPU | Lower the batch size |
| Host memory exceeded | `.err`, `sacct` | `--mem` too low | Raise `--mem` |
| Can't download dataset / model | `.err` | Not logged in, or no internet on compute nodes | See [Moving Data](data-transfer.md) |
| Import errors | `.err` | Wrong env or modules | Check the activation lines in the template |

Anything new goes to [Troubleshooting → GPU cluster](../troubleshooting/gpu-cluster.md).
