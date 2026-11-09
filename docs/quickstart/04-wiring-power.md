# 4. Wiring & Power Check

<p class="gr-meta">Maintainers: Era Shkembi, Tristan Elizalde · Last verified: [TEAM VERIFICATION REQUIRED]</p>

## Purpose

Wire each arm's servo chain to its controller and confirm the power is correct **before** anything moves.

## Prerequisites

- Arms assembled ([step 2](02-assembly.md)), servo IDs set ([step 3](03-servo-ids.md))
- Multimeter

## Safety

!!! danger "Leader and follower power are not interchangeable"
    Our follower arm uses the **12V STS3215** servos. The leader arm uses a different configuration. Before connecting a supply, check that its voltage matches the servos on **that** arm. A higher-voltage supply on lower-rated servos can damage them. `[TEAM VERIFICATION REQUIRED: write the exact supply each arm uses]`

## Procedure

1. Daisy-chain the servos on each arm and route the cables as in [Wiring Diagrams](../hardware/wiring.md).
2. With the supply **unplugged from the board**, measure its output with the multimeter. Write it down.
3. Check polarity at the board's power input. `[TEAM VERIFICATION REQUIRED: board model and which terminal is which]`
4. Connect power, then USB.

[ADD REAL DIAGRAM]: annotated wiring photo for each arm.

## Expected result

| Check | Follower | Leader |
|---|---|---|
| Supply measured voltage | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] |
| Board power LED on | ☐ | ☐ |
| No heat or smell after 1 minute idle | ☐ | ☐ |

## Verification

All servo IDs respond on the bus (same check as step 3) with everything wired.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Some servos don't respond once chained | Loose connector partway down the chain, or duplicate IDs | Check each connector. Re-check IDs |
| [TEAM VERIFICATION REQUIRED] | | |

**Last verified:** [TEAM VERIFICATION REQUIRED]
