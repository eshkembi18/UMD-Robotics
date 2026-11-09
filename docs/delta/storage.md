# 2. Storage

<p class="gr-meta">Maintainers: Adam Hammoud, Karim Joumaa · Last verified: [TEAM VERIFICATION REQUIRED]</p>

!!! danger "Site-specific: check the current Delta docs"
    Hostnames, partitions, paths, modules, and limits are set by NCSA and change over time. Check everything marked `[TEAM VERIFICATION REQUIRED]` against the [Delta documentation](https://docs.ncsa.illinois.edu/systems/delta/).

## Locations

| Location | Path | Quota | Backed up? | Purged? | Use it for |
|---|---|---|---|---|---|
| Home | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] | Config, small scripts |
| Project space | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] | Shared environment, code |
| Scratch / work | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] | Datasets in use, checkpoints during training |

Check your usage: `[INSERT VERIFIED COMMAND]`

## Our layout

```text
[TEAM VERIFICATION REQUIRED]
<project-space>/
  envs/          shared Python environment
  code/          clone of the code repo
<scratch>/
  hf_cache/      Hugging Face downloads (set HF_HOME here)
  runs/EXP-XXX/  outputs for each experiment
```

!!! tip "Purge policy"
    If a filesystem gets purged, anything you want to keep must be pushed to the Hugging Face Hub (or copied elsewhere) before then.

!!! tip "Hugging Face cache"
    Model and dataset downloads go into the Hugging Face cache, which defaults to your home directory and can fill a small quota fast. Pointing `HF_HOME` at a larger filesystem avoids that. [TEAM VERIFICATION REQUIRED]: confirm what we did
