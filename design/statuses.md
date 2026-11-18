# Statuses

Buffs, debuffs, hidden markers and states. Module durations and amounts live with the module (`modules.md`); this file says what each status does and the rules they share.

## General rules
- **Stacking:** reapplying a status refreshes its timer by default. A status can set its own rule instead, such as Intensity (each application adds a layer) or Independent (each application runs separately).
- **Slows** multiply together, so they never reach 100%.
- **Timescale:** status durations and DoT ticks follow the timescale, so Time Slow stretches them and Time Stop freezes them (`time.md`).
- **Crowd control** (Stun, Root, Taunted, Engulfed) can be chained without limit. Leaders and the player take half-length crowd control.
- **Dragged targets:** their statuses keep running, but DoTs deal no damage while they're dragged.
- **Display:** small icons above the head, plus a comic callout when a status lands ("STUNNED!", "ROOTED!").

## Resists
- Every module that applies a debuff has a `Resist:<Stat>` tag naming the stat that resists it.
- A successful resist ignores the debuff entirely.
- Resist chance = defender's resist stat ÷ (defender's resist stat + attacker's stat). Equal stats give 50%. Luck modifies the roll (`luck.md`).

## Catalog
| Status | Kind | Effect | Stacking | Sources |
|---|---|---|---|---|
| Stun | Crowd control | Can't move, attack or use powers. Can still be knocked back. Carriers keep their Valuables | Refresh | Spectrum Bolt, Smoke Bomb, Megaphone |
| Root | Crowd control | Can't move, but can attack and use powers. Can still be knocked back | Refresh | Glyph Trap |
| Taunted | Crowd control | Must target the taunter | Refresh | Taunt |
| Engulfed | Crowd control | Grabbed and held | Refresh | Engulf |
| Marked | Debuff | Deals less damage, and takes more damage from whoever marked it | Refresh | Taunt |
| Burn | DoT | Fire damage over time | Independent | Fire Spell Tome, Spectrum Bolt |
| Infected | DoT | Damage over time. Dying while Infected turns the target into a zombie | Refresh | Infectious Bite |
| Broken Limb | Slow | Slower movement | Refresh | Broken Limb |
| Carrying Treasure | Slow | See `world.md` | Intensity (per Valuable) | Valuables |
| Slot Disable | Disable | A random gear slot stops working | Refresh | Slot Disable |
| Hex | Disable | A random active power slot stops working | Refresh | Hex |
| Numbing Toxin | Disable | A random passive power slot stops working | Refresh | Numbing Toxin |
| Pied | Screen effect (player only) | Smears part of the screen, fading out over its duration | Intensity (each pie adds a smear) | Cream Pie |
| Deathly Rage | Buff | Triples Strength and Toughness | Doesn't stack | Deathly Rage |
| Spotlight | Buff | All stats boosted while inside the spotlight | Lasts while inside | Spotlight |
| Gold-Plated Chrome | Buff | Toughness and Damage Reduction per Valuable held | Intensity (per Valuable) | Gold-Plated Chrome |
| Defiance Roll | Hidden marker | Lowers the Defiance proc chance (`stats.md`) | Intensity (per proc) | Defiance |
| Charmed | Hidden marker | Charming has already rolled on this target | Permanent | Charming |
| Incapacitated | State | At 0 HP. Can't act. Can be Dragged and captured | | 0 HP |
| Dragged | State | Can't be hurt | | Drag |
| Invulnerable | State | Takes no damage | | Defiance, Dash |

- Modules with the `CannotBeDisabled` tag are immune to Disable statuses.

## Open
- Which attacker stat goes into the resist formula?
- Do Disable statuses stack by disabling another slot, or only refresh?
- How does Smoke Bomb's "stunned while inside" work on Leaders, given half-length crowd control?
- Defiance clears all DoTs and debuffs. Should Carrying Treasure and hidden markers survive it?
- Does Invulnerable also block new debuffs?
- What does "dying" mean for Infected? Enemies at 0 HP become Incapacitated rather than dying.
