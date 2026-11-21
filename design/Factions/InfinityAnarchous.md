# Infinity Anarchous

Rogues with random powers and gear who refuse to join any organization, led by a superhuman who's too chill to lead.

Shared faction rules are in `../factions.md`.

## Faction rules
- **Wildcards:** most Anarchous entities draw random modules at spawn (`../factions.md`). Goons draw 1, Champions draw 2 on top of Chad Adjacent.
- **No Bosses:** everyone's in it for themselves. They grab Valuables and run off the map with them.
- **Rules Are Fake** (from rank S):
  - Anarchous entities have a 50% chance to ignore any debuff, on top of normal resists (`../statuses.md`).
  - 25% of citizens are disguised Rogues. They reveal themselves when the player gets close or tries to Drag them. Each reveal lowers the mission's citizen count by 1, so it never counts against Rescue goals (`../missions.md`).
- **Faction tags:** `LootDestination:MapEdge` (`../world.md`).
- **Leader behavior:** Chad doesn't loot. He wanders between sockets for the whole mission, checking out buildings. He fights back anything within reach but never chases: less a proper threat, more a wandering map hazard.
- **Countdown target:** a bomb spray-painted with "NO MASTERS".
- **Comic callouts:** "NO MASTERS!", "RULES ARE FAKE!", "IT'S ALL GOOD." (Chad).
- **Story Arcs:** Headhunted (`../StoryArcs/Headhunted.md`).

## Entities
| Rank | Entity | Min rank | Description | Modules | Locked until | Tags |
|---|---|---|---|---|---|---|
| Leader | Chad | D | Superhuman "chill guy" who goes along with his crazed friends | Chill Punch, Vibe Check, Lean Back, Super Stats, Super Speed, No Big Deal | Vibe Check (C), Lean Back (B), No Big Deal (A) | |
| Champion | Anarchist | D | Random powers and gear, super stats | Chad Adjacent, 2 random | | |
| Champion | Chaos Agent | B | Even more random | Chad Adjacent, 3 random | | |
| Champion | Prodigy | A | Draws only from hero modules | Chad Adjacent, 2 random (hero modules only) | | |
| Goon | Rogue | D | One random power or piece of gear | 1 random | | `Coward` |
| Goon | Wildcard | C | Two random powers or pieces of gear | 2 random | | `Coward` |

- Modules are in AI priority order; random draws come after fixed modules. Locked modules are skipped below their rank (`../factions.md`).

## Spawning
- **Arrival:** `Arrival:OnFoot` (`../enemies.md`).
- **Champion share:** default (`../enemies.md`).
- **Budget costs:** in `../data/entities.csv`. Chad is outside the budget.
- **Mission Weight:** every type 1.
- **Location Weight:** clubs 2, parks 2; everything else 1.

## Open
- Story Arc idea: "Chad's Block Party", Chad throws a party that gets wildly out of hand.
