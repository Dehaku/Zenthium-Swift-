# Hexbound Coven

An overly enthusiastic magic cult that treats every crime as a ritual, led by Blazithion's Grand Librarian.

Shared faction rules are in `../factions.md`.

## Faction rules
- **Magic items:** Valuables (`../world.md`) count as magic items for the Coven. While Vex holds Valuables, every Coven entity deals +5% damage per Valuable she holds. With no Leader on the mission, there's no power-up. The bonus never carries past the mission.
- **Portal Storm** (from rank S): every 30 s, a portal opens near the player and releases 2 Imps.
- **Faction tags:** none. Loot goes to Vex (`../world.md`).
- **Leader behavior:** Vex loots Valuables like a goon, and her goons bring theirs to her. The Coven's power-up only works while she holds Valuables.
- **Comic callouts:** "SHHH!", plus two more (Open).
- **Story Arcs:** Relic Fever (`../StoryArcs/RelicFever.md`).

## Entities
| Rank | Entity | Min rank | Description | Modules | Locked until | Tags |
|---|---|---|---|---|---|---|
| Leader | Grand Librarian Vex | D | Steals magic items, silences heroes and collects late fees | Shush!, Book Barrage, Late Fee, Portal Step | Late Fee (C), Shush! (B), Portal Step (A) | |
| Champion | Hexer | D | Disables heroes' powers | Hex, Hex Bolt | | |
| Champion | Summoner | D | Summons Imps | Summon Imps, Hex Bolt | | |
| Champion | Pyromancer | C | Fire specialist | Fire Ring, Fire Wand | | |
| Champion | Archivist | A | Necromancer: gets fallen Coven members back on their feet | Reanimate, Hex Bolt | | |
| Goon | Acolyte | D | Carries a fire wand that can set things on fire | Fire Wand | | `Coward` |
| Goon | Familiar | B | A black cat that grabs Valuables and runs them to Vex | Tow Beam | | `Coward` |

- Modules are in AI priority order. Locked modules are skipped below their rank (`../factions.md`).
- **Summons:** Summon Imps and Portal Storm create Imps, small melee entities with Imp Claw.

## Spawning
- **Arrival:** `Arrival:Portal` (`../enemies.md`).
- **Champion share:** default (`../enemies.md`).
- **Budget costs:** Acolyte 1, Familiar 2, Hexer 4, Summoner 5, Pyromancer 5, Archivist 6. Vex is outside the budget; Imps are summons.
- **Mission Weight:** Arson Riot 3, Countdown 2, Invasion 1, Rescue 1.
- **Location Weight:** museums 3, antique shops 3, libraries 3, mansions 2; everything else 1.

## Open
- Late Fee needs more to it.
- Two more comic callouts.
- Story Arc idea: "The Forbidden Stacks", Vex tries to seize Blazithion's library and its sealed books.
- Numbers for Shush!, Book Barrage, Late Fee, Portal Step, Hex Bolt, Imp Claw, Fire Ring and Reanimate, for the numbers pass.
