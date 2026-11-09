# 5. Leader–Follower Configuration

<p class="gr-meta">Maintainers: Era Shkembi, Tristan Elizalde · Last verified: [TEAM VERIFICATION REQUIRED]</p>

## Purpose

Set up the two arms as a pair: know which USB port is which arm, give each arm a stable identity in software, and make sure nobody can mix them up later.

## Prerequisites

- Both arms wired and power-checked ([step 4](04-wiring-power.md))
- LeRobot installed ([step 6](06-software-install.md)). You'll need it to find the ports

## Safety

!!! warning
    Mixing up the leader and follower configs means the wrong arm gets driven. Label everything physically **and** in software before step 7.

## Procedure

1. Plug in **only the follower** controller. Find its port.
    ```bash
    # [INSERT VERIFIED COMMAND]: LeRobot's "find port" utility for our pinned version
    ```
    Write it down: follower port = `[TEAM VERIFICATION REQUIRED]`
2. Unplug it, plug in **only the leader**, and repeat. Leader port = `[TEAM VERIFICATION REQUIRED]`
3. Choose an ID / name for each arm in LeRobot's config. Calibration files are saved under these names, so keep them the same forever. `[TEAM VERIFICATION REQUIRED: our names, e.g. follower_main / leader_main]`
4. Put the ports and names in the robot config. See [Robot Configuration](../software/robot-config.md).
5. Label the physical USB cables "LEADER" and "FOLLOWER".

!!! tip "Ports change"
    Port names can change when you replug, reboot, or switch laptops. If teleop suddenly drives the wrong arm or can't connect, re-run steps 1–2 first. `[TEAM VERIFICATION REQUIRED: if we set up stable device names (e.g. udev rules on Linux), document it here]`

## Expected result

| Arm | Port | Software ID | Supply |
|---|---|---|---|
| Leader | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] |
| Follower | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] | 12V |

## Verification

- [ ] Each port responds only when its own arm is plugged in
- [ ] Cables and supplies are labeled
- [ ] The config file has the right port for each arm

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Port disappears after replugging | OS assigned a new name | Re-run the port finder |
| [TEAM VERIFICATION REQUIRED] | | |

**Last verified:** [TEAM VERIFICATION REQUIRED]
