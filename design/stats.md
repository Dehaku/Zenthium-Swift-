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
- **Trigger:** incoming damage would take an entity to 0 HP or below. It is left at 1 HP instead.
- **Proc chance:** 1% per 10 Will. Can exceed 100%.
  - Example: at 200%, two procs are guaranteed and the remaining roll is 0%.
- **Cost:** each proc removes 100 Will for the rest of the mission, which lowers the proc chance.
- **Effect:** 5 seconds of invulnerability.
- **Presentation:** time slows briefly and "I will not die here!" displays.
- **HUD:** the Will percentage shows next to the health bar.

## Open
- Does Defiance apply to every entity (enemies included) or only to heroes? The rule currently says "an entity".
