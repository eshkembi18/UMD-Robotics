# Software Testing & Debugging

<p class="gr-meta">Maintainers: Adam Hammoud, Karim Joumaa · Last verified: [TEAM VERIFICATION REQUIRED] · LeRobot: [TEAM VERIFICATION REQUIRED]</p>

## Quick health checks

| Check | Command | Expected |
|---|---|---|
| LeRobot version | [INSERT VERIFIED COMMAND] | Matches the pinned version |
| Ports present | [INSERT VERIFIED COMMAND] | Both arms listed |
| All servos respond | [INSERT VERIFIED COMMAND] | Every ID answers |
| Cameras open | [INSERT VERIFIED COMMAND] | Each camera returns frames |

## Debugging approach

1. **Isolate the layer:** is it hardware, communication, LeRobot config, or our code? Work up from the bottom ([Hardware Communication](hardware-communication.md)).
2. **Reproduce it with the smallest thing possible**, e.g. one servo or one camera.
3. **Read the full traceback.** Search the [troubleshooting KB](../troubleshooting/index.md) and LeRobot's GitHub issues for the error text.
4. **Write it up** once it's solved.

## Logs

[TEAM VERIFICATION REQUIRED]: where LeRobot / our scripts write logs, and how to turn on verbose output

## Tests in the code repo

[TEAM VERIFICATION REQUIRED]: any automated tests we have and how to run them
