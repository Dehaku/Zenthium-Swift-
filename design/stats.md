# Stats

## Primary stats (SWIFT)
Upgradable and uncapped. Bought with Zenny in the HQ Training Room. Every entity starts at 10 in every stat, before modifications of any kind. Civilians stay at 10. Designers set each preset hero's starting stats on top of that.

| Stat | Role |
|---|---|
| **S**trength | Melee damage; Kick damage and knockback; Drag capacity |
| **W**ill | Defiance (below); magic modules; resisting some debuffs |
| **I**ntelligence | Tech and equipment skill; magic modules; resisting some debuffs, such as Slot Disable |
| **F**inesse | Ranged damage; precision; passive dodge chance. Does not affect move speed |
| **T**oughness | HP; resisting some debuffs, such as Infected and Broken Limb |

- Percentage stat boosts multiply, except the difficulty bonus, which adds to the innate rank boost (`difficulty.md`). Example: Chad's 10 Strength x3 (innate +200%, `factions.md`) x3 (Super Stats, `modules.md`) = 90.
- These roles are general. Each module defines exactly how it uses stats (`modules.md`).
- Which stat resists a debuff is set by a tag on the module that applies it (`statuses.md`).

## Secondary stats
Not directly upgradable. Modules change them through tags.
- **Detectability:** how fast enemies notice the character (below).

## Detection
- Enemies see in all directions, out to a set range. Line of sight is required: buildings and props block it (`world.md`).
- While a character is in view, an awareness bar fills over the enemy. At 100%, the enemy is aware of them.
- The bar fills slower at longer range and for lower Detectability. Default Detectability: instant at 10 m, 10 s at 100 m.

## Defiance (Will)
Applies to every entity.

- **Trigger:** anything that would take an entity to 0 HP or below. It is left at 1 HP instead.
- **Cleanse:** clears all DoTs and debuffs on the entity, except Carrying Treasure and hidden markers (`statuses.md`). An Infected entity saved this way does not turn into a zombie.
- **Proc chance:** 1% per 10 Will. Can exceed 100%.
  - Example: at 213%, two procs are guaranteed and the remaining roll is 13%.
- **Cost:** each proc gives the entity a silent **Defiance Roll** debuff of 100%. It removes 100% from the entity's Defiance proc chance, as if one guaranteed proc had been used up. Lasts the mission and stacks per proc. The Will stat itself is untouched, so nothing else that uses Will is affected.
  - Example: at 213%, the first proc leaves 113%, the second leaves 13%, and a third is a 13% roll.

| | Player | Everyone else |
|---|---|---|
| Invulnerability | 5 s | 1 s |
| Presentation | Time slows briefly and "I will not die here!" displays | "Defiance!" pops above the head and fades out over 1 s, with a quiet sound cue |
| HUD | Effective proc chance (after Defiance Roll) next to the health bar | None |

- The player's slowdown is a plain timescale change. Cooldowns always run in real seconds (`time.md`), so it needs no special rules.

## Open
- (none)
