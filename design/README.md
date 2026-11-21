# Zenthium SWIFT Heroes (working title)

Status: design. No build plan yet.

## Core concept
- Top-down 2D superhero game inspired by comic book, DCU and MCU universes. Mostly comedic tone.
- Mission-based. Solo only.
- Platforms: mouse and keyboard, and gamepad. No touch: the game needs 10+ buttons plus movement.
- The player runs the hero organization **SWIFT** (`lore.md`).
- Missions reward Zenny (`economy.md`), spent at HQ (`hq.md`).

## Files
| File | Covers |
|---|---|
| `heroes.md` | Hero roster, CAH, slots |
| `stats.md` | SWIFT stats, secondary stats, detection, Defiance |
| `combat.md` | Damage, damage reduction, knockback, friendly fire, resources |
| `statuses.md` | Status rules, resists, status catalog |
| `time.md` | Timescale and time powers |
| `modules.md` | Module schema, tags, module info, full module catalog |
| `difficulty.md` | Difficulty ranks, per-rank scaling, mission modifiers |
| `missions.md` | Mission flow, types, secondary goals, citizens, extraction |
| `factions.md` | Shared faction rules: ranks, weights, minimum ranks |
| `Factions/` | One file per faction, from `Factions/_Template.md` |
| `maps.md` | Map generation, size, Blazithion's districts, sockets, fog of war |
| `enemies.md` | Enemy spawning (threat budget, squads, reinforcements, arrival tags, population cap) and AI |
| `world.md` | Buildings, walls, doors, windows, props, fire, Valuables |
| `economy.md` | Zenny currencies, hero reward bonus, dev options |
| `hq.md` | HQ between missions and its tabs |
| `story.md` | Story Arc rules |
| `StoryArcs/` | One file per Story Arc |
| `lore.md` | Pure flavor: world lore, megacorporations |
| `hud.md` | HUD layout, indicators, end-of-mission screen, options |
| `controls.md` | Default bindings |
| `balance.md` | Balance foundation: formulas, anchors, standard tiers, power budget, progression and price targets |
| `data/` | All per-item numbers, as CSV files (see `balance.md`) |
| `future.md` | Ideas board: features we won't build now |

Each file ends with an `## Open` section for its unresolved questions.

## Open
- Final title. Working title is "Zenthium SWIFT Heroes".
