# Balance Foundation

The shared formulas, anchors and standard values that every number is measured against. First pass; expect tuning.
The final numbers will live in a spreadsheet with formulas, so changing an anchor updates everything that depends on it. This file holds the rules.

## 1. Core formulas
| Value | Formula | Examples |
|---|---|---|
| HP | 10 x Toughness | Civilian 100. Toughness 20 hero: 200 |
| Leader HP | x2 on top of the above | A rank D Leader (Toughness 30): 600 |
| Armor | 50% of Toughness (`combat.md`) | Toughness 10: 5 Armor |
| Kick damage | 10 + 2 x Strength | Strength 10: 30. Strength 20: 50 |
| Normal damage | Like Kick: 10 + 2 x the module's stat (Strength for melee, Finesse for ranged, or the module's own) | |
| Dodge chance | 0.5% per point of Finesse, capped at 75% | Finesse 10: 5%. Finesse 20: 10% |
| Vision range | 100 m. Awareness fills instantly at 10 m and takes 10 s at 100 m, scaling linearly between (`stats.md`) | |
| Resource value | 1 point of resource is worth 1 s of cooldown, matching the +1 regen (`combat.md`) | |

- **Enemy attacks** default to the Light damage tier (section 4), so heroes survive the anchor below.
- **Provisional:** Leaders' x2 HP and Light-tier enemy attacks were added to hit the anchors. Expect playtesting to change them.

## 2. Stacking rules
Where each rule lives, in one place:

| Rule | File |
|---|---|
| Percentage stat boosts multiply; the difficulty bonus adds to the innate rank boost | `stats.md` |
| Armor first, then Damage Reduction (sources multiply); every hit deals at least 5%; DoTs ignore both | `combat.md` |
| Slows multiply | `statuses.md` |
| Status stacking: Refresh by default | `statuses.md` |
| Reward bonuses add | `economy.md` |
| Rank scaling: +10% health and damage, +20% stats, added per rank | `difficulty.md` |

## 3. Anchors
Target outcomes at rank D for a starting hero (Strength 10-20, Toughness 10-20):

| Anchor | Target | Check with the formulas |
|---|---|---|
| Kicks to defeat a goon | About 3 | Goon: 100 HP, 5 Armor. Kick does 25-45 → 3-4 hits |
| Kicks to defeat a Champion | About 10 | Champion (stats 20): 200 HP, 10 Armor. Kick does 20-40 → 5-10 hits |
| Kicks to defeat a Leader | About 40 | Leader (stats 30): 600 HP, 15 Armor. Kick does 15-35 → 17-40 hits |
| Goon hits a hero survives | About 15 | Goon Light hit: 15 damage. Hero takes 5-10 → 10-40 hits |
| Mission pace | About 5 minutes, about 30 enemies on a Medium map | One fight every 20-30 s |

## 4. Standard tiers
Modules use these words; each word means a standard value.

| Scale | Tiers |
|---|---|
| Damage (x Normal damage) | Light 0.5x, Normal 1x, Heavy 2x, Massive 4x |
| Duration | Brief 1 s, Short 3 s, Medium 5 s, Long 10 s |
| Radius | Small 3 m, Medium 6 m, Large 10 m, Huge 15 m |
| Knockback | Light 2 m, Normal 4 m, Heavy 8 m, Huge 15 m |
| Cooldown | Spammable 1 s, Short 5 s, Medium 15 s, Long 30 s, Ultimate 60 s |
| Range | Melee 2 m, Short 8 m, Medium 15 m, Long 30 m |

## 5. Power budget
- **Longer cooldown or bigger cost, stronger effect.** Base rule: a damage module's damage = Normal damage x (cooldown / 3 s). Kick (3 s) is the 1x reference.
- A resource cost counts as that many seconds of cooldown (section 1).
- Utility (crowd control, mobility, healing) trades against damage: a module with strong utility gets a lower damage tier for the same cooldown.

## 6. Progression targets
How strong the player should be at each rank, against the enemies there. Enemy figures are for a goon.

| Rank | Goon stats | Goon HP and damage bonus | Target hero key stats |
|---|---|---|---|
| D | 10 | +0% | 20 |
| C | 12 | +10% | 25 |
| B | 14 | +20% | 30 |
| A | 16 | +30% | 35 |
| S | 18 | +40% | 40 |
| Each S rank after | +2 | +10% | +5 |

- Target: a hero's two key stats are about twice a same-rank goon's.

## 7. Economy in missions of work
Prices are set in how many missions' worth of rewards they cost, then converted to Zenny.

| Purchase | Cost | Currency |
|---|---|---|
| 1 stat point | 1 mission | Basic |
| A module | 3 missions | Gem |
| A module tier upgrade | 3 missions per tier | Gem |
| A slot | 10 missions | Metallic |
| A preset hero | 25 missions | Metallic |
| An extra Recruit | 25 missions | Metallic |

- First pass income at rank D, before bonuses: about 100 Basic, 20 Gem and 2 Metallic per mission. Each mission type shifts the mix (`economy.md`).

## 8. Benchmarks
Scenarios to sanity-check the numbers. If one feels wrong, fix the anchor or the formula, not one module.
- Rush Hour at rank D, starting slots only, against a squad of 4 Greys.
- A full preset kit at rank B against a Champion.
- A Leader fight at rank S.
- A Recruit just after Headhunted (rank S2), with starter modules only.

## Open
- Build the numbers spreadsheet from these formulas and tiers.
- Knockback scaling with stats.
- Income mix per mission type.
