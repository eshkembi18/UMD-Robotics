---
hide:
  - navigation
  - toc
---

<div class="gr-hero" markdown>

# Generalist Robotics

<p class="gr-sub">SO-101 · Hugging Face LeRobot · NCSA Delta</p>

We're working toward a generalist manipulation pipeline on low-cost SO-101 robot arms: leader–follower teleoperation for collecting demonstrations, learned policies trained on GPU clusters, and real-world evaluation. This site documents how everything is built, what has actually worked, and what went wrong, so the next team can start where we stopped.

[Start the Quickstart :material-arrow-right:](quickstart/index.md){ .md-button .md-button--primary }
[Hardware](hardware/index.md){ .md-button }
[Software & ML](software/index.md){ .md-button }
[Handoff](handoff/index.md){ .md-button }

</div>

## Project status

| Item | Details |
|---|---|
| **Course** | Senior Design 1 (CIS) — University of Michigan–Dearborn |
| **Semester** | Fall 2026 |
| **Phase** | Robot arms only: get the SO-101 arms moving and doing simple tasks autonomously |
| **Status** | <span class="status progress">In progress</span> |
| **Project client** | Dr. Ang Li, UM-Dearborn CIS `[TEAM VERIFICATION REQUIRED: confirm title / role wording]` |
| **Team** | Era Shkembi · Tristan Elizalde · Adam Hammoud · Karim Joumaa ([roles](team/index.md)) |
| **Last site update** | 2026-11-07 |
| **Code** | [GitHub repository](https://github.com/eshkembi18/UMD-Robotics) `[TEAM VERIFICATION REQUIRED]` |

## Pipeline

Colors show where each stage stands. Update the `class` lines below as stages move.

```mermaid
flowchart LR
    A[Hardware setup] --> B[Teleoperation]
    B --> C[Dataset collection]
    C --> D[Model training<br/>NCSA Delta]
    D --> E[Policy deployment]
    E --> F[Evaluation]

    classDef done fill:#14532d,stroke:#22c55e,color:#f0fdf4
    classDef progress fill:#451a03,stroke:#f59e0b,color:#fffbeb
    classDef planned fill:#1e293b,stroke:#64748b,color:#cbd5e1

    class A progress
    class B,C,D,E,F planned
```

<span class="status done">Implemented</span> &nbsp; <span class="status progress">In progress</span> &nbsp; <span class="status planned">Planned</span> &nbsp; <span class="status validated">Validated with recorded results</span>

| Stage | Status | Where it's documented |
|---|---|---|
| Hardware setup (3D-printed SO-101, servos, wiring) | <span class="status progress">In progress</span> | [Hardware](hardware/index.md), [Quickstart 1–5](quickstart/index.md) |
| Teleoperation (leader → follower) | <span class="status planned">Planned</span> `[TEAM VERIFICATION REQUIRED]` | [Quickstart 8](quickstart/08-teleoperation.md) |
| Dataset collection | <span class="status planned">Planned</span> | [Dataset Collection](software/dataset-collection.md) |
| Model training on NCSA Delta | <span class="status planned">Planned</span> | [NCSA Delta guide](delta/index.md) |
| Policy deployment | <span class="status planned">Planned</span> | [Inference & Deployment](software/inference-deployment.md) |
| Evaluation | <span class="status planned">Planned</span> | [Experiments](experiments/index.md) |

## Demo

<div class="gr-placeholder">
[ADD REAL VIDEO]<br/>
Embed a short clip of the arm working once you have one.<br/>
Host it on YouTube (unlisted) or Hugging Face, not in git.
</div>

## Where to go

<div class="grid cards" markdown>

-   :material-rocket-launch: **[Quickstart](quickstart/index.md)**

    Parts on a table to a moving arm, step by step.

-   :material-cog: **[Hardware](hardware/index.md)**

    BOM, printing, leader vs follower, servos, wiring.

-   :material-brain: **[Software & ML](software/index.md)**

    Architecture, environment, data, training, deployment.

-   :material-server: **[NCSA Delta](delta/index.md)**

    Getting GPU training running on the cluster.

-   :material-flask: **[Experiments](experiments/index.md)**

    What we tested, how, and the recorded results.

-   :material-wrench: **[Troubleshooting](troubleshooting/index.md)**

    Symptom → cause → fix for every problem we hit.

-   :material-scale-balance: **[Decision Log](decisions/index.md)**

    Why we chose what we chose.

-   :material-account-switch: **[Handoff](handoff/index.md)**

    For next semester's team: what works, what's next, who has access.

</div>
