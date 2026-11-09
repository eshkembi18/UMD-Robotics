# Troubleshooting

<p class="gr-meta">Maintainer: whole team</p>

Every problem we hit, and how we fixed it (or didn't). **Searching is the fastest way in:** press ++slash++ and type the error message or the symptom.

**Rule:** if you spent more than about 30 minutes on a problem, it goes here. If someone fixed something in the team chat, turn it into an entry that week.

## Categories

| Category | Covers |
|---|---|
| [Mechanical](mechanical.md) | Printed parts, joints, fasteners, cable routing |
| [Electrical](electrical.md) | Power supplies, voltage, connectors, boards |
| [Servo Communication](servo-communication.md) | Ports, IDs, servos not responding |
| [Calibration](calibration.md) | Calibration failing, joints off or reversed |
| [LeRobot Software](lerobot-software.md) | Install, versions, imports, config errors |
| [Teleoperation](teleoperation.md) | Lag, jitter, wrong arm moving, tracking errors |
| [Dataset Collection](dataset-collection.md) | Cameras, recording, upload, corrupted episodes |
| [Model Training](model-training.md) | Loss not decreasing, crashes, config errors |
| [GPU Cluster](gpu-cluster.md) | NCSA Delta access, jobs, storage, environment |
| [Deployment](deployment.md) | Policy runs, checkpoint loading, robot behavior |

## Adding an entry

Add it to the matching category page, using the format shown there. For a long investigation, give it its own page:

```bash
python scripts/new_entry.py troubleshooting "servo not detected"
```

## Not sure which layer it is?

Work from the bottom up: **mechanical → electrical → servo communication → calibration → LeRobot software → your code.** Most "software" problems on a new setup turn out to be a cable, a port, or a power supply.
