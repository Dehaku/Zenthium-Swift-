# Statuses

Buffs, debuffs, hidden markers and states. Module durations and amounts live with the module (`modules.md`); this file says what each status does and the rules they share.

## General rules
- **Stacking:** reapplying a status refreshes its timer by default. A status can set its own rule instead, such as Intensity (each application adds a layer) or Independent (each application runs separately).
- **Slows** multiply together, so they never reach 100%.
- **Timescale:** status durations and DoT ticks follow the timescale, so Time Slow stretches them and Time Stop freezes them (`time.md`).
- **Crowd control** (Stun, Root, Taunted, Engulfed, Hypnotized) can be chained without limit. Leaders and the player take half-length crowd control. Effects that last "while inside" an area, like Smoke Bomb's stun, pulse on them instead: 0.5 s on, 0.5 s off.
- **Invulnerable** entities take no damage and no new debuffs.
- **Dragged targets:** their statuses keep running, but DoTs deal no damage while they're dragged.
- **Display:** small icons above the head, plus a comic callout when a status lands ("STUNNED!", "ROOTED!").

## Resists
- Every module that applies a debuff has a `Resist:<Stat>` tag naming the stat that resists it.
- A successful resist ignores the debuff entirely.
- Resist chance = defender's resist stat ÷ (defender's resist stat + attacker's stat). Equal stats give 50%. Luck modifies the roll (`luck.md`).
- The attacker's stat is the one the applying module scales with. If it has none, use the attacker's value of the resist stat.

## Catalog
| Status | Kind | Effect | Stacking | Sources |
|---|---|---|---|---|
| Stun | Crowd control | Can't move, attack or use powers. Can still be knocked back. Carriers keep their Valuables | Refresh | Spectrum Bolt, Smoke Bomb, Megaphone |
| Root | Crowd control | Can't move, but can attack and use powers. Can still be knocked back | Refresh | Glyph Trap |
| Taunted | Crowd control | Must target the taunter | Refresh | Taunt |
| Hypnotized | Crowd control | Fights on the side of whoever hypnotized it. Leaders take half-length, like other crowd control | Refresh | Hypnotic Gaze |
| Engulfed | Crowd control | Grabbed and held | Refresh | Engulf |
| Marked | Debuff | Deals less damage, and takes more damage from all sources | Refresh | Taunt, Final Notice |
| Burn | DoT | Fire damage over time. Lasts 10x longer on props | Independent | Fire Spell Tome, Spectrum Bolt, Hoop of Fire, Fire Ring, burning buildings, exploding vehicles (`world.md`) |
| Infected | DoT | Damage over time. Any entity reduced to 0 HP while Infected rises as a zombie on the spot | Refresh | Infectious Bite, Outbreak, Acid Spit |
| Broken Limb | Slow | Slower movement | Refresh | Broken Limb |
| Gooed | Slow | Slower movement | Refresh | Goo Punch, Sticky Body |
| Carrying Treasure | Slow | See `world.md` | Intensity (per Valuable) | Valuables |
| Slot Disable | Disable | A random gear slot stops working | Independent: each hit disables another slot | Slot Disable, Repossess |
| Hex | Disable | A random active power slot stops working | Independent: each hit disables another slot | Hex |
| Silenced | Disable | All active power slots stop working | Refresh | Shush! |
| Numbing Toxin | Disable | A random passive power slot stops working | Independent: each hit disables another slot | Numbing Toxin |
| Pied | Screen effect (player only) | Smears part of the screen, fading out over its duration | Intensity (each pie adds a smear) | Cream Pie |
| Deathly Rage | Buff | Greatly boosts Strength and Toughness | Doesn't stack | Deathly Rage |
| Spotlight | Buff | All stats boosted while inside the spotlight | Lasts while inside | Spotlight |
| Gold-Plated Chrome | Buff | Toughness and Damage Reduction per Valuable held | Intensity (per Valuable) | Gold-Plated Chrome |
| Notarized | Buff | Damage Reduction while near a Notary | Lasts while in range | Notarized |
| Gel Coated | Buff | Can't be Burned | Refresh | Gel Coat |
| Reactive Plating | Buff | Armor per stack, up to a cap. Ends after a few seconds without being hit | Intensity (per hit) | Reactive Plating |
| Overdrive | Buff | Bonus damage and move speed | Lasts while at low HP | Overdrive |
| Mutate | Buff | Stronger in every stat, can't be knocked back | Lasts while at low HP | Mutate |
| Soul Shard | Buff | More max Charge per stack | Intensity (per defeat) | Crystal Hunger |
| Defiance Roll | Hidden marker | Lowers the Defiance proc chance (`stats.md`) | Intensity (per proc) | Defiance |
| Charmed | Hidden marker | Charming has already rolled on this target | Permanent | Charming |
| Incapacitated | State | At 0 HP. Can't act. Enemies can be Dragged and captured; civilians are only downed, and can be Dragged out to safety | | 0 HP |
| Dragged | State | Can't be hurt | | Drag |
| Intangible | State | Passes through walls, doors, props and entities | | Phase Shift |
| Invulnerable | State | Takes no damage | | Defiance, Dash, No Big Deal |

- Modules with the `CannotBeDisabled` tag are immune to Disable statuses.

## Open
- (none)
