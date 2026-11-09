# Software & ML Architecture

<p class="gr-meta">Maintainers: Adam Hammoud, Karim Joumaa · Last verified: [TEAM VERIFICATION REQUIRED] · LeRobot: [TEAM VERIFICATION REQUIRED]</p>

## Overview

All robot control, data collection, training, and policy execution goes through [Hugging Face LeRobot](https://github.com/huggingface/lerobot). The system runs in two very different modes, and it helps to keep them separate in your head:

=== "Real-time control (on the laptop)"

    ```mermaid
    flowchart TB
        OP((Operator / task)) --> SRC{Command source}
        SRC -->|teleop| LEAD[Leader arm]
        SRC -->|autonomous| POL[Trained policy]
        LEAD -->|joint positions| LR[LeRobot control loop]
        POL -->|actions| LR
        LR -->|position commands| FOL[Follower arm]
        FOL --> ENV[Physical environment]
        CAM[Cameras] -->|frames| LR
        FOL -->|joint state| LR
        LR -->|observations| POL
    ```

    Runs on the laptop connected to the arms. It's latency-sensitive: every loop it reads state and camera frames, gets an action (from the leader or a policy), and sends it to the follower.

=== "Training (offline, on NCSA Delta)"

    ```mermaid
    flowchart LR
        REC[Recorded episodes<br/>joint state + video + actions] --> DS[(LeRobot dataset<br/>Hugging Face Hub)]
        DS --> PRE[Loading / preprocessing]
        PRE --> TR[Policy training<br/>GPU, NCSA Delta]
        TR --> CK[(Checkpoint<br/>Hugging Face Hub)]
        CK -.->|download| POL2[Policy on laptop]
    ```

    Runs on the cluster. It isn't time-critical: it reads a fixed dataset and writes checkpoints. Nothing here touches the robot.

## Components

| Component | What it does | Data in | Data out | Status |
|---|---|---|---|---|
| Leader arm + LeRobot | Reads the human's motion | Servo positions | Target joint positions | <span class="status planned">Planned</span> |
| Follower arm + LeRobot | Executes motion | Target positions | Joint state | <span class="status planned">Planned</span> |
| Cameras | Visual observations | — | Frames | <span class="status planned">Planned</span> |
| Recorder | Saves demos | State, frames, actions | LeRobot dataset | <span class="status planned">Planned</span> |
| Training | Learns a policy | Dataset | Checkpoint | <span class="status planned">Planned</span> |
| Policy inference | Runs the learned policy | Observations | Actions | <span class="status planned">Planned</span> |

`[TEAM VERIFICATION REQUIRED: update the statuses as each one actually works]`

## Which policy?

`[TEAM VERIFICATION REQUIRED: which policy architecture(s) we're training or deploying, e.g. a pretrained foundation model vs training from scratch. Record the choice in the decision log.]`

## Pages in this section

| Area | Pages |
|---|---|
| Foundations | [LeRobot Overview](lerobot-overview.md) · [Python Environment](python-environment.md) · [Dependency Management](dependencies.md) |
| Talking to the robot | [Robot Configuration](robot-config.md) · [Communication with Hardware](hardware-communication.md) · [Teleoperation Workflow](teleoperation.md) |
| Data | [Dataset Collection](dataset-collection.md) · [Dataset Structure](dataset-structure.md) · [Data Preprocessing](preprocessing.md) |
| Learning | [Policy Training](policy-training.md) · [Checkpoint Management](checkpoints.md) · [Inference & Deployment](inference-deployment.md) |
| Quality | [Testing & Debugging](testing-debugging.md) |

GPU training on the cluster: [NCSA Delta guide](../delta/index.md).
