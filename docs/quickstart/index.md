# Quickstart: Zero to Moving Arm

<p class="gr-meta">Maintainers: Era Shkembi, Tristan Elizalde (steps 1–5) · Adam Hammoud, Karim Joumaa (steps 6–9) · Last verified: [TEAM VERIFICATION REQUIRED]</p>

This is the most important part of the site. An incoming student with the printed parts, servos, and a laptop should be able to follow these pages in order and end with a working leader–follower SO-101 setup, without having to ask us.

!!! info "Primary references"
    We follow the [XLeRobot documentation](https://xlerobot.readthedocs.io/) as our main build guide, together with the official [LeRobot SO-101 guide](https://huggingface.co/docs/lerobot/so101). When our steps and theirs differ, these pages say why. When they get updated upstream, check the version notes on each page.

## Steps

| # | Step | Owner | Status |
|---|---|---|---|
| 1 | [Prerequisites & tools](01-prerequisites.md) | Hardware | <span class="status progress">In progress</span> |
| 2 | [Hardware assembly](02-assembly.md) | Hardware | <span class="status progress">In progress</span> |
| 3 | [Servo ID assignment](03-servo-ids.md) | Hardware | <span class="status planned">Planned</span> `[TEAM VERIFICATION REQUIRED]` |
| 4 | [Wiring & power check](04-wiring-power.md) | Hardware | <span class="status planned">Planned</span> `[TEAM VERIFICATION REQUIRED]` |
| 5 | [Leader–follower configuration](05-leader-follower.md) | Hardware | <span class="status planned">Planned</span> |
| 6 | [Software install](06-software-install.md) | Software | <span class="status planned">Planned</span> `[TEAM VERIFICATION REQUIRED]` |
| 7 | [Calibration](07-calibration.md) | Hardware + Software | <span class="status planned">Planned</span> |
| 8 | [First teleoperation](08-teleoperation.md) | Software | <span class="status planned">Planned</span> |
| 9 | [First dataset recording](09-first-recording.md) | Software | <span class="status planned">Planned</span> |
| 10 | [Verification checklist](10-verification.md) | Whole team | <span class="status planned">Planned</span> |

!!! note "Order"
    Step 6 (software) is needed to find ports and set servo IDs, so many people install it right after step 1. That's fine. The numbering follows the hardware build order.

!!! tip "Keeping this honest"
    A step only becomes <span class="status done">Implemented</span> once someone has run it start to finish on our hardware and written the date in its **Last verified** line. If you follow a step and it doesn't work, fix the page or add a [troubleshooting entry](../troubleshooting/index.md). Don't leave it broken for the next person.

## Page format

Every step page uses the same sections, so you always know where to look:

**Purpose** · **Prerequisites** · **Safety** · **Procedure** · **Expected result** · **Verification** · **Troubleshooting** · **Last verified**

To write a new one, copy the [procedure template](../page-templates/procedure.md).
