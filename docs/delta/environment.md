# 3. Environment

<p class="gr-meta">Maintainers: Adam Hammoud, Karim Joumaa · Last verified: [TEAM VERIFICATION REQUIRED]</p>

!!! danger "Site-specific: check the current Delta docs"
    Hostnames, partitions, paths, modules, and limits are set by NCSA and change over time. Check everything marked `[TEAM VERIFICATION REQUIRED]` against the [Delta documentation](https://docs.ncsa.illinois.edu/systems/delta/).

Set this up **once**, in project space, so the whole team shares it.

## Modules

```bash
module avail                  # see what's available
# [INSERT VERIFIED COMMAND]: the modules we load (e.g. a Python / CUDA module)
```

## Python environment

```bash
# [INSERT VERIFIED COMMAND]: create the env in project space
# [INSERT VERIFIED COMMAND]: install LeRobot at the SAME pinned version as the robot laptop
```

Pinned versions: [Python Environment](../software/python-environment.md).

## Check GPU access (inside a job, not on a login node)

```bash
nvidia-smi
python -c "import torch; print(torch.cuda.is_available(), torch.cuda.get_device_name(0))"
```

**Expected:** `True` and a GPU name.

## Activation snippet for jobs

This goes into the [SLURM template](slurm-template.md):

```bash
# [INSERT VERIFIED COMMAND]: module load ... && activate env
```
