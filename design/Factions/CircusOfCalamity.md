# Circus of Calamity

A traveling circus that's also a crime ring. Every heist is a show.

Shared faction rules are in `../factions.md`.

## Faction rules
- **Encore!:** while the Ringmaster is present, the first time each Champion is Incapacitated, it pops back up at 50% HP with a bow and an "ENCORE!" callout. Once per Champion.
- **Three-Ring Circus** (from rank S): three stationary Spotlights appear around the map. Circus entities inside them get +50% to all stats.
- **Faction tags:** none. Loot goes to the Ringmaster (`../world.md`).
- **Leader behavior:** standard looting. Encore! only works while he's alive. He announces each reinforcement wave like a show (flavor only).
- **Countdown target:** a giant jack-in-the-box. It's a bomb.
- **Comic callouts:** "HONK!", "TA-DA!", "SHOWTIME!"
- **Story Arcs:** Headhunted (`../StoryArcs/Headhunted.md`).

## Entities
| Rank | Entity | Min rank | Description | Modules | Locked until | Tags |
|---|---|---|---|---|---|---|
| Leader | The Ringmaster | D | Runs the show. His spotlight buffs every performer near him | Spotlight, Hoop of Fire, Whip Crack, Grand Finale | Hoop of Fire (C), Grand Finale (A) | |
| Champion | Strongman | D | Grabs citizens, props and goons and throws them at you; punches when there's nothing to grab | Power Throw, Drag, Haymaker, Immovable | | |
| Champion | Human Cannonball | D | Launches into you for huge knockback, often into walls | Cannonball Launch | | |
| Champion | Acrobat | B | Fast flanker | Dash, Flying Kick | | |
| Champion | Lion Tamer | A | Fights alongside a summoned lion | Summon Lion, Whip Crack | | |
| Goon | Clown | D | Throws cream pies | Cream Pie | | `Coward` |
| Goon | Juggler | C | Throws flaming torches and bowling balls | Bowling Ball, Torch Toss | | `Coward` |

- Modules are in AI priority order. Locked modules are skipped below their rank (`../factions.md`).
- **Summons:** Lions are melee beasts with Lion Maul, and `Coward`.

## Spawning
- **Arrival:** `Arrival:ClownCar` (`../enemies.md`).
- **Champion share:** default (`../enemies.md`).
- **Budget costs:** in `../data/entities.csv`. The Ringmaster is outside the budget; Lions are summons.
- **Mission Weight:** Invasion 3, Rescue 2, Countdown 1, Arson Riot 1.
- **Location Weight:** parks 3, clubs 3, stores 2; everything else 1.

## Open
- Story Arc idea: "Opening Night", the Circus comes to Blazithion and each stage is one of their shows.
- Numbers for Hoop of Fire, Whip Crack, Grand Finale, Haymaker, Flying Kick, Summon Lion, Lion Maul, Bowling Ball and Torch Toss, for the numbers pass.
