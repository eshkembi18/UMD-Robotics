# 7. Calibration

<p class="gr-meta">Maintainers: Era Shkembi, Tristan Elizalde, Adam Hammoud, Karim Joumaa · Last verified: [TEAM VERIFICATION REQUIRED] · LeRobot: [TEAM VERIFICATION REQUIRED]</p>

## Purpose

Map each servo's raw position to joint positions LeRobot understands, so the leader and follower agree on what "the same pose" means.

## Prerequisites

- Steps [3](03-servo-ids.md), [4](04-wiring-power.md), and [5](06-software-install.md) complete
- Arm base clamped down

## Safety

!!! warning
    The follower may move during or right after calibration. Keep hands clear, and keep the area around the arm free of objects.

## Procedure

1. Calibrate the **follower** arm.
    ```bash
    # [INSERT VERIFIED COMMAND]
    ```
    `[TEAM VERIFICATION REQUIRED: describe the poses the tool asks for, with photos]`
2. Calibrate the **leader** arm.
    ```bash
    # [INSERT VERIFIED COMMAND]
    ```
3. Note where the calibration files are saved, and back them up. `[TEAM VERIFICATION REQUIRED: path]`

[ADD REAL PHOTO]: each pose the calibration asks for.

## Expected result

Calibration completes for both arms and writes a calibration file for each.

## Verification

Move one leader joint at a time during [step 8](08-teleoperation.md). The matching follower joint should move in the same direction by about the same amount.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Follower joint moves the opposite way | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] |

**Last verified:** [TEAM VERIFICATION REQUIRED]
