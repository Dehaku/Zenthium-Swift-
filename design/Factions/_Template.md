# Faction Name

One or two sentences: who they are and what they want.

Shared faction rules are in `../factions.md`.

## Faction rules
Mechanics only this faction has: its signature twist, faction-wide effects, special loot rules. Keep each one short and point to the file that owns any shared rule.

- **Faction tags:** tags every entity in the faction has, such as `LootDestination:<place>`. Optional.
- **Leader behavior:** anything special the Leader does beyond its modules, such as looting or fleeing. "Standard" if nothing.
- **Comic callouts:** a few lines shown when they act ("POW!").
- **Story Arcs:** arcs this faction can run (`../StoryArcs/`).

## Entities
| Rank | Entity | Min rank | Description | Modules | Locked until | Tags |
|---|---|---|---|---|---|---|
| Leader | | D | | Modules in AI priority order | Optional: Module (C), Module (B) | |
| Champion | | D | | | | |
| Goon | | D | | | | `Coward` |

- Modules are listed in AI priority order. "Locked until" is optional; leave it empty to unlock everything at every rank (`../factions.md`).
- New modules go in `../modules.md`; new statuses in `../statuses.md`.

## Spawning
Neutral factions that don't spawn normally (such as Zenthium) skip this section.

- **Arrival:** `Arrival:<tag>` (`../enemies.md`).
- **Champion share:** default, or per rank (`../enemies.md`).
- **Budget costs:** a cost per entity. The Leader is outside the budget.
- **Mission Weight:** a relative weight per mission type; 1 if unlisted (`../factions.md`).
- **Location Weight:** a relative weight per location; 1 if unlisted.

## Open
- (none)
