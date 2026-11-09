# Experiment Report Template

Fields marked *(optional)* can be deleted if they don't apply. Never fill a results field with an estimate. Use `[RESULTS PENDING]` until real data exists.

````markdown
# EXP-000: Short title

<p class="gr-meta">Owner: Name · Date run: YYYY-MM-DD · Status: <span class="status planned">Planned</span></p>

## Question & goal

- **Research question:** What are we trying to find out?
- **Objective:** What we'll do.
- **Hypothesis** *(optional)*: What we expect, and why.
- **Success criteria:** Decided **before** running. E.g. "success = object ends inside target zone".

## Setup

| Item | Value |
|---|---|
| Hardware config | e.g. follower arm, 12V STS3215, camera positions |
| Code commit | |
| LeRobot version | |
| Dataset ID + revision | |
| Training config | link to config / command |
| Checkpoint | Hugging Face link |
| Test environment | table, lighting, objects |

## Evaluation protocol

How each trial is run and judged, so someone else can repeat it exactly.

## Results

[RESULTS PENDING]

| Metric | Value |
|---|---|
| Successful trials | |
| Total trials | |
| **Success rate** (successful ÷ total × 100) | |
| Mean execution time *(optional)* | |
| Inference latency *(optional, if measured)* | |
| Training runtime *(optional)* | |

### Failure breakdown *(optional)*

| Failure type | Count |
|---|---|
| | |

## Video

[ADD REAL VIDEO]

## Analysis

What happened and why we think so. Label guesses as guesses.

## Conclusions & next steps

-
````
