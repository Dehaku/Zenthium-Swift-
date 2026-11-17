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
| Drag | Base action | All heroes | | Grab a target and pull it behind you. Checks for citizens first, then Incapacitated (0 HP) enemies. Carries 1 target per 100 Strength (at least 1). You can fight while dragging and aren't slowed, except by Stubborn citizens (`missions.md`). Dragged targets can't be hurt |
| Sprint | Base action | All heroes | | Toggle. +50% move speed, no stamina cost. Enemies and civilians don't sprint |
| Speed Punch | Active | Hero | `Melee` | Attacks 3x faster than Kick, full Kick damage per hit, no knockback. Meant to be stronger than Kick. Pairs well with time powers |
| Power Throw | Active | Hero | | Uses Strength. Throw anything and anyone you're dragging |
| Time Slow | Active | Hero | `Time` | See `time.md` |
| Time Stop | Active | Hero | `Time` | See `time.md` |
| Super Lucky | Passive | Hero | | Large Luck boost (`luck.md`). Inspired by Domino |
| Deathly Rage | Passive | Any | `Buff` | On Defiance proc, grants the Deathly Rage buff: triples Strength and Toughness. Does not stack. Lasts until the mission ends |
| Soulful | Passive | Hero | `CannotBeDisabled` | +50% spell damage, 150 Mana, +5 Mana/s |
| High-Capacity Battery | Passive | Hero | `CannotBeDisabled` | Charge: high capacity, low regen |
| Quick-Charge Battery | Passive | Hero | `CannotBeDisabled` | Charge: low capacity, high regen |
| Reaper Battery | Passive | Hero | `CannotBeDisabled` | Charge: average capacity, no regen. Defeating a creature refills it to full |
| Sprinter | Passive | Hero | | 100 Stamina, +10 Stamina/s. Sprint is 2x faster |
| Charming | Passive | Hero | | On approach: 50% chance to turn a Stubborn citizen Scared, 5% chance to convert a goon to your side. Each target rolls once; a hidden Charmed debuff marks it |
| Hex | Active | Unassigned | `Debuff`, `Resist:Will` | Spell. Disables a random active power slot for 5 s |
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

## Open
- Does Deathly Rage's tripled Toughness also scale current HP, or only max HP?
- Sprinter: is +10/s Stamina regen? Does its 2x sprint drain Stamina, and is 2x on top of base Sprint's +50%?
- Numbers for the three Battery modules.
