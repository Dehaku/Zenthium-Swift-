# Difficulty

## Ranks
D (lowest), C, B, A, S, then S2, S3, S4 and so on, forever.

- **Unlocking:** beat at least one mission on a rank to unlock the next.
- Each rank keeps everything from the ranks below it.

| Rank | Adds | Map size (`maps.md`) | Locked doors |
|---|---|---|---|
| D | The baseline. Mostly goons; Champions are rare. All mission intel is revealed | Small | Wood, Glass |
| C | Champions appear regularly | Medium | Stone |
| B | Reinforcements: waves arrive from the map edges partway through. Heavy Turrets in some buildings (`world.md`) | Medium | Stone |
| A | More Leader-led missions. Fire spreads between buildings | Large | Metal |
| S | Leaders gain an extra random module | Large | Crystalline |
| S2 and up | Only the per-rank increases below | Large | Crystalline |

## Every rank above D
- **Enemies:** +25% health and +25% damage.
- **Enemy stats:** +20% to all SWIFT stats. This adds to the innate rank boost (`factions.md`) as one source. Example at B: goons +40%, Champions +140%, Leaders +240%.
- **Rewards:** +25%.
- **Mission goals:** harder timers, rescue counts and other number goals (`missions.md`).
- **Hidden intel:** each intel field on the mission map has +5% chance to be hidden (C: 5%, B: 10%, and so on). Rank D always reveals everything.
- **Exits:** fewer exit zones, placed farther away. Always at least 1.

## Enemy types by rank
- Every enemy entity has a **minimum rank** to spawn, so factions gain new entity types as the rank rises (`factions.md`).

## Enemy behavior
- **Alarms:** when an enemy becomes aware of the player, nearby enemies become aware too. The alarm radius grows with rank.
- **Hostages:** at higher ranks, goons Drag civilians as human shields.
- **Leaders' extra modules:** from rank S, Leaders draw an extra random module from every module in the game, the same way Infinity Anarchous do.

## Mission modifiers
Occasional twists on a mission, not on every mission.
- **Night Time:** all vision ranges are halved, for everyone.
- **Zenthium Fissure:** a fissure opens on the map and now and then spawns hostile neutral creatures from Zenthium (`lore.md`) that attack everyone.

## Open
- Do the +25% increases add up per rank (S2 = +125%) or compound (1.25 x 1.25 ...)?
- From which rank do hostages appear?
- Alarm radius, and how much it grows per rank.
- Chance of a Leader-led mission per rank.
- Leaders' extra modules: only one from S, or one more per S rank?
- Mission modifiers: how often they appear, from which rank, whether they show as mission intel, and whether the mission creator can set them.
- The higher-rank enemy types for each faction.
- The Zenthium Fissure creatures.
