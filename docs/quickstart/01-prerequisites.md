# 1. Prerequisites & Tools

<p class="gr-meta">Maintainers: Era Shkembi, Tristan Elizalde · Last verified: [TEAM VERIFICATION REQUIRED]</p>

## Purpose

Get everything you need on the table before you start, so you don't stop halfway through assembly.

## Hardware

| Item | Qty | Notes |
|---|---|---|
| Printed SO-101 parts (leader + follower sets) | [TEAM VERIFICATION REQUIRED] | We printed our own. Print files and settings: [3D-Printed Components](../hardware/printed-parts.md) |
| STS3215 servos for the follower arm (12V version) | [TEAM VERIFICATION REQUIRED] | See [Servo Configuration](../hardware/servos.md) |
| Servos for the leader arm | [TEAM VERIFICATION REQUIRED] | The leader configuration is different from the follower. Check the official BOM |
| Servo controller / bus boards | [TEAM VERIFICATION REQUIRED] | One per arm |
| Power supplies | [TEAM VERIFICATION REQUIRED] | Voltage must match the servos on that arm |
| USB cables | [TEAM VERIFICATION REQUIRED] | Data-capable, not charge-only |
| Cameras | [TEAM VERIFICATION REQUIRED] | Needed from step 9 onward |
| Screws / hardware kit | [TEAM VERIFICATION REQUIRED] | |

The full costed list is in the [Bill of Materials](../hardware/bom.md).

## Tools

- [ ] Screwdrivers matching the screw kit `[TEAM VERIFICATION REQUIRED: sizes]`
- [ ] Multimeter (for the power check in step 4)
- [ ] Clamps or a way to fix the arm base to the table
- [ ] Labels / tape to mark servo IDs and leader vs follower parts

## Software & accounts

- [ ] A laptop with Linux, macOS, or Windows `[TEAM VERIFICATION REQUIRED: which OS has actually worked for us]`
- [ ] Python environment manager `[TEAM VERIFICATION REQUIRED: conda / uv / venv, whichever we standardize on]`
- [ ] GitHub access to the project repo
- [ ] Hugging Face account (for datasets and models), added to the project org
- [ ] NCSA Delta access, only needed for training. See the [Delta guide](../delta/index.md)

## Safety

!!! warning
    You'll be working with powered servos that can move suddenly and pinch fingers. Read [Hardware Safety](../hardware/safety.md) before you power anything.

## Verification

You're ready when every box above is checked and every part is labeled leader or follower.

**Last verified:** [TEAM VERIFICATION REQUIRED]
