# Python Environment Setup

<p class="gr-meta">Maintainers: Adam Hammoud, Karim Joumaa · Last verified: [TEAM VERIFICATION REQUIRED] · LeRobot: [TEAM VERIFICATION REQUIRED]</p>

First-time install is in [Quickstart step 6](../quickstart/06-software-install.md). This page covers how our environments are organized.

## Two environments, one version

| | Robot laptop | NCSA Delta |
|---|---|---|
| Purpose | Control, teleop, recording, inference | Training |
| OS | [TEAM VERIFICATION REQUIRED] | Delta's Linux. See [Delta: Environment](../delta/environment.md) |
| Python | [TEAM VERIFICATION REQUIRED] | **Same as the laptop** |
| LeRobot | [TEAM VERIFICATION REQUIRED] | **Same as the laptop** |
| Env manager | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] |

!!! warning "Keep them matched"
    Train and deploy with the same LeRobot version. A checkpoint trained with one version may not load, or may behave differently, under another.

## Creating the environment

```bash
# [INSERT VERIFIED COMMAND]: create env with the pinned Python
# [INSERT VERIFIED COMMAND]: activate it
# [INSERT VERIFIED COMMAND]: install from our lock/requirements file
```

## Rules

- One environment per project, named `[TEAM VERIFICATION REQUIRED]`.
- Never `pip install` something new without adding it to the lock file. See [Dependency Management](dependencies.md).
- If your environment breaks, delete it and recreate it from the lock file instead of patching it.
