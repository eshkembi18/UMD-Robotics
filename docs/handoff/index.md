# Handoff for Future Teams

<p class="gr-meta">Maintainer: whole team · Last updated: [TEAM VERIFICATION REQUIRED] · Update before the end of every semester</p>

If you're the next team: welcome. This section is everything we wish we'd known on day one.

## Start here

1. Read [Current State](current-state.md) to see what works and what doesn't.
2. Work through [Access Transfer](access-transfer.md) with the outgoing team **before they graduate**.
3. Get your own setup running with [Reproducing the Setup](reproduce.md).
4. Check [Inventory & Locations](inventory.md) for hardware, datasets, and models.
5. Plan your semester with [Next Steps](next-steps.md).

## One-paragraph summary

`[TEAM VERIFICATION REQUIRED]: 3–4 sentences at the end of the semester. What we built, where it stands, and the single most important thing to do next.`

## Architecture in one picture

```mermaid
flowchart LR
    subgraph Laptop[Robot laptop]
      LR[LeRobot] --- CFG[Robot config +<br/>calibration]
    end
    L[Leader arm] --> LR
    LR --> F[Follower arm<br/>12V STS3215]
    CAM[Cameras] --> LR
    LR -->|record| HF[(Hugging Face Hub<br/>datasets + checkpoints)]
    HF -->|train| D[NCSA Delta]
    D -->|checkpoint| HF
    HF -->|deploy| LR
```

Details: [Hardware](../hardware/index.md) · [Software & ML](../software/index.md) · [NCSA Delta](../delta/index.md)
