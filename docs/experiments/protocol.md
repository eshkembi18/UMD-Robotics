# Evaluation Protocol

<p class="gr-meta">Maintainer: whole team · Last reviewed: [TEAM VERIFICATION REQUIRED]</p>

The shared rules for running any evaluation, so results from different weeks and different people can be compared.

## Before the trials

1. Write down the **success criteria** on the experiment page **before** running anything.
2. Fix the number of trials in advance. Don't stop early because it's going well or badly. `[TEAM VERIFICATION REQUIRED: our default trial count]`
3. Set up the scene to match the training data: camera positions, lighting, table surface, objects.
4. Record the checkpoint, the LeRobot version, and the calibration date.

## During the trials

- Use the same object start positions for every checkpoint you compare. `[TEAM VERIFICATION REQUIRED: how we define and mark them]`
- Record every trial on video, including failures.
- Mark each trial as success or failure immediately, using the pre-written criteria.
- If you intervene for safety, the trial counts as a failure. Note why.

## Scoring

**Success rate = successful trials ÷ total trials × 100**

Report it alongside the raw counts, e.g. "7 / 10 (70%)", never as a percentage alone. With small trial counts, small differences between checkpoints may be noise.

## Failure categories

Tag each failure with one category, so patterns show up:

| Category | Meaning |
|---|---|
| Missed grasp | Gripper closed, but not on the object |
| Dropped | Grasped, then lost the object |
| Wrong target | Moved to the wrong place |
| Collision | Hit something it shouldn't have |
| Frozen / stalled | Stopped making progress |
| Safety stop | A person intervened |
| Other | Describe it |

Adjust these once real failures show different patterns. `[TEAM VERIFICATION REQUIRED]`
