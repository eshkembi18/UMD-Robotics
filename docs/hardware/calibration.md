# Calibration

<p class="gr-meta">Maintainers: Era Shkembi, Tristan Elizalde · Last verified: [TEAM VERIFICATION REQUIRED]</p>

The procedure is in [Quickstart step 7](../quickstart/07-calibration.md). This page explains what calibration does and how to manage it.

## What calibration does

Each servo reports a raw position. Calibration records the raw values at known reference poses and joint limits, so LeRobot can turn raw readings into consistent joint positions. The leader and follower are calibrated separately, so that "the same pose" means the same thing on both.

## Calibration files

| Arm | File location | Backed up where |
|---|---|---|
| Follower | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] |
| Leader | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] |

!!! warning
    Policies are trained on data recorded with a specific calibration. Recalibrating the follower can change how a trained policy behaves. Note the date of every recalibration in the [maintenance log](maintenance.md#maintenance-log).

## When to recalibrate

- After replacing a servo or reassembling a joint
- When teleop tracking is visibly off
- [TEAM VERIFICATION REQUIRED: anything else we found]

[ADD REAL PHOTO]: each calibration pose.
