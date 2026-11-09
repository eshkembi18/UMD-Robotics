# ADR-002: NCSA Delta for GPU Training

<p class="gr-meta">Date: [TEAM VERIFICATION REQUIRED] · Status: Accepted · Deciders: whole team</p>

## Problem

Training (or fine-tuning) manipulation policies needs more GPU than our laptops have.

## Options considered

| Option | Pros | Cons |
|---|---|---|
| NCSA Delta | [TEAM VERIFICATION REQUIRED] | Queue waits, cluster learning curve, allocation tied to specific people |
| Local / lab GPU | [TEAM VERIFICATION REQUIRED] | [TEAM VERIFICATION REQUIRED] |
| Cloud GPU (paid) | Fast to start | Costs money |

## Decision

Deploy and train our pretrained model on NCSA Delta, on a shared instance.

## Rationale

[TEAM VERIFICATION REQUIRED]

## Tradeoffs & consequences

- Access has to be transferred deliberately at handoff. See the [access checklist](../handoff/access-transfer.md).
- Site settings change. The [Delta guide](../delta/index.md) has to be re-verified each semester.

## Evidence

[TEAM VERIFICATION REQUIRED]
