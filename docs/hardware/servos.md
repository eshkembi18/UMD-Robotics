# Servo Configuration

<p class="gr-meta">Maintainers: Era Shkembi, Tristan Elizalde · Last verified: [TEAM VERIFICATION REQUIRED]</p>

## Follower servos: Feetech STS3215, 12V version

Get these values from the manufacturer datasheet or the official SO-101 BOM, **not from memory**, and link the source next to each one.

| Property | Value | Source |
|---|---|---|
| Rated voltage | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED: datasheet link] |
| Gear ratio | [TEAM VERIFICATION REQUIRED] | |
| Stall torque | [TEAM VERIFICATION REQUIRED] | |
| Stall current | [TEAM VERIFICATION REQUIRED] | |
| Position sensor resolution | [TEAM VERIFICATION REQUIRED] | |
| Interface | Serial bus, daisy-chained | [TEAM VERIFICATION REQUIRED: link] |
| Baud rate used | [TEAM VERIFICATION REQUIRED] | Set during LeRobot motor setup |

## Leader servos

| Joint | Model / variant | Rated voltage | Source |
|---|---|---|---|
| [TEAM VERIFICATION REQUIRED] | | | |

## ID map

| Joint | Follower ID | Leader ID |
|---|---|---|
| [TEAM VERIFICATION REQUIRED: joint names as LeRobot uses them] | | |

How to set IDs: [Quickstart step 3](../quickstart/03-servo-ids.md).

## Settings we changed

Anything we changed beyond what LeRobot's setup writes (limits, PID, torque), and why:

| Setting | Joint(s) | Value | Why |
|---|---|---|---|
| [TEAM VERIFICATION REQUIRED, or "none"] | | | |

## Identifying a servo

New servos usually come with the same factory ID, so a replacement must be set up on its own before it joins the chain. See [Maintenance & Replacement](maintenance.md).
