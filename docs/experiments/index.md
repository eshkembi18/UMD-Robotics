# Experiments & Results

<p class="gr-meta">Maintainer: whole team</p>

Every experiment or training run worth talking about gets its own page from the [experiment template](../page-templates/experiment.md):

```bash
python scripts/new_entry.py experiment EXP-001 "short title"
```

!!! warning "Only real data"
    Results appear here only once they're recorded. No estimates, and no "it seemed to work". A capability becomes <span class="status validated">Validated</span> only when an experiment page backs it up.

## How we evaluate

All experiments follow the shared [Evaluation Protocol](protocol.md): success criteria written down beforehand, a fixed trial count, video of every trial, and failure categories.

**Success rate = successful trials ÷ total trials × 100**, always reported with the raw counts.

The roll-up of all results is on [Results Summary](results.md). Datasets and checkpoints are linked from the [dataset registry](../software/dataset-collection.md#dataset-registry) and the [checkpoint registry](../software/checkpoints.md#registry).

## Experiment registry

| ID | Title | Date | Dataset | Checkpoint | Success rate | Status |
|---|---|---|---|---|---|---|
| — | No experiments recorded yet | | | | | [RESULTS PENDING] |

