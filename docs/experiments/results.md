# Results Summary

<p class="gr-meta">Maintainer: whole team · Only recorded data appears here</p>

This page rolls up results from individual [experiment pages](index.md). Every number must link back to the experiment that produced it.

## Success rates

| Experiment | Task | Checkpoint | Successes / trials | Success rate |
|---|---|---|---|---|
| — | — | — | [RESULTS PENDING] | — |

## Training runs

| Experiment | GPU type | Runtime | Dataset episodes |
|---|---|---|---|
| — | — | [RESULTS PENDING] | — |

## Failure breakdown

| Experiment | Missed grasp | Dropped | Wrong target | Collision | Stalled | Safety stop | Other |
|---|---|---|---|---|---|---|---|
| — | | | | | | | |

## Charts

Once there are at least two experiments to compare, add a chart. Mermaid bar charts work without any extra tools. Copy this, fill in **real** values, and change the fence from `text` to `mermaid`:

```text
xychart-beta
    title "Success rate by checkpoint"
    x-axis ["EXP-001", "EXP-002"]
    y-axis "Success rate (%)" 0 --> 100
    bar [0, 0]
```
