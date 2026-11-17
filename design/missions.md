# Missions

- Average length: about 5 minutes.
- One faction per mission (`factions.md` decides which).
- Failing a mission loses its rewards. No other penalty (`economy.md`).

## Start sequence
1. Camera zooms in on the mission goal and the mission text displays.
2. Camera zooms out and pans over.
3. Camera zooms in on the player hero.

- Skip: hold any button for 1 s. "Skipping" shows centered in the bottom third of the screen, with a circle that grows until it skips.

## Difficulty
- Payday 2-style tiers. Higher tiers give bigger rewards.
- For now, difficulty only raises enemy health and damage. Enemies scale with difficulty, not with the player's stats.
- Some mission rules also scale with difficulty (below).

## Types
| Type | Goal | Fail |
|---|---|---|
| Rescue | Enter a location and extract citizens | Fewer than 25% of the target citizens rescued. The % rises with difficulty |
| Countdown | Find and break a bomb or horror egg before it goes off or hatches. Difficulty sets the timer and how hard the target is to reach (locked doors, wall and door materials) | It goes off |
| Arson Riot | Goons set buildings and vehicles on fire. Draft rules in Open | See Open |
| Invasion | King of the hill. Enemies head for a location (armory, bank, hospital, lab, etc.) to take it. Defeat them all | The loss timer runs out. Each enemy inside the location's radius speeds it up; the player's presence doesn't block it |

- Each Invasion location has random flavor text, such as "They're trying to steal the money!" or "They're trying to release a deadly pathogen!"

## Shared rules
- Goons are scattered around every mission and fight the player once aware of them (`stats.md`).
- A mission has a chance to be led by a super villain (a faction Leader). Beating them isn't required.
- Each mission gets one random **optional secondary goal**, such as:
  - Smash an egg nest.
  - Rescue a scientist.
  - Show off for a news reporter (use a power or gear in front of them).
  - Defeat the Leader.
  - Capture the Leader, Champions or Goons.
- Secondary goals reward, at random, extra Zenny or a percentage reward bonus (`economy.md`).

## Citizens
| Type | Behavior |
|---|---|
| Scared | Panics and flees from threats |
| Incapacitated | Cannot move on their own |
| Stubborn | Won't move. Much slower to grab, and dragging one slows you by 25% |

- Citizens can be Infected and turn into zombies.

## Extraction
- **Drag** citizens out by hand (`modules.md`).
- **Extraction gear:** special equipment, such as a Metal Gear-style balloon or a teleportation device.
- **Exits:** any map edge and/or a marked zone, such as an evac vehicle.

## Open
- Arson Riot rules. Draft: fires can't be put out, so the player stops as many buildings igniting as possible. Fail if a set % of buildings ignite (the % scales with difficulty). At very high difficulty, fire spreads to neighboring buildings.
- How does capturing work? Drag the Incapacitated target to an exit?
