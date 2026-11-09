# Robot Configuration

<p class="gr-meta">Maintainers: Adam Hammoud, Karim Joumaa · Last verified: [TEAM VERIFICATION REQUIRED] · LeRobot: [TEAM VERIFICATION REQUIRED]</p>

Everything that's specific to **our** physical setup lives in config, not hardcoded in scripts.

## What goes in config

| Setting | Our value | Changes when… |
|---|---|---|
| Follower port | Machine-specific, see [Quickstart 5](../quickstart/05-leader-follower.md) | You switch laptop or replug |
| Leader port | Machine-specific | Same |
| Follower ID / name | [TEAM VERIFICATION REQUIRED] | Never. Calibration files are tied to it |
| Leader ID / name | [TEAM VERIFICATION REQUIRED] | Never |
| Cameras (name, index/path, resolution, fps) | [TEAM VERIFICATION REQUIRED] | You move or swap cameras |
| Calibration directory | [TEAM VERIFICATION REQUIRED] | — |

## Our config

```yaml
# [INSERT VERIFIED CONFIG]
# Paste our real config here with ports replaced by placeholders like <FOLLOWER_PORT>.
# Use the format our pinned LeRobot version actually accepts (CLI flags or config file).
```

## Where it lives

[TEAM VERIFICATION REQUIRED]: path in the code repo

## Rules

- Ports are written as placeholders in shared files. Each person sets their own locally.
- Don't change the robot IDs after calibrating, or LeRobot won't find the calibration.
