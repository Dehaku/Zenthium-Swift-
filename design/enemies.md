# Enemy Spawns and AI

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
| Invasion | A light starting force; most of the budget arrives as waves heading for the location. At every rank, a wave arrives on the reinforcement timing below, each about 25% of the budget, until the budget runs out |

## Reinforcements
- From rank B (`difficulty.md`).
- A wave arrives when 60 s pass or the enemies alive drop below 50% of the starting force, whichever comes first.
- Each wave is about 20% of the starting budget.
- At most 3 waves at B, plus 1 more per rank above B.
- Waves enter from a map edge at least 50 m from the player, or drop in at a random socket at least 20 m from the player: a visible landing area shows a 10 s countdown before they land.
- Waves arrive aware. They head for, in order of priority and availability: the objective, their Leader, the player's last known position, the map center.
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
- Enemies that escape off the map count as defeated. Valuables they carry off count as stolen (`world.md`).
- **Population cap:** at most 60 enemies alive at once by default, adjustable in the options menu. Only goons, Champions and Leaders from the spawner count; Heavy Turrets, allies and Fissure creatures don't. Reinforcements wait while the cap is reached.

## Neutral spawns
- **Heavy Turrets:** from rank B, each building has a 15% chance to have one (`world.md`).
- **Zenthium Fissure** (`difficulty.md`): the first spawn comes 60 s in: 3 Zen Creatures, 1 Zen Soldier and the Zen Commander together. After that, a Zen Creature every 20 s and a Zen Soldier every 60 s.
- The Fissure can be closed by destroying it. It has high HP and follows Champion scaling. Every 25% of its HP lost spawns a Zen Soldier and a Zen Creature.

## AI
Applies to enemies, neutrals and the player's allies (converted goons, summons).

### States
Idle (patrol, `## Squads`), Combat, Searching, Looting (`world.md`), Objective (Invasion location, carrying Valuables, fleeing the map).

### Using modules
- Each entity has a designer-ordered module list. In combat it uses the first module that's off cooldown, can afford its cost and has a target in range.
- This is how "Reprogram first" works: Reprogram sits at the top of the Hacker's list.

### Targets
- Enemies attack anyone not on their side, civilians included. Outside Invasion, they only attack civilians once they're in Combat (aware of the player or an ally).
- They attack the nearest valid target. Exceptions: Taunt overrides it, and an entity that just took damage turns on whoever hit it, unless it was an ally.
- Enemies prefer the player and the player's allies. They fight neutrals only when attacked by them, or when nothing better is in view.
- Neutral creatures (Zenthium) have no preference: they attack anything not on their own team. Heavy Turrets never attack civilians (`world.md`).

### Becoming aware
- An entity hit while unaware becomes aware instantly.
- On becoming aware, a comic "!" pops over its head, and it waits 0.5 s before acting.
- **Alert:** during that 0.5 s, a half-transparent grey circle shows a 10 m alert radius. When the 0.5 s ends, allies inside it become aware too, each starting its own 0.5 s delay and alert circle. Alerts chain, so a large group can wake up all at once. If the entity is defeated first, no alert goes out.

### Losing the target
- When line of sight breaks, the entity goes to the target's last known position and searches for about 10 s. Then its awareness drains over 3 s and it returns to Idle.

### Movement
- Melee: chase and attack.
- Ranged: move until the target is in range, stop and fire. Back off a little if the target comes within 3 m.
- Allies (converted goons, summons): outside combat, follow the player and stay within about 10 m.

### Other rules
- **Telegraphs:** modules with the `Telegraph` tag flash red for 0.5 s before they hit.
- **Champions and Leaders** use the same AI, with their own module lists. Leaders keep their special behaviors (entrance, looting, fleeing with Valuables).
- **Friendly fire:** enemy attacks can hurt other enemies, but never make them target each other. Dev option: a toggle to turn this off.
- **Cowardice:** entities with the `Coward` tag roll once when they drop below 20% HP: a 25% chance to panic and run for the map edge until they escape. Goons get it by default. Zombies, Zenthium creatures and summons don't.

## Open
- Budget costs for every entity.
