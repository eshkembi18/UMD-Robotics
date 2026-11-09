# Inference & Deployment

<p class="gr-meta">Maintainers: Adam Hammoud, Karim Joumaa · Last verified: [TEAM VERIFICATION REQUIRED] · LeRobot: [TEAM VERIFICATION REQUIRED]</p>

Running a trained policy on the follower arm.

!!! danger
    The first run of any new checkpoint is in a cleared workspace, at reduced speed if possible, with someone ready to cut power. See [Hardware Safety](../hardware/safety.md).

## Procedure

1. Download the checkpoint ([Checkpoints](checkpoints.md)).
2. Confirm the laptop's LeRobot version matches the one used for training.
3. Set up the scene exactly as in the training data (cameras, lighting, object positions).
4. Run:
    ```bash
    # [INSERT VERIFIED COMMAND]
    ```
5. Evaluate with the [evaluation protocol](../experiments/protocol.md).

## Where does inference run?

| Option | Notes |
|---|---|
| On the robot laptop | [TEAM VERIFICATION REQUIRED]: does it have a GPU? Is the loop rate OK? |
| Remote (e.g. on a GPU machine) | [TEAM VERIFICATION REQUIRED]: only if we set this up |

## Latency

| Metric | Value | How measured | Hardware |
|---|---|---|---|
| Policy inference time per step | [RESULTS PENDING] | | |
| Control loop rate during policy run | [RESULTS PENDING] | | |
