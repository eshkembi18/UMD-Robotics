# 3. Servo ID Assignment

<p class="gr-meta">Maintainers: Era Shkembi, Tristan Elizalde · Last verified: [TEAM VERIFICATION REQUIRED] · LeRobot: [TEAM VERIFICATION REQUIRED: version/commit]</p>

## Purpose

Give every servo on a bus a unique ID so the controller can address each joint separately.

!!! note "Why this step exists"
    New servos usually come with the **same factory ID**, so if you chain them together before configuring them, the controller can't tell them apart. That's why servos get configured one at a time.

## Prerequisites

- LeRobot installed (do [step 6](06-software-install.md) first if you haven't)
- Controller board connected over USB, with its power supply

## Safety

!!! warning
    Only connect one servo to the board when you're setting its ID, unless the official procedure says otherwise for your LeRobot version.

## Procedure

1. Find the controller's USB port.
    ```bash
    # [INSERT VERIFIED COMMAND]
    # See the "find port" step in the LeRobot SO-101 guide for your pinned version.
    ```
2. Run the motor setup for the **follower** arm and follow the prompts, connecting one servo at a time.
    ```bash
    # [INSERT VERIFIED COMMAND]
    ```
3. Repeat for the **leader** arm.
    ```bash
    # [INSERT VERIFIED COMMAND]
    ```

## Our ID map

| Joint | Follower ID | Leader ID |
|---|---|---|
| [TEAM VERIFICATION REQUIRED: joint names as LeRobot uses them] | | |

Put a matching label on each physical servo.

## Expected result

The setup tool confirms each ID as it's written. `[TEAM VERIFICATION REQUIRED: paste real output]`

## Verification

With all servos on the bus, every expected ID responds. `[INSERT VERIFIED COMMAND]`

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Port not found | Charge-only USB cable, or a missing driver / permissions on Linux | Use a data cable. `[TEAM VERIFICATION REQUIRED: our fix]` |
| [TEAM VERIFICATION REQUIRED] | | |

**Last verified:** [TEAM VERIFICATION REQUIRED]
