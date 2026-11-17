# Modules

"Module" is the code name for active powers, passive powers and gear. Players see the names Powers and Gear.

## Entity model
- Heroes, enemies and civilians are all the same **Entity**.
- Special abilities come entirely from slotted modules. Everything is data-driven.
- Enemies use fixed module lists from the same data.

## Schema
| Field | Notes |
|---|---|
| ID | Unique |
| Category | Active, Passive, Gear |
| Tags | See below |
| Triggers | See below |
| Effects | |
| Stat formula | Unique per module. Examples: one stat at 3x; two stats at 2x each; raw Intelligence plus 3x the bonuses from magic gear such as spell books |
| Resources | The resource it spends, or the capacity and regen it grants (`combat.md`) |
| Damage type | Physical, Magic or Energy (`combat.md`) |
| Cooldown | In real seconds (`time.md`) |

- Every module takes 1 slot.
- Gear can have actives, passives or both. Gear actives have their own buttons (`controls.md`).
- Magic modules and items generally use Intelligence and Will; each module decides how.
- **Tags (examples):** `Melee`, `Ranged`, `Time`, `Buff`, `Debuff`, `Summon`, `Resist:<Stat>`, `KnockbackResistant`, `CannotBeDisabled`. Shared tags let modules change secondary stats without hard-coded pairings.
- **Triggers (examples):** always-on, on hit, on damage taken, on Defiance proc, on timer, on activation, on approach.
- **Presentation:** every module needs an icon, a visual flash, a sound cue and optional comic callout text ("POW!").

## Module info
- Holding the "more info" button shows the module's formula with live numbers. Values in square brackets are the summed totals of the matching bonuses.
- Format example: `Damage = Strength([Strength])x2 + Gear([GearBonus]), Attack Speed = Finesse([Finesse])x3 + Gear([GearBonus])`

## Buying, tiers and upgrades
- Bought with Zenny at HQ: powers in the Zen Garden, gear in the Research Lab (`hq.md`).
- Tiers are separate modules shown as one, with up and down arrows to cycle through the versions. Zenny colors can map to tiers, with metallic variants as an upgrade tier.
- Owned modules can be upgraded.

## Catalog
Defiance is a core Will rule, not a module (`stats.md`). Faction units are described in `factions.md`. "Unassigned" modules have no owner yet but are in the pool (for example, for Infinity Anarchous).

