# Modules

"Module" is the code name for active powers, passive powers and gear. Players see the names Powers and Gear.

## Entity model
- Heroes, enemies and civilians are all the same **Entity**.
- Special abilities come entirely from slotted modules. Everything is data-driven.
- Enemies use fixed module lists from the same data.

## Schema
| Field | Notes |
|---|---|
| ID | Unique |
| Category | Base action, Active, Passive, Gear (active or passive). On-hit effects are Passives with an on-hit trigger |
| Tags | See below |
| Triggers | See below |
| Effects | |
| Stat formula | Unique per module. Examples: one stat at 3x; two stats at 2x each; raw Intelligence plus 3x the bonuses from magic gear such as spell books |
| Resources | The resource it spends, or the capacity and regen it grants (`combat.md`) |
| Damage type | Physical, Magic or Energy (`combat.md`) |
| Cooldown | In real seconds (`time.md`) |

- Every module takes 1 slot.
- Gear can have actives, passives or both. Gear actives have their own buttons (`controls.md`).
- Magic modules and items generally use Intelligence and Will; each module decides how.
- **Module tags (examples):** `Melee`, `Ranged`, `Time`, `Buff`, `Debuff`, `Summon`, `Resist:<Stat>`, `KnockbackResistant`, `CannotBeDisabled`, `Telegraph`, `Ignites`, `Extinguish` (`world.md`), `NoRegen:<Resource>` (`combat.md`). Shared tags let modules change secondary stats without hard-coded pairings.
- **Entity tags** go on entities, not modules: `Hackable`, `Coward` (`enemies.md`), `LootDestination:<place>` (`world.md`). See `factions.md`.
- **Triggers (examples):** always-on, on hit, on damage taken, on Defiance proc, on timer, on activation, on approach.
- **Presentation:** every module needs an icon, a visual flash, a sound cue and optional comic callout text ("POW!").

## Module info
- Holding the "more info" button shows the module's formula with live numbers. Values in square brackets are the summed totals of the matching bonuses.
- Format example: `Damage = Strength([Strength])x2 + Gear([GearBonus]), Attack Speed = Finesse([Finesse])x3 + Gear([GearBonus])`

## Buying, tiers and upgrades
- Bought with Zenny at HQ: powers in the Zen Garden, gear in the Research Lab (`hq.md`).
- Tiers are separate modules shown as one, with up and down arrows to cycle through the versions. Higher tiers cost more Gem Zenny (`economy.md`).
- Owned modules can be upgraded.

## Catalog
Defiance is a core Will rule, not a module (`stats.md`). Faction entities are described in `Factions/`. Owner says who carries a module now; any module can also go on presets and Recruits. "Unassigned" modules have no owner yet but are in the pool (for example, for Infinity Anarchous).

