# Technomafia

A cyberpunk crime family with chrome implants, running Blazithion's rackets.

Shared faction rules are in `../factions.md`.

## Faction rules
- **We Own This Block:** every Heavy Turret on a Technomafia mission (from rank B, `../world.md`) starts hacked to their side. The player can hack them back with Reprogram.
- **Hit Contract** (from rank S): every 60 s, a van drops 3 Mafiosos who head straight for the player.
- **Faction tags:** none. Loot goes to Kingping (`../world.md`).
- **Leader behavior:** Kingping loots Valuables like a goon, and his goons bring theirs to him. Gold-Plated Chrome makes him tougher the more he holds.
- **Countdown target:** a bomb.
- **Comic callouts:** "BADA-PING!", "NOTHING PERSONAL.", "CONNECTION TERMINATED."
- **Story Arcs:** Headhunted (`../StoryArcs/Headhunted.md`).

## Entities
| Rank | Entity | Min rank | Description | Modules | Locked until | Tags |
|---|---|---|---|---|---|---|
| Leader | Kingping | D | "King Ping": mafia don with a chrome body and experimental tech implants | Gatling Arm, Hush Money, Chrome Fist, Overdrive, Chrome Body, Gold-Plated Chrome | Hush Money (C), Gatling Arm (B), Overdrive (A) | |
| Champion | Tank | D | Tank treads for a lower body, cannons for arms | Ram, Cannons, Treads, Immovable | | |
| Champion | Hacker | D | Hijacks machines, deploys Mini Turrets and scrambles heroes' gear | Reprogram, Turrets, Slot Disable | | |
| Champion | Kneecapper | C | Bruiser with a chrome pipe | Chrome Pipe, Broken Limb | | |
| Champion | Cyberdoc | A | Back-alley implant surgeon who crashes heroes' powers | Hex, Numbing Toxin | | |
| Goon | Mafioso | D | Machine gun in hand, blades built into the arms | Machine Gun, Blade Arms | | `Coward` |
| Goon | Drone Courier | B | Non-combatant looter: grabs Valuables and rushes them to Kingping | Tow Beam | | `Coward`, `Hackable` |

- Modules are in AI priority order. Locked modules are skipped below their rank (`../factions.md`).
- **Summons:** the Hacker's Turrets create Mini Turrets, which are `Hackable`.

## Spawning
- **Arrival:** `Arrival:Van` (`../enemies.md`).
- **Champion share:** default (`../enemies.md`).
- **Budget costs:** in `../data/entities.csv`. Kingping is outside the budget.
- **Mission Weight:** Invasion 3, Countdown 2, Rescue 1, Arson Riot 1.
- **Location Weight:** banks 3, clubs 2, warehouses 2, stores 2; everything else 1.

## Open
- Story Arc idea: "Protection Racket", shaking down Blazithion's shops district by district.
- Numbers for Gatling Arm, Hush Money (radius), Chrome Fist, Overdrive, Ram, Chrome Pipe and Mini Turrets, for the numbers pass.
