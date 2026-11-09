# 8. First Teleoperation

<p class="gr-meta">Maintainers: Adam Hammoud, Karim Joumaa · Last verified: [TEAM VERIFICATION REQUIRED] · LeRobot: [TEAM VERIFICATION REQUIRED]</p>

## Purpose

Move the leader arm by hand and have the follower copy it in real time. This is the first time the whole system works end to end.

## Prerequisites

- [Calibration](07-calibration.md) done for both arms
- Both controllers connected, ports known

## Safety

!!! danger
    Start with slow, small leader movements. Have one person ready to cut power to the follower. `[TEAM VERIFICATION REQUIRED: our emergency stop method]`

## Procedure

1. Start teleoperation.
    ```bash
    # [INSERT VERIFIED COMMAND]
    ```
2. Move each leader joint slowly, one at a time.
3. Then try a combined motion, like reaching forward and closing the gripper.
4. Stop teleoperation. `[TEAM VERIFICATION REQUIRED: how, e.g. Ctrl+C]`

[ADD REAL VIDEO]: a short clip of the first successful teleop.

## Expected result

The follower tracks the leader closely, with no jitter or lag you'd notice. `[TEAM VERIFICATION REQUIRED: describe what "good" looked like for us]`

## Verification

- [ ] Each joint tracks in the right direction
- [ ] Gripper opens and closes
- [ ] Follower holds a pose without drifting when the leader is still

## Troubleshooting

See [Teleoperation issues](../troubleshooting/teleoperation.md).

**Last verified:** [TEAM VERIFICATION REQUIRED]
