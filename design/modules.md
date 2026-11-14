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
| Slot cost | |
| Tags | See below |
| Triggers | See below |
| Effects | |
| Stat scaling | SWIFT stat(s) it scales with (`stats.md`) |
| Cooldown tag | `Cooldown:Fixed` or `Cooldown:Scaled` (`time.md`) |

- **Tags (examples):** `Melee`, `Ranged`, `Time`, `Debuff`, `Summon`, `Cooldown:Fixed`, `Cooldown:Scaled`. Shared tags let gear and powers change secondary stats without hard-coded pairings.
- **Triggers (examples):** always-on, on hit, on damage taken, on Defiance proc, on timer, on activation.
- **Presentation:** every module needs an icon, a visual flash, a sound cue and optional comic callout text ("POW!").
- **Tiers:** Zenny colors can map to module rarity or tier, with metallic variants as an upgrade tier.

## Catalog
Defiance is a core Will rule, not a module (`stats.md`). Faction units are described in `factions.md`.

| Module | Category | Owner | Tags | Mechanics |
|---|---|---|---|---|
| Kick | Base action | All heroes | `Melee` | Strength scaling, scaling knockback. Outside slots |
| Speed Punch | Active | Hero | `Melee` | Attacks 3x faster than Kick, full Kick damage per hit, no knockback. No timescale cooldown tag. Pairs well with time powers |
| Super Lucky | Passive | Hero | | Raises Luck so all random rolls favor the character (inspired by Domino) |
| Time Slow | Active | Hero | `Time` | Lowers timescale; player unaffected |
| Time Stop | Active | Hero | `Time` | Freezes timescale; player unaffected |
| Meat Slap | Active | Dr. Edd | `Ranged` | Ranged attack |
| Regeneration | Passive | Dr. Edd | | HP regen |
| Engulf | Active | Dr. Edd | | Grabs and holds the target |
| Bone Spike | Active | Stalker | `Ranged` | Ranged attack |
| Half-Invisible | Passive | Stalker | | Stealth; uses Detectability rules |
| Durability | Passive | Breaker | | Damage reduction |
| Broken Limb | On hit | Breaker | `Debuff` | Slowing debuff |
| Infectious Bite | On hit | Zombie | `Debuff` | "Infected" DoT debuff |
| Turn on Death | Passive | Zombie | | An Infected target becomes a zombie when it dies |
| Treads | Passive | Tank | | Mobility |
| Cannons | Active | Tank | `Ranged` | Ranged attack |
| Turrets | Active | Hacker | `Summon` | Summons turret entities |
| Slot Disable | On hit | Hacker | `Debuff` | Disables a random equipment slot for 5 s. Intelligence can resist |
| Chrome Body | Passive | Kingpin | | Durability and implant effects |
| Machine Gun | Active | Mafioso | `Ranged` | Ranged attack |
| Blade Arms | Active | Mafioso | `Melee` | Melee attack |
| Super Stats | Passive | Chad | | Speed, durability, stat scaling |

## Open
- Speed Punch does full Kick damage at 3x the attack rate. If it outclasses Kick, give it a longer cooldown or lower damage per hit.
