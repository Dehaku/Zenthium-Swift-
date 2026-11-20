# Difficulty

## Ranks
D (lowest), C, B, A, S, then S2, S3, S4 and so on, forever.

- **Unlocking:** beat at least one mission on a rank to unlock the next.
- Each rank keeps everything from the ranks below it.

| Rank | Adds | Map size (`maps.md`) | Locked doors |
|---|---|---|---|
| D | The baseline. Mostly goons; Champions are rare. All mission intel is revealed | Small | Wood, Glass |
| C | Champions appear regularly | Medium | Stone |
| B | Reinforcement waves (`enemies.md`). Heavy Turrets in some buildings (`world.md`) | Medium | Stone |
| A | Fire spreads between buildings (`world.md`) | Large | Metal |
| S | Leaders gain extra random modules (below) | Large | Crystalline |
| S2 and up | Only the per-rank increases below | Large | Crystalline |

## Every rank above D
- **Enemies:** +10% health and +10% damage. These add up per rank (S2, five ranks above D, is +50%).
- **Enemy stats:** +20% to all SWIFT stats. This adds to the innate rank boost (`factions.md`) as one source. Example at B: goons +40%, Champions +140%, Leaders +240%.
- **Rewards:** +25%, adding up the same way.
- **Mission goals:** harder timers, rescue counts and other number goals (`missions.md`).
- **Hidden intel:** each intel field on the mission map has +5% chance to be hidden (C: 5%, B: 10%, and so on). Rank D always reveals everything.
- **Exits:** fewer exit zones, placed farther away. Always at least 1.
- **Leader-led missions:** 0% at D, +20% per rank (C 20%, B 40%, A 60%), and guaranteed from S.

## Enemy types by rank
- Some entities have modules locked until a higher rank (`factions.md`).
- Every enemy entity has a **minimum rank** to spawn, so factions gain new entity types as the rank rises. Each faction's higher-rank entities are designed in their faction file (`Factions/`).

## Leaders' extra modules
- From rank S, Leaders gain one extra random module per S rank (S: 1, S2: 2, and so on), with extra slots to hold them.
- They're drawn from every module in the game, the same way Infinity Anarchous draw theirs.

## Mission modifiers
- From rank C, every mission has a 50% chance to get a modifier. If it does, it rolls another 50% for a second one, and so on until a roll fails. Each modifier can appear only once; the rolls stop when none are left.
- Modifiers show as intel in one "Hazards" field (`hq.md`).
- **Night Time:** all vision ranges are halved, for everyone.
- **Zenthium Fissure:** a fissure opens on the map and now and then spawns hostile neutral creatures from Zenthium (`Factions/Zenthium.md`, timing in `enemies.md`) that attack everyone.

## Open
- Hidden-intel chance has no cap, so very high S ranks hide everything. Cap it?
