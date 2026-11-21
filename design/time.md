# Time System

- A global **timescale** affects movement, DoT ticks, timers, cinematic cutscenes, and anything that moves over time, such as projectiles.
- **Only player heroes have time powers.** Enemies have none and cannot change the player's timescale.
- All cooldowns run in real seconds, never on the timescale.

## Time powers
Durations and cooldowns are in `data/modules.csv`.

| Power | Effect |
|---|---|
| Time Slow | The game runs slower for a while; the player is unaffected |
| Time Stop | The game freezes. The player is unaffected. Damage to frozen entities lands immediately. Projectiles freeze and have no collision while frozen, so the player can walk through bullets. Countdown mission timers pause too (intended) |

## Open
- (none)
