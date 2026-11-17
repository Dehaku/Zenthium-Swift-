# Combat

## Damage
- General rule: melee damage scales with Strength, ranged damage with Finesse. Each module sets its own formula (`modules.md`).
- Toughness gives HP.
- Damage types: **Physical**, **Magic**, **Energy**.
- Friendly fire is off by default. It is on only while the player holds the friendly fire button (`controls.md`).

## Damage reduction
Two forms:
- **Armor (flat):** subtracts a fixed amount from every hit.
- **Damage Reduction (%):** cuts every hit by a percentage. Comes from modules, such as Weather the Storm.

## Knockback
- Strength comes from the module (Kick scales with Strength).
- Knockback resistance is yes or no. It comes from modules with the `KnockbackResistant` tag.
- Entities knocked into a wall deal heavy damage to it (`world.md`).

## Debuff resists
- Every module that applies a debuff has a `Resist:<Stat>` tag naming the stat that resists it.
- A successful resist ignores the debuff entirely.

## Resources
- **Stamina**, **Mana**, **Charge** and **Ammo**.
- Shown as bars under the player.
- Capacity and recharge rate come from modules, such as Soulful, the Battery modules and Sprinter (`modules.md`).
- Modules can use a cooldown, a resource, or both.

## Open
- Damage reduction details: where Armor comes from, the order the two forms apply in, how percentages stack, and a minimum damage per hit.
- Full list of status effects and their stacking rules (Infected, Broken Limb, Slot Disable, Hex, Numbing Toxin, Charmed, Defiance Roll, Deathly Rage). Revisit later.
