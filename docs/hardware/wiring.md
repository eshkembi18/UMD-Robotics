# Wiring Diagrams

<p class="gr-meta">Maintainers: Era Shkembi, Tristan Elizalde · Last verified: [TEAM VERIFICATION REQUIRED]</p>

## Overview

```mermaid
flowchart LR
    subgraph Follower
      PF[12V supply] --> BF[Controller board]
      BF --- S1F[Servo 1] --- S2F[Servo 2] --- S3F[...] --- S6F[Gripper servo]
    end
    subgraph Leader
      PL[Leader supply] --> BL[Controller board]
      BL --- S1L[Servo 1] --- S2L[Servo 2] --- S3L[...] --- S6L[Gripper servo]
    end
    BF -->|USB| PC[Laptop]
    BL -->|USB| PC
```

The chain order above is generic. Replace it with our real order once it's confirmed. `[TEAM VERIFICATION REQUIRED]`

## Follower arm

<div class="gr-placeholder">[ADD REAL DIAGRAM]<br/>Annotated photo: board model, power input and polarity, USB, servo chain order and IDs</div>

## Leader arm

<div class="gr-placeholder">[ADD REAL DIAGRAM]<br/>Same as above for the leader</div>

## Connector reference

| Connection | Connector type | Notes |
|---|---|---|
| Servo to servo | [TEAM VERIFICATION REQUIRED] | |
| Board power input | [TEAM VERIFICATION REQUIRED] | Polarity: [TEAM VERIFICATION REQUIRED] |
| Board to laptop | [TEAM VERIFICATION REQUIRED] | Must be a data-capable cable |

Store editable diagram source files in `docs/assets/diagrams/`.
