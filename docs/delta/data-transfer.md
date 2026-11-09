# 4. Moving Data

<p class="gr-meta">Maintainers: Adam Hammoud, Karim Joumaa · Last verified: [TEAM VERIFICATION REQUIRED]</p>

!!! danger "Site-specific: check the current Delta docs"
    Hostnames, partitions, paths, modules, and limits are set by NCSA and change over time. Check everything marked `[TEAM VERIFICATION REQUIRED]` against the [Delta documentation](https://docs.ncsa.illinois.edu/systems/delta/).

## Default: through the Hugging Face Hub

Datasets live on the Hub ([Dataset Collection](../software/dataset-collection.md)), and the training job downloads them by ID.

1. Log in to Hugging Face once on Delta, using a token you created yourself. **Never** paste the token into a file in this repo.
    ```bash
    # [INSERT VERIFIED COMMAND]: Hugging Face CLI login
    ```
2. Check whether compute nodes can reach the internet. [TEAM VERIFICATION REQUIRED]
    - **If yes:** the job downloads the dataset itself.
    - **If no:** pre-download on the login node into the cache:
        ```bash
        # [INSERT VERIFIED COMMAND]
        ```

## Local files (not on the Hub)

```bash
# [INSERT VERIFIED COMMAND]: rsync / scp / Globus. Whichever we used
```

## Rules

- Training reads a **specific dataset revision**. Record it in the experiment page.
- Don't keep the only copy of anything on Delta.
