# Hardware Safety

<p class="gr-meta">Maintainers: Era Shkembi, Tristan Elizalde · Last reviewed: [TEAM VERIFICATION REQUIRED]</p>

Read this before powering anything.

## Hazards

| Hazard | When | How to avoid it |
|---|---|---|
| Pinched fingers | Any time the follower is powered | Keep hands out of its reach while it's running. Use slow motions for first tests |
| Sudden motion | Starting teleop, running a policy, right after calibration | Clear the workspace. One person stands ready to cut power |
| Wrong supply voltage | Connecting power | Measure first. Labeled supplies ([Power](power.md)) |
| Servo overheating | Long sessions, stalled joints | Don't let the arm push against obstacles. Power down if a servo gets hot |
| Arm tipping | Fast motions | Clamp the base |
| Objects thrown or knocked over | Policy runs | Use only light, unbreakable test objects |

## Emergency stop

`[TEAM VERIFICATION REQUIRED: our stop procedure, e.g. unplug the follower supply, then stop the script]`

## Rules

1. Nobody runs a **new checkpoint** alone.
2. Power down the follower when it's not in use.
3. Never leave a powered arm unattended.
4. [TEAM VERIFICATION REQUIRED: any lab rules]
