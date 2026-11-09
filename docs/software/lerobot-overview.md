# LeRobot Overview

<p class="gr-meta">Maintainers: Adam Hammoud, Karim Joumaa · Last verified: [TEAM VERIFICATION REQUIRED] · LeRobot: [TEAM VERIFICATION REQUIRED]</p>

[LeRobot](https://github.com/huggingface/lerobot) is Hugging Face's open-source robotics library. We use it for everything that touches the robot or the data:

| What we use it for | Where it's documented here |
|---|---|
| Motor setup and calibration for SO-101 | [Quickstart 3](../quickstart/03-servo-ids.md), [7](../quickstart/07-calibration.md) |
| Leader–follower teleoperation | [Teleoperation Workflow](teleoperation.md) |
| Recording datasets in the LeRobot dataset format | [Dataset Collection](dataset-collection.md), [Dataset Structure](dataset-structure.md) |
| Training policies | [Policy Training](policy-training.md) |
| Running policies on the robot | [Inference & Deployment](inference-deployment.md) |

## Version we're on

| | |
|---|---|
| Release / commit | [TEAM VERIFICATION REQUIRED] |
| Date pinned | [TEAM VERIFICATION REQUIRED] |
| Why this version | [TEAM VERIFICATION REQUIRED] |

!!! warning "LeRobot changes quickly"
    Command names, config options, and file locations have changed between LeRobot versions. Every command on this site is tied to the version above. Before upgrading, read the release notes, re-run the [Quickstart](../quickstart/index.md), and update this page.

## Official resources

- [LeRobot documentation](https://huggingface.co/docs/lerobot)
- [LeRobot GitHub](https://github.com/huggingface/lerobot)
- [SO-101 guide](https://huggingface.co/docs/lerobot/so101)
- [XLeRobot docs](https://xlerobot.readthedocs.io/), our main build guide

## Concepts worth knowing

| Term | Meaning |
|---|---|
| Robot | The follower arm (plus cameras) as LeRobot sees it |
| Teleoperator | The device a person controls it with, here the leader arm |
| Observation | What the robot senses at a time step: joint positions, camera frames |
| Action | The target joint positions sent to the follower |
| Episode | One recorded demonstration, start to finish |
| Policy | A model that maps observations to actions |

`[TEAM VERIFICATION REQUIRED]: check these terms against the docs for our pinned version`
