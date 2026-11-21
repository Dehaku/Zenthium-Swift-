# Galactic Repo Agency

Alien bureaucrats repossessing Earth, one item at a time.

Shared faction rules are in `../factions.md`.

## Faction rules
- **Crop circles:** placed at random around the map (their source: `../lore.md`). 1 at rank D, plus 1 per rank, up to 5 at S; no more after that.
  - A citizen inside a crop circle is abducted: they disappear for good. Citizens the player is dragging are abducted too, so stay clear of crop circles.
  - A hero pulled into a crop circle isn't abducted. It's only an annoyance.
  - A crop circle takes all Valuables (`../world.md`) off any entity that enters it, the player included. They count as stolen.
- **Faction tags:** `LootDestination:CropCircle`. Repo entities take Valuables, and citizens they drag, to the nearest crop circle instead of to their Leader (`../world.md`, `../enemies.md`).
- **Leader behavior:** standard. GleebPeep's loot goes to crop circles like everyone else's.
- **Mothership Strike** (from rank S): every 30 s, an orbital beam targets the player's position. A red ring and a countdown from 5 show where it will hit, like Breaching Charge (`../modules.md`). It deals 300 damage in a 5 m radius.
- **Countdown target:** a repossession beacon.
- **Comic callouts:** "PAST DUE!", "REPOSSESSED!", "SIGN HERE!".
- **Story Arcs:** Relic Fever (`../StoryArcs/RelicFever.md`), Hostile Takeover (`../StoryArcs/HostileTakeover.md`).

## Entities
| Rank | Entity | Min rank | Description | Modules | Locked until | Tags |
|---|---|---|---|---|---|---|
| Leader | GleebPeep | D | Tired repo officer with a tablet and a ship's tractor beam | Call for Backup, Repossess, Final Notice, Tractor Beam, Tablet Slap | Final Notice (C), Repossess (C), Call for Backup (B) | |
| Champion | Tractor Drone | D | Hovering drone that pulls heroes and citizens toward the crop circles | Tractor Pull | | `Hackable` |
| Champion | Shield Bearer | D | Armored; can't be knocked back, and blocks shots from the front | Energy Shield, Energy Blaster, Immovable, High-Capacity Battery | | |
| Champion | Auditor | C | Anti-stealth: exposes the player to everyone nearby | Audit, Repossess | | |
| Champion | Notary | A | Support: notarizes nearby allies, making them tougher | Notarized | | |
| Goon | Grey | D | Energy blasters; drags citizens away | Energy Blaster, Drag | | `Coward` |
| Goon | Tow Saucer | B | A small saucer that steals props, citizens and Valuables from range and flies them to a crop circle. Crashes when destroyed: 50 damage in a 5 m radius | Tow Beam | | `Coward`, `Hackable` |

- Modules are in AI priority order. Locked modules are skipped below their rank (`../factions.md`).
- At rank D on Small maps, the Champion share can't afford any Champions. That's intended.

## Spawning
- **Arrival:** `Arrival:Beam` (`../enemies.md`).
- **Champion share:** default (`../enemies.md`).
- **Budget costs:** Grey 1, Tow Saucer 2, Tractor Drone 4, Shield Bearer 5, Auditor 5, Notary 6. GleebPeep is outside the budget.
- **Mission Weight:** Rescue 3, Invasion 2, Countdown 1, Arson Riot 1.
- **Location Weight:** banks 2, museums 2, parks 2; everything else 1.

## Open
- Numbers for Tractor Beam (range, pull strength), Tractor Pull, Tablet Slap and Audit (cooldown), for the numbers pass.
