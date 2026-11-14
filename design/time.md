# Time System

- A global **timescale** affects movement, DoT ticks, timers, distance-based stats and cinematic cutscenes.
- **Only player heroes have time powers.** Enemies have none and cannot change the player's timescale.
- Time powers: **Time Slow** and **Time Stop**. The player is unaffected by either (`modules.md`).

## Cooldown tags
| Tag | Runs on |
|---|---|
| `Cooldown:Fixed` | Real seconds |
| `Cooldown:Scaled` | The timescale |

- Rule: while a time power is active, player modules use fixed cooldowns.

## Open
- Under the rule above, `Cooldown:Scaled` has no users outside cutscenes. Keep the tag only if a module needs it.
