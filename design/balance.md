# Balance Foundation

The shared formulas, anchors and standard values that every number is measured against. First pass; expect tuning.
Numbers live in plain-text CSV files in `data/`, their only home. A check script reads them, applies the formulas here, and reports the real numbers with over- and under-budget flags. On request, it can also generate a spreadsheet view for exploring; that view is never where numbers are stored. This file holds the rules.

## 1. Core formulas
Constant names refer to `data/constants.csv`, where every value lives.

| Value | Formula |
|---|---|
| HP | Toughness x `hp_per_toughness`. Leaders also x `leader_hp_multiplier` |
| Armor | Toughness x `armor_per_toughness` (`combat.md`) |
| Normal damage | `normal_damage_base` + `normal_damage_per_stat` x the module's stat (Strength for melee, Finesse for ranged, or the module's own). Kick is Normal damage with Strength |
| Dodge chance | Finesse x `dodge_per_finesse`, capped at `dodge_cap` |
| Awareness | Fills instantly within `awareness_instant_range`, and takes `awareness_max_time` at `vision_range`, scaling linearly between (`stats.md`) |
| Resource value | 1 point is worth `resource_seconds_per_point` of cooldown, matching the +1 regen (`combat.md`) |

- **Enemy attacks** default to the `enemy_default_damage_tier` (section 4), so heroes survive the anchor below.
- **Provisional:** Leaders' extra HP and the enemy default damage tier were added to hit the anchors. Expect playtesting to change them.

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

| Anchor | Target |
|---|---|
| Kicks to defeat a goon | About 3 |
| Kicks to defeat a Champion | About 10 |
| Kicks to defeat a Leader | About 40 |
| Goon hits a hero survives | About 15 |
| Mission pace | About 5 minutes, about 30 enemies on a Medium map: one fight every 20-30 s |

- `python3 tools/balance.py report` calculates the actual values to compare.

## 4. Standard tiers
Modules use these words; each word means a standard value, set in `data/constants.csv` (the `tier` rows).

| Scale | Tiers |
|---|---|
| Damage (x Normal damage) | Light, Normal, Heavy, Massive |
| Duration | Brief, Short, Medium, Long |
| Radius | Small, Medium, Large, Huge |
| Knockback | Light, Normal, Heavy, Huge |
| Cooldown | Spammable, Short, Medium, Long, Ultimate |
| Range | Melee, Short, Medium, Long |
| Utility (damage budget multiplier) | None, Some, Strong |

## 5. Power budget
- **Longer cooldown or bigger cost, stronger effect.** Base rule: a damage module's damage = Normal damage x (cooldown / `kick_cooldown`). Kick is the 1x reference.
- The check script flags a module as OVER or UNDER budget when its damage is more than 1.5x or less than 0.5x its budget.
- A resource cost counts as that many seconds of cooldown (section 1).
- Utility (crowd control, mobility, healing) trades against damage: each module has a Utility tier that shrinks its damage budget.

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
Prices are set in how many missions' worth of rewards they cost, then converted to Zenny using the first-pass income per mission (`economy` rows in `data/constants.csv`). The prices themselves live in `data/prices.csv`. Each mission type shifts the income mix (`economy.md`).

## 8. Benchmarks
Scenarios to sanity-check the numbers. If one feels wrong, fix the anchor or the formula, not one module.
- Rush Hour at rank D, starting slots only, against a squad of 4 Greys.
- A full preset kit at rank B against a Champion.
- A Leader fight at rank S.
- A Recruit just after Headhunted (rank S2), with starter modules only.

## Data and tools
| File | Holds |
|---|---|
| `data/constants.csv` | Formula constants, standard tier values, income. `mirror` rows copy a few rules from other files for the script; keep them in sync |
| `data/modules.csv` | Per-module inputs: stat, damage tier, cooldown or resource cost, and other tiers |
| `data/entities.csv` | Per-entity inputs: rank tier, minimum rank, budget cost |
| `data/heroes.csv` | Preset hero stats |
| `data/props.csv` | Prop and vehicle values |
| `data/prices.csv` | Prices in missions of work |
| `../tools/balance.py` | `report` prints the calculated numbers and flags; `xlsx` writes a spreadsheet view to `build/` (not committed) |

## Open
- The numbers pass, in this order: modules, entities and heroes, props and world values, then prices and income. Each step moves that area's existing numbers out of the markdown files into its CSV.
- Knockback scaling with stats.
- Income mix per mission type.