| Module | Category | Owner | Tags | Mechanics |
|---|---|---|---|---|
| Kick | Base action | All heroes | `Melee` | 10 damage, 3 s cooldown. Strength scaling, scaling knockback |
| Drag | Base action | All heroes, Grey, Strongman | | Grab a target and pull it behind you. Checks for citizens first, then Valuables (the player picks these up instantly; `world.md`), then Incapacitated (0 HP) enemies, then props (Strength limits in `world.md`). Carries 1 target, +1 per 100 Strength (150 Strength carries 2). You can fight while dragging and aren't slowed, except by Stubborn citizens (`missions.md`). Dragged targets can't be hurt |
| Sprint | Base action | All heroes | | Toggle. +50% move speed, no stamina cost. Enemies and civilians don't sprint |
| Uppercut | Active | Hero | `Melee` | Like Kick, with 5x knockback. Costs 50 Stamina |
| Speed Punch | Active | Hero | `Melee` | Attacks 3x faster than Kick, full Kick damage per hit, no knockback. Meant to be stronger than Kick. Pairs well with time powers |
| Power Throw | Active | Hero | | Uses Strength. Throw anything and anyone you're dragging |
| Time Slow | Active | Hero | `Time` | See `time.md` |
| Time Stop | Active | Recruits only (for now) | `Time` | See `time.md` |
| Super Lucky | Passive | Hero | | Large Luck boost (`luck.md`). Inspired by Domino |
| Deathly Rage | Passive | Any | `Buff` | On Defiance proc, grants the Deathly Rage buff: triples Strength and Toughness; the extra HP is added to current HP too. Does not stack. Lasts until the mission ends |
| Soulful | Passive | Hero | `CannotBeDisabled` | +50% spell damage, 150 Mana, +5 Mana/s |
| High-Capacity Battery | Passive | Hero | `CannotBeDisabled` | 200 Charge, +5 Charge/s |
| Quick-Charge Battery | Passive | Hero | `CannotBeDisabled` | 50 Charge, +20 Charge/s |
| Reaper Battery | Passive | Hero | `CannotBeDisabled`, `NoRegen:Charge` | 100 Charge, no regen. Defeating an enemy refills it to full |
| Sprinter | Passive | Hero | | 100 Stamina, +10 Stamina/s regen. Doubles Sprint's bonus to +100% move speed. Sprinting never costs Stamina; Stamina is spent by other modules |
| Weather the Storm | Passive | Hero | | When hit, spends 5 Stamina (if you have it) for no knockback and 25% less damage from that hit |
| Charming | Passive | Hero | | On approach: 50% chance to turn a Stubborn citizen Scared, 5% chance to convert a goon to your side. A converted goon hands you its Valuables. Each target rolls once; a hidden Charmed debuff marks it |
| Ink Beast | Active | Rune | `Summon` | Summons an ink beast that fights alongside him |
| Glyph Trap | Active | Rune | `Debuff`, `Resist:Will` | Places a glyph. Enemies who step on it are rooted in place |
| Spectrum Bolt | Active | Prism | `Ranged`, `Debuff`, `Resist:Toughness`, `Resist:Will` | Magic bolt that costs Charge. Each cast cycles color: Red implodes, pulling nearby enemies toward the impact and then bursting outward to knock them back; Blue burns (DoT, resisted by Toughness), Purple may stun (resisted by Will) |
| Card Throw | Active | Madame Tarot | `Ranged` | Homing cards that deal Magic damage. Each card has a random effect |
| Mirage | Active | Madame Tarot | | Creates decoys that draw enemy attention, and lowers her Detectability while they last |
| Dash | Active | Hero | | A quick burst of movement in your facing direction. Costs Stamina. Invulnerable during the dash |
| Telekinetic Throw | Active | Hero | | Throw what you're dragging with telekinesis. Uses Will in place of Strength, both for damage and for the prop size you can throw (`world.md`) |
| Goo Punch | Active | Hero | `Melee`, `Debuff`, `Resist:Strength` | A goo punch that splashes, applying Gooed (a slow) to enemies within 3 m |
| Telekinetic Grab | Active | Hero | | Instant Drag at range: grabs a citizen, Valuable, prop or Incapacitated enemy from a distance |
| Shockwave Stomp | Active | Hero | | Knocks back everything around you, sending enemies into walls |
| Ooze Through | Passive | Hero | | Slip through locked doors as a puddle instead of breaking them (`world.md`) |
| Evac Balloon | Gear (active) | Hero | | Attach to a citizen or Incapacitated enemy and it floats them away. Counts as rescued or captured |
| Six-Shooter | Gear (active) | Hero | `Ranged` | Physical damage. Uses 6 Ammo, then reloads |
| Padded Suit | Gear (passive) | Hero | | +30 Armor. A lot early on, not much later |
| Force Spell Tome | Gear (passive) | Hero | | +15 Magic damage on your magic hits |
| Fire Spell Tome | Gear (passive) | Hero | `Debuff`, `Resist:Toughness` | +10 Magic damage on your magic hits, plus Burn: 12 damage over 4 s (`statuses.md`) |
| Electric Spell Tome | Gear (passive) | Hero | | +10 Magic damage on your magic hits, plus a chain that jumps to up to 5 more enemies within 5 m for 5 damage each |
| First Aid Spray | Gear (active) | Hero | | Heals you for 25% of max HP; 20 s cooldown. Used on an Incapacitated citizen, it costs nothing, has no cooldown, and gets them up as Scared |
| Water Cannon | Gear (active) | Hero | `Ranged`, `Extinguish` | A 12 m water jet with intense knockback. Uses Ammo |
| Gel Coat | Active | Hero | `Extinguish` | Coat yourself, an ally, a citizen or a building in goo. Removes Burn and blocks new Burns for a few seconds; a coated building's fire goes out |
| Fireproof Body | Passive | Hero | `Extinguish` | You can't be Burned. Anything you're dragging is put out and can't be Burned |
| Smoke Bomb | Gear (active) | Hero | `Debuff`, `Resist:Toughness` | A smoke cloud that blocks line of sight and resets nearby enemies' awareness bars. Enemies inside are stunned for as long as they stay in it |
| Repulsor Blast | Gear (active) | Hero | `Ranged` | Energy beam that costs Charge, scales with Intelligence, and knocks targets back |
| Grappling Hook | Gear (active) | Hero | | 30 m range. Zip to a wall, or yank an enemy to you |
| Bandolier | Gear (passive) | Hero | | More Ammo capacity and faster reloads for every gun |
| Breaching Charge | Gear (active) | Hero | | Place a charge. A red circle shows its 15 m blast radius and a small red number counts down from 5. Then it explodes for high damage in the area and blows open locked doors and walls |
| Stasis Cuffs | Gear (active) | Hero | | Captures an Incapacitated enemy on the spot, no exit needed |
| Megaphone | Gear (active) | Hero | `Debuff`, `Resist:Toughness` | Turns nearby Stubborn citizens Scared, sends Scared citizens running for the nearest exit, and stuns enemies within 10 m |
| Barrier Shield | Active | Hero | | A 180-degree crescent shield in front of you that blocks projectiles for a few seconds. Costs Mana. Enemies that touch it are knocked back with Kick's force |
| Stealth Suit | Gear (passive) | Hero | | Lowers Detectability, plus a flat +10% dodge chance |
| Energy Shield | Active | Hero | | Like Barrier Shield, but costs Charge instead of Mana |
| Taunt | Active | Hero | `Debuff`, `Resist:Will` | "COME AT ME!" Every enemy that can see you must target you for 4 s and are Marked: they deal 30% less damage and take 25% more damage. While taunting, you take 50% less damage, and every enemy that hits you is knocked back with Kick's force. Long cooldown |
| Express Delivery | Passive | Hero | | +1 Drag capacity for citizens |
| Mind over Matter | Passive | Hero | | Anything you throw or kick (props, Valuables) deals +50% damage. Thrown props take half damage |
| Quick Draw | Passive | Hero | | The first shot after reloading deals double damage |
| Ricochet | Passive | Hero | | Your shots bounce to one more enemy within 5 m for half damage |
| Overclocked | Passive | Hero | | +50% damage while Charge is above 80% |
| Reactive Plating | Passive | Hero | | +5 Armor each time you're hit, up to +50. Resets after 5 s without being hit |
| Sticky Body | Passive | Hero | `Debuff`, `Resist:Strength` | Enemies who hit you in melee get Gooed (`statuses.md`) |
| Absorbent | Passive | Hero | | 25% chance a ranged hit is absorbed: you take the damage, then heal 110% of it |
| Living Ink | Passive | Hero | | Ink Beast summons a second beast |
| Fresh Ink | Passive | Hero | | Each enemy you defeat heals you for 5% of your HP |
| Stacked Deck | Passive | Hero | | Card Throw's random effects are twice as likely to be good ones |
| Crystal Hunger | Passive | Hero | | Zenthium creatures ignore you until you attack them. Each entity defeated within 10 m of you gives a stack of Soul Shard: +5 max Charge per stack, for the rest of the mission |
| Glow Up | Passive | Hero | | Below 50% HP: +50% Magic damage, and Night Time doesn't halve your vision (`difficulty.md`) |
| Second Wind | Passive | Hero | | When Defiance triggers, fully heals you |
| Hex | Active | Hexer, Cyberdoc | `Debuff`, `Resist:Will` | Spell. Disables a random active power slot for 5 s |
| Numbing Toxin | Passive | Cyberdoc | `Debuff`, `Resist:Toughness` | On hit: poison. Disables a random passive power slot for 5 s |
| Meat Slap | Active | Dr. Edd | `Ranged` | Ranged attack |
| Regeneration | Passive | Dr. Edd | | HP regen |
| Engulf | Active | Dr. Edd | `Telegraph` | Grabs and holds the target |
| Bone Spike | Active | Stalker | `Ranged` | Ranged attack |
| Half-Invisible | Passive | Stalker | | 50% transparent. Uses Detectability rules |
| Durability | Passive | Breaker | | 50% Damage Reduction |
| Broken Limb | Passive | Breaker, Kneecapper | `Debuff`, `Resist:Toughness` | On hit: applies Broken Limb, a slow |
| Infectious Bite | Passive | Zombie | `Debuff`, `Resist:Toughness` | On hit: applies Infected, a DoT |
| Turn on Death | Passive | Zombie | | Any entity reduced to 0 HP while Infected rises as a zombie on the spot, civilians included (`statuses.md`) |
| Treads | Passive | Tank | | -10% move speed, +50% HP |
| Cannons | Active | Tank | `Ranged`, `Telegraph` | Ranged attack |
| Turrets | Active | Hacker | `Summon` | Summons Mini Turrets, which are `Hackable` |
| Repossess | Active | GleebPeep, Auditor | `Debuff`, `Resist:Intelligence` | "REPOSSESSED!" Takes a random gear slot for 5 s, applying Slot Disable (`statuses.md`) |
| Final Notice | Active | GleebPeep | `Debuff`, `Resist:Will` | Applies Marked for 6 s: the target deals 30% less damage and takes 25% more damage (`statuses.md`) |
| Tablet Slap | Active | GleebPeep | `Melee` | A melee attack with knockback |
| Call for Backup | Active | GleebPeep | `Summon` | 30 s cooldown. Summons 3-5 goons and 2 Champions, using the faction's arrival tag (`enemies.md`) |
| Audit | Active | Auditor | | Reveals the player to every enemy within 30 m, making them aware at once |
| Notarized | Passive | Notary | `Buff` | Allies within 10 m get +25% Damage Reduction |
| Tow Beam | Active | Tow Saucer, Drone Courier | | Grabs a prop, citizen or Valuable from range and flies it to the entity's loot destination (`world.md`) |
| Reprogram | Active | Hacker | `Resist:Intelligence` | Takes over a target with the `Hackable` tag, such as a Heavy Turret, which then fights for the Hacker's side. Any entity with Reprogram uses it first on a Hackable target in view |
| Heavy Gun | Active | Heavy Turret | `Ranged` | Ranged attack |
| Slot Disable | Passive | Hacker | `Debuff`, `Resist:Intelligence` | On hit: disables a random gear slot for 5 s. Hits from the Hacker's turrets don't count |
| Chrome Body | Passive | Kingping | | 25% Damage Reduction |
| Gold-Plated Chrome | Passive | Kingping | `Buff` | +5% Toughness and +1% Damage Reduction for each Valuable he holds. Each bonus is one source that adds up per Valuable (40 Valuables = +200% Toughness and 40% Damage Reduction) and multiplies with his other sources. The extra HP from Toughness is added to current HP too |
| Gatling Arm | Active | Kingping | `Ranged`, `Telegraph` | A ranged spray |
| Hush Money | Active | Kingping | | Bribes nearby Scared citizens into becoming Stubborn (`missions.md`) |
| Chrome Fist | Active | Kingping | `Melee` | A melee hit with heavy knockback |
| Overdrive | Passive | Kingping | `Buff` | Below 50% HP: +50% damage and move speed |
| Ram | Active | Tank | `Melee`, `Telegraph` | Charges at a target, slamming it into walls |
| Chrome Pipe | Active | Kneecapper | `Melee` | A melee swing with knockback |
| Machine Gun | Active | Mafioso | `Ranged` | Ranged attack |
| Blade Arms | Active | Mafioso | `Melee` | Melee attack |
| Super Stats | Passive | Chad | | +200% to all SWIFT stats |
| Super Speed | Passive | Chad | | +200% base move speed |
| Chad Adjacent | Passive | Infinity Anarchous Champions | | +50% to all SWIFT stats |
| Tractor Beam | Active | GleebPeep | | Beam that pulls in every entity and prop in its path |
| Tractor Pull | Active | Tractor Drone | | Pulls a hero or citizen toward the nearest Repo Agency crop circle (`Factions/GalacticRepoAgency.md`) |
| Immovable | Passive | Shield Bearer, Strongman, Tank | `KnockbackResistant` | Can't be knocked back |
| Energy Blaster | Active | Shield Bearer, Grey | `Ranged` | Ranged attack, Energy damage |
| Spotlight | Active | The Ringmaster | `Buff` | A spotlight with a 20 m radius, centered on him. Circus entities inside get +50% to all stats |
| Cannonball Launch | Active | Human Cannonball | `Melee`, `Telegraph` | Launches at a target for huge knockback |
| Cream Pie | Active | Clown | `Ranged`, `Debuff`, `Resist:Will` | Thrown pie. On hit, applies "Pied": smears part of the player's screen, fading out over 3 s. Pies stack, so many can cover the screen quickly (`statuses.md`) |
| Summon Imps | Active | Summoner | `Summon` | Summons imp entities |
| Fire Wand | Active | Acolyte | `Ranged`, `Ignites` | Magic fire attack |

## Open
- How tiers and upgrades relate: is upgrading a module the same as buying its next tier?
- Tractor Beam: does it pull toward GleebPeep or toward a crop circle?
- The Owner column misses heroes using faction modules (Immovable, Regeneration). Keep it for factions only?
- More numbers: Kick's Strength scaling, Telekinetic Grab range, Evac Balloon and Stasis Cuffs cooldowns, Megaphone radius and stun length, Regeneration rate.
- Numbers for Dash (Stamina cost), Shockwave Stomp, Six-Shooter, Smoke Bomb, Repulsor Blast, Bandolier, Breaching Charge (damage), Barrier Shield (duration, Mana), Stealth Suit (Detectability), Taunt (cooldown), Water Cannon (Ammo, knockback) and Gel Coat (duration).
- Numbers for Ink Beast, Glyph Trap, Spectrum Bolt, Card Throw and Mirage.
- Card Throw's list of random card effects.
