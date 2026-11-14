# Stats and Combat

## Primary stats (SWIFT)
Upgradable, uncapped and grow without limit. Upgraded in the HQ Training Room.

| Stat | Role |
|---|---|
| **S**trength | Scales melee gear damage, and Kick damage and knockback |
| **W**ill | Powers Defiance (below) |
| **I**ntelligence | Tech and equipment skill. Can resist Hacker slot disabling |
| **F**inesse | Scales ranged gear damage. Speed, dodging, precision |
| **T**oughness | Grants HP. Can resist DoTs and debuffs such as Infected and Broken Limb |

## Secondary stats
Not directly upgradable. Gear and powers change them through shared tags (`modules.md`).
- **Luck:** a modifier on every random roll the character makes.
- **Detectability:** how easily enemies spot the character.

## Combat rules
- Melee gear damage scales with Strength.
- Ranged gear damage scales with Finesse.
- Toughness gives HP.
- Every hero can always Kick (`modules.md`).

## Defiance (Will)
Applies to every entity.

- **Trigger:** incoming damage would take an entity to 0 HP or below. It is left at 1 HP instead.
- **Proc chance:** 1% per 10 Will. Can exceed 100%.
  - Example: at 213%, two procs are guaranteed and the remaining roll is 13%.
- **Cost:** each proc gives the entity a silent **Defiance Roll** debuff of 100%. It removes 100% from the entity's Defiance proc chance, as if one guaranteed proc had been used up. Lasts the mission and stacks per proc. The Will stat itself is untouched, so nothing else that uses Will is affected.
  - Example: at 213%, the first proc leaves 113%, the second leaves 13%, and a third is a 13% roll.

| | Player | Everyone else |
|---|---|---|
| Invulnerability | 5 s | 1 s |
| Presentation | Time slows briefly and "I will not die here!" displays | "Defiance!" pops above the head and fades out over 1 s, with a quiet sound cue |
| HUD | Will percentage next to the health bar | None |
