# Infinity Anarchous

Rogues with random powers and gear who refuse to join any organization, led by a superhuman who's too chill to lead.

Shared faction rules are in `../factions.md`.

## Faction rules
- **Wildcards:** most Anarchous entities draw random modules at spawn (`../factions.md`). Goons draw 1, Champions draw 2 on top of Chad Adjacent.
- **No Bosses:** everyone's in it for themselves. They grab Valuables and run off the map with them.
- **(Rank S effect):** TBD (Open).
- **Faction tags:** `LootDestination:MapEdge` (`../world.md`).
- **Leader behavior:** Chad doesn't loot. He wanders between sockets for the whole mission, checking out buildings.
- **Countdown target:** TBD (Open).
- **Comic callouts:** TBD (Open).
- **Story Arcs:** none yet.

## Entities
| Rank | Entity | Min rank | Description | Modules | Locked until | Tags |
|---|---|---|---|---|---|---|
| Leader | Chad | D | Superhuman "chill guy" who goes along with his crazed friends | Chill Punch, Vibe Check, (TBD), Super Stats, Super Speed, (TBD) | Vibe Check (C), first TBD (B), second TBD (A) | |
| Champion | Anarchist | D | Random powers and gear, super stats | Chad Adjacent, 2 random | | |
| Champion | Chaos Agent | B | Even more random | Chad Adjacent, 3 random | | |
| Champion | Prodigy | A | Draws only from hero modules | Chad Adjacent, 2 random (hero modules only) | | |
| Goon | Rogue | D | One random power or piece of gear | 1 random | | `Coward` |
| Goon | Wildcard | C | Two random powers or pieces of gear | 2 random | | `Coward` |

- Modules are in AI priority order; random draws come after fixed modules. Locked modules are skipped below their rank (`../factions.md`).

## Spawning
- **Arrival:** `Arrival:OnFoot` (`../enemies.md`).
- **Champion share:** default (`../enemies.md`).
- **Budget costs:** Rogue 1, Wildcard 2, Anarchist 5, Chaos Agent 6, Prodigy 7. Chad is outside the budget.
- **Mission Weight:** every type 1.
- **Location Weight:** clubs 2, parks 2; everything else 1.

## Open
- Chad's two remaining modules (replacing Go With the Flow and Power Nap).
- The rank S faction effect.
- Countdown target and comic callouts.
- Story Arc idea: "Chad's Block Party", Chad throws a party that gets wildly out of hand.
- Numbers for Chill Punch and Vibe Check, for the numbers pass.