| Module | Category | Owner | Tags | Mechanics |
|---|---|---|---|---|
| Kick | Base action | All heroes | `Melee` | 10 damage, 3 s cooldown. Strength scaling, scaling knockback |
| Drag | Base action | All heroes, Grey, Strongman | | Grab a target and pull it behind you. Checks for citizens first, then Incapacitated (0 HP) enemies. Carries 1 target, +1 per 100 Strength (150 Strength carries 2). You can fight while dragging and aren't slowed, except by Stubborn citizens (`missions.md`). Dragged targets can't be hurt |
| Sprint | Base action | All heroes | | Toggle. +50% move speed, no stamina cost. Enemies and civilians don't sprint |
| Uppercut | Active | Hero | `Melee` | Like Kick, with 5x knockback. Costs 50 Stamina |
| Speed Punch | Active | Hero | `Melee` | Attacks 3x faster than Kick, full Kick damage per hit, no knockback. Meant to be stronger than Kick. Pairs well with time powers |
| Power Throw | Active | Hero | | Uses Strength. Throw anything and anyone you're dragging |
| Time Slow | Active | Hero | `Time` | See `time.md` |
| Time Stop | Active | Hero | `Time` | See `time.md` |
| Super Lucky | Passive | Hero | | Large Luck boost (`luck.md`). Inspired by Domino |
| Deathly Rage | Passive | Any | `Buff` | On Defiance proc, grants the Deathly Rage buff: triples Strength and Toughness; the extra HP is added to current HP too. Does not stack. Lasts until the mission ends |
| Soulful | Passive | Hero | `CannotBeDisabled` | +50% spell damage, 150 Mana, +5 Mana/s |
| High-Capacity Battery | Passive | Hero | `CannotBeDisabled` | 200 Charge, +5 Charge/s |
| Quick-Charge Battery | Passive | Hero | `CannotBeDisabled` | 50 Charge, +20 Charge/s |
| Reaper Battery | Passive | Hero | `CannotBeDisabled` | 100 Charge, no regen. Defeating a creature refills it to full |
| Sprinter | Passive | Hero | | 100 Stamina, +10 Stamina/s regen. Doubles Sprint's bonus to +100% move speed. Sprinting never costs Stamina; Stamina is spent by other modules |
| Weather the Storm | Passive | Hero | | When hit, spends 5 Stamina (if you have it) for no knockback and 25% less damage from that hit |
| Charming | Passive | Hero | | On approach: 50% chance to turn a Stubborn citizen Scared, 5% chance to convert a goon to your side. Each target rolls once; a hidden Charmed debuff marks it |
| Hex | Active | Hexer | `Debuff`, `Resist:Will` | Spell. Disables a random active power slot for 5 s |
| Numbing Toxin | On hit | Unassigned | `Debuff`, `Resist:Toughness` | Poison. Disables a random passive power slot for 5 s |
| Meat Slap | Active | Dr. Edd | `Ranged` | Ranged attack |
| Regeneration | Passive | Dr. Edd | | HP regen |
| Engulf | Active | Dr. Edd | | Grabs and holds the target |
| Bone Spike | Active | Stalker | `Ranged` | Ranged attack |
| Half-Invisible | Passive | Stalker | | 50% transparent. Uses Detectability rules |
| Durability | Passive | Breaker | | Damage reduction |
| Broken Limb | On hit | Breaker | `Debuff`, `Resist:Toughness` | Slowing debuff |
| Infectious Bite | On hit | Zombie | `Debuff`, `Resist:Toughness` | "Infected" DoT debuff |
| Turn on Death | Passive | Zombie | | An Infected target becomes a zombie when it dies, civilians included |
| Treads | Passive | Tank | | Mobility |
| Cannons | Active | Tank | `Ranged` | Ranged attack |
| Turrets | Active | Hacker | `Summon` | Summons turret entities |
| Slot Disable | On hit | Hacker | `Debuff`, `Resist:Intelligence` | Disables a random gear slot for 5 s. Hits from the Hacker's turrets don't count |
| Chrome Body | Passive | Kingping | | Durability and implant effects |
| Machine Gun | Active | Mafioso | `Ranged` | Ranged attack |
| Blade Arms | Active | Mafioso | `Melee` | Melee attack |
| Super Stats | Passive | Chad | | Speed, durability, stat scaling |
| Tractor Beam | Active | GleebPeep | | Beam that pulls in every entity and prop in its path |
| Tractor Pull | Active | Tractor Drone | | Pulls a hero or citizen toward the nearest Repo Agency crop circle (`factions.md`) |
| Immovable | Passive | Shield Bearer, Strongman | `KnockbackResistant` | Can't be knocked back |
| Energy Blaster | Active | Shield Bearer, Grey | `Ranged` | Ranged attack, Energy damage |
| Spotlight | Active | The Ringmaster | `Buff` | A 20 m spotlight centered on him. Circus units inside get +50% to all stats |
| Cannonball Launch | Active | Human Cannonball | `Melee` | Launches at a target for huge knockback |
| Cream Pie | Active | Clown | `Ranged`, `Debuff`, `Resist:Intelligence` | Thrown pie. On hit, applies "Pied": smears part of the player's screen for a few seconds |
| Summon Imps | Active | Summoner | `Summon` | Summons imp entities |
| Fire Wand | Active | Acolyte | `Ranged` | Magic fire attack. Can set buildings and vehicles on fire |

## Open
- Pied's duration.
