# Missions

- Average length: about 5 minutes.
- One faction per mission, picked by faction weights (`factions.md`).
- Failing a mission loses its rewards. No other penalty (`economy.md`).

## Start sequence
1. Camera zooms in on the mission goal and the mission text displays.
2. Camera zooms out and pans over.
3. Camera zooms in on the player hero.

- Skip: hold any button for 1 s. "Skipping" shows centered in the bottom third of the screen, with a circle that grows until it skips.

## Difficulty
- Letter ranks from D to S and beyond (`difficulty.md`). Enemies scale with rank, not with the player's stats.
- Some mission rules also scale with rank (below).

## Types
| Type | Goal | Fail |
|---|---|---|
| Rescue | Enter a location and extract citizens. Target citizens: Small map 6, Medium 10, Large 15 | Fewer than 25% of the target citizens rescued. The % rises with difficulty |
| Countdown | Find and break the faction's Countdown target (a bomb, horror egg, beacon and so on, set in its faction file) before it goes off. The timer is 180 s at rank D, 10 s shorter per rank, never under 90 s. Difficulty also sets how hard the target is to reach (locked doors, wall and door materials) | It goes off |
| Arson Riot | Goons set buildings and vehicles on fire (`world.md`). Defeat every enemy. Every goon gets an Ignite action: 5 s at a building, reset by any damage, used only while the player is outside its attack range | Too many buildings burning or burned out: 50% at D, 5% lower per rank, never below 20% |
| Invasion | King of the hill. Enemies head for a location (armory, bank, hospital, lab, etc.) to take it. Defeat them all | The 120 s loss timer runs out. Each enemy inside the location's Huge radius speeds it up by 10%; the player's presence doesn't block it |

- Each Invasion location has random flavor text, such as "They're trying to steal the money!" or "They're trying to release a deadly pathogen!"

## Shared rules
- Goons are scattered around every mission and fight the player once aware of them (`stats.md`).
- Neutral entities (Zenthium creatures, Heavy Turrets) never count toward "defeat every enemy".
- A mission has a chance to be led by a super villain (a faction Leader). Beating them isn't required.
- Each mission gets one random **optional secondary goal**, such as:
  - Smash an egg nest.
  - Rescue a scientist.
  - Show off for a news reporter (use a power or gear in front of them).
  - Defeat the Leader (only when a Leader is present).
  - Capture the Leader (only when a Leader is present), Champions or Goons.
  - Prevent 50% of Valuables from being stolen (`world.md`). The % changes with difficulty.
- Secondary goals reward, at random, extra Zenny or a percentage reward bonus (`economy.md`).
- Destroying a Zenthium Fissure counts as a completed bonus secondary goal: +25% rewards (`Factions/Zenthium.md`).

## Citizens
| Type | Behavior |
|---|---|
| Scared | Panics and flees from any enemy inside their 20 m fear range |
| Incapacitated | Cannot move on their own |
| Stubborn | Won't move. Much slower to grab, and dragging one slows you by 25% |

- Citizens can be Infected and turn into zombies.

## Extraction
- **Drag** citizens out by hand (`modules.md`).
- **Extraction gear:** special equipment, such as a Metal Gear-style balloon or a teleportation device.
- **Exits:** marked zones on the map's edges, such as an evac vehicle. Fewer at higher ranks, always at least 1 (`difficulty.md`). Fleeing enemies can leave from any edge.
- **Capture:** an Incapacitated enemy inside an exit zone is captured. How it got there doesn't matter (Drag, Power Throw, knockback).

## Open
- In Arson Riot, when a goon could both loot and ignite, which comes first?
