# 9. First Dataset Recording

<p class="gr-meta">Maintainers: Adam Hammoud, Karim Joumaa · Last verified: [TEAM VERIFICATION REQUIRED] · LeRobot: [TEAM VERIFICATION REQUIRED]</p>

## Purpose

Record a small test dataset of teleoperated demos with camera data, and confirm it saved correctly. The point here is checking the pipeline, not getting a good dataset.

## Prerequisites

- [Teleoperation](08-teleoperation.md) working
- Cameras connected and mounted `[TEAM VERIFICATION REQUIRED: camera models and placement]`
- Hugging Face login if you're pushing to the Hub `[TEAM VERIFICATION REQUIRED: do we push, or keep it local first?]`

## Safety

Same as [teleoperation](08-teleoperation.md). Clear the workspace of anything that isn't part of the task.

## Procedure

1. Check that each camera is detected.
    ```bash
    # [INSERT VERIFIED COMMAND]
    ```
2. Record a few short episodes of a simple task. `[TEAM VERIFICATION REQUIRED: which task]`
    ```bash
    # [INSERT VERIFIED COMMAND]
    ```
3. Replay or visualize the dataset to check it.
    ```bash
    # [INSERT VERIFIED COMMAND]
    ```

!!! tip "Never put secrets in commands you paste here"
    If a command needs a Hugging Face token, write `$HF_TOKEN` or say "log in with the Hugging Face CLI". Never paste the token itself.

## Expected result

A dataset with the number of episodes you recorded, with joint data and video for each camera. `[TEAM VERIFICATION REQUIRED: where it's stored]`

## Verification

The replay or visualization shows the motions you performed, and the camera frames line up with them.

Dataset conventions (naming, storage, structure): [Dataset Collection](../software/dataset-collection.md).

**Last verified:** [TEAM VERIFICATION REQUIRED]
