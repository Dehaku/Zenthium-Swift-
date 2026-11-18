# Enemy Spawns

## Threat budget
- Each enemy entity has a budget cost. Example: goon 1, Champion 5.
- Each mission gets a budget from its map size: Small 30, Medium 60, Large 100. The budget doesn't grow with rank; enemy stats already do (`difficulty.md`).
- The spawner spends the budget on entities the mission's faction can field at that rank (minimum ranks, `factions.md`).
- Champions can use at most part of the budget. Each faction sets its own share (`factions.md`), so designers can tune it, for example tilting Zombies toward goons. Default for every faction for now: D 10%, C 30%, B 40%, A and up 50%.
- Leaders are outside the budget. When the Leader roll succeeds, the Leader makes a dramatic entrance 30 s into the mission, using the faction's arrival tag (below).

## Squads
- Enemies spawn in squads of 3-5 goons around a socket (`maps.md`), sometimes led by a Champion.
- **Idle:** until they notice the player, squads wander between nearby sockets at half move speed, like a patrol. Goons still loot Valuables they see (`world.md`).

## Mission type profiles
Where each mission type spends its budget:

| Type | Placement |
|---|---|
| Rescue | Squads near clusters of citizens |
| Countdown | A heavy guard around the target, light elsewhere |
| Arson Riot | Squads spread across many buildings |
| Invasion | A light starting force; most of the budget arrives as waves heading for the location |

## Reinforcements
- From rank B (`difficulty.md`).
- A wave arrives when 60 s pass or the enemies alive drop below 50% of the starting force, whichever comes first.
- Each wave is about 20% of the starting budget.
- Waves enter from a map edge at least 50 m from the player, or drop in: a visible landing area shows a 10 s countdown before they land.
- **Arrival tags:** each faction has an arrival tag that sets how its waves show up (`factions.md`). Tags are reusable by any faction:

| Tag | Arrival |
|---|---|
| `Arrival:Van` | Vans drive in from a map edge and unload |
| `Arrival:ClownCar` | A tiny car drives in from a map edge and far too many come out |
| `Arrival:OnFoot` | Walk in from a map edge |
| `Arrival:Beam` | Drop in: beamed down |
| `Arrival:Sewer` | Drop in: crawl out of a manhole |
| `Arrival:Portal` | Drop in: step out of a magic portal |

## Limits
- Defeated enemies never respawn. New enemies only come from reinforcements, Invasion waves and Zenthium Fissures.
- **Population cap:** at most 60 enemies alive at once by default, adjustable in the options menu. Reinforcements wait while the cap is reached. Fissure creatures ignore the cap.

## Neutral spawns
- **Heavy Turrets:** from rank B, each building has a 15% chance to have one (`world.md`).
- **Zenthium Fissure** (`difficulty.md`): the first spawn comes 60 s in: 3 Zen Creatures, 1 Zen Soldier and the Zen Commander together. After that, a Zen Creature every 20 s and a Zen Soldier every 60 s.

## Open
- Budget costs for every entity.
