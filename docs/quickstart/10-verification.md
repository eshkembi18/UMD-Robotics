# 10. Verification Checklist

<p class="gr-meta">Maintainer: whole team · Last full run-through: [TEAM VERIFICATION REQUIRED]</p>

Run through this when a new person sets up the system, after hardware changes, and before every demo. If every box is checked, the setup is reproducible.

## Hardware

- [ ] Both arms assembled, all joints move freely unpowered ([step 2](02-assembly.md))
- [ ] Every servo has its documented ID and a physical label ([step 3](03-servo-ids.md))
- [ ] Supply voltage measured and matches each arm's servos ([step 4](04-wiring-power.md))
- [ ] Leader and follower ports, names, and cables labeled ([step 5](05-leader-follower.md))
- [ ] All IDs respond on each bus

## Software

- [ ] LeRobot installed at the pinned version ([step 6](06-software-install.md))
- [ ] Calibration files exist for both arms and are backed up ([step 7](07-calibration.md))

## System

- [ ] Teleop: follower tracks leader on every joint ([step 8](08-teleoperation.md))
- [ ] Cameras detected
- [ ] A test dataset records and replays correctly ([step 9](09-first-recording.md))

## Sign-off

| Date | Who | LeRobot version | Result | Notes |
|---|---|---|---|---|
| [TEAM VERIFICATION REQUIRED] | | | | |

When everything passes, update the **Last verified** date on each step page.
