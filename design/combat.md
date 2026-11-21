# Combat

## Damage
- General rule: melee damage scales with Strength, ranged damage with Finesse. Each module sets its own formula (`modules.md`).
- Toughness gives HP.
- Damage types: **Physical**, **Magic**, **Energy**.
- Friendly fire is off by default. It is on only while the player holds the friendly fire button (`controls.md`).

## Movement
- Base move speed: 6 m/s. A starting value; expect lots of tuning.
- Sprint and other speed bonuses are percentages of it (`modules.md`).

## Damage reduction
Two forms:
- **Armor (flat):** subtracts a fixed amount from every hit. Toughness gives Armor equal to 50% of its value, so damage stats outweigh Toughness 2:1. Modules can add more.
- **Damage Reduction (%):** cuts every hit by a percentage. Comes from modules, such as Weather the Storm. Multiple sources multiply, so they never reach 100% (two 50% sources give 75%).

Order: Armor first, then Damage Reduction. Example: a 100 damage hit against 10 Armor and 30% reduction deals (100 - 10) x 0.7 = 63.

Every hit deals at least 5% of its original damage.

Damage over time (DoT) ignores both Armor and Damage Reduction, so it stays dangerous.

## Knockback
- Strength comes from the module (Kick scales with Strength).
- Knockback resistance is yes or no. It comes from modules with the `KnockbackResistant` tag.
- Entities knocked into a wall deal heavy damage to it (`world.md`).

## Statuses
Buffs, debuffs, crowd control and resists are in `statuses.md`.

## Resources
- **Stamina**, **Mana**, **Charge** and **Ammo**.
- Shown as bars under the player.
- Every module that spends a resource also grants just enough of it to be used once, plus +1 regen per second. Grants from several modules add to the same pool.
- Passive resource modules, such as Soulful, the Battery modules and Sprinter, add extra reserves and regen on top (`modules.md`).
- So any entity, hero or enemy, can always use the modules it has, and modules don't need balancing against each other.
- Modules can use a cooldown, a resource, or both.

## Open
- (none)
