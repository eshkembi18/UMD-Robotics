# Power Distribution

<p class="gr-meta">Maintainers: Era Shkembi, Tristan Elizalde · Last verified: [TEAM VERIFICATION REQUIRED]</p>

!!! danger "Leader and follower power are not interchangeable"
    The follower uses **12V STS3215** servos. Before connecting any supply to any arm, confirm its voltage matches that arm's servos. Over-voltage can damage servos.

## Supplies

| Arm | Supply model | Rated output | Measured voltage | Current rating | Connector |
|---|---|---|---|---|---|
| Follower | [TEAM VERIFICATION REQUIRED] | 12V | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] |
| Leader | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] |

## Current budget

Make sure each supply can handle all the servos on its arm moving under load. Use datasheet values and say where they came from:

| Arm | Servos | Per-servo current (source) | Worst-case total | Supply rating | OK? |
|---|---|---|---|---|---|
| Follower | [TEAM VERIFICATION REQUIRED] | | | | |
| Leader | [TEAM VERIFICATION REQUIRED] | | | | |

## Power-on order

1. [TEAM VERIFICATION REQUIRED: e.g. supply → board, then USB]

## Labeling

- [ ] Each supply labeled with its arm and voltage
- [ ] Barrel / terminal connectors can't be swapped by accident 

Power check procedure: [Quickstart step 4](../quickstart/04-wiring-power.md).
