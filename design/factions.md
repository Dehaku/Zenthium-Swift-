# Villain Factions

Each faction has three ranks:
- **Leader:** a powerful super villain. Innate +200% to all SWIFT stats.
- **Champions:** strong entities with unique capabilities. Innate +100% to all SWIFT stats.
- **Goons:** weak minions, easy to beat in small numbers. No innate boost.

Innate boosts apply before modules. Difficulty adds to them (`difficulty.md`), and each entity has a minimum rank to spawn.

Entity abilities are modules; mechanics live in `modules.md`. A faction can run any Story Arc it lists (`story.md`). Entities scale with mission difficulty (`difficulty.md`).

## Weights
- Any faction can run any mission type.
- **Mission Weight:** how likely a faction is to cause each mission type.
- **Location Weight:** how likely a faction is to hit each kind of location.

## Zombies
Biological infestation.

| Rank | Entity | Description | Modules |
|---|---|---|---|
| Leader | Dr. Edd | Tentacled bioweapon gone mad | Meat Slap, Regeneration, Engulf |
| Champion | Stalker | Half invisible, ranged attacker. Bone Spike is unrelated to the invisibility | Half-Invisible, Bone Spike |
| Champion | Breaker | Durable; hits slow the target | Durability, Broken Limb |
| Goon | Zombie | Slow moving. Victims who die while Infected become zombies | Infectious Bite, Turn on Death |

- **Arrival:** `Arrival:Sewer` (`enemies.md`).
- **Champion share:** default (`enemies.md`).
- **Higher-rank entities:** open (`difficulty.md`).

## Technomafia
Cyberpunk criminal organization with implants.

| Rank | Entity | Description | Modules |
|---|---|---|---|
| Leader | Kingping | "King Ping": mafia don with a chrome body and experimental tech implants. Loots Valuables like a goon, and his goons bring theirs to him | Chrome Body, Gold-Plated Chrome |
| Champion | Tank | Tank treads for a lower body, cannons for arms | Treads, Cannons |
| Champion | Hacker | Deploys turrets; each of its own hits disables a random gear slot. Takes over Heavy Turrets | Turrets, Slot Disable, Reprogram |
| Goon | Mafioso | Every Mafioso has both a machine gun and blade arms | Machine Gun, Blade Arms |

- **Arrival:** `Arrival:Van` (`enemies.md`).
- **Champion share:** default (`enemies.md`).
- **Higher-rank entities:** open (`difficulty.md`).

## Infinity Anarchous
Rogues with random powers and gear who refuse to join any organization. Random modules are drawn from every module, including other factions'.

| Rank | Entity | Description | Modules |
|---|---|---|---|
| Leader | Chad | Superhuman "chill guy" who goes along with his crazed champion friends. Super stats, speed and durability | Super Stats, Super Speed |
| Champion | (varies) | Random powers and gear, super stats | Chad Adjacent, Random |
| Goon | (varies) | One random power or piece of gear each | Random (1) |

- **Arrival:** `Arrival:OnFoot` (`enemies.md`).
- **Champion share:** default (`enemies.md`).
- **Higher-rank entities:** open (`difficulty.md`).

## Galactic Repo Agency
Alien bureaucrats repossessing Earth, one item at a time. Crop circles are placed at random around the map (their source: `lore.md`). Greys Drag citizens into the crop circles, so Rescue missions turn into a race.

- A citizen inside a crop circle is abducted: they disappear for good.
- A hero pulled into a crop circle isn't abducted. It's only an annoyance.
- A crop circle takes all Valuables (`world.md`) off any entity that enters it, the player included. They count as stolen.
- **Crop circles per mission:** 1 at rank D, plus 1 per rank above D.
- **Loot:** Repo entities have `LootDestination:CropCircle`, so they take Valuables to the nearest crop circle instead of to their Leader (`world.md`).
- **Mothership Strike** (from rank S): every 30 s, an orbital beam targets the player's position. A red ring and a countdown from 5 show where it will hit, like Breaching Charge (`modules.md`).
- **Comic callouts:** "PAST DUE!", "REPOSSESSED!", "SIGN HERE!".
- Story Arcs: Relic Fever (`StoryArcs/RelicFever.md`), Hostile Takeover (`StoryArcs/HostileTakeover.md`).

| Rank | Entity | Description | Modules |
|---|---|---|---|
| Leader | GleebPeep | Tired repo officer with a tablet and a ship's tractor beam | Tractor Beam, Repossess, Final Notice, Tablet Slap, Call for Backup |
| Champion | Tractor Drone | Pulls heroes and citizens toward the crop circles | Tractor Pull |
| Champion | Shield Bearer | Armored; can't be knocked back, and blocks shots from the front | Immovable, Energy Blaster, Energy Shield, High-Capacity Battery |
| Champion (from C) | Auditor | Anti-stealth: exposes the player to everyone nearby | Audit, Repossess |
| Champion (from A) | Notary | Support: notarizes nearby allies, making them tougher | Notarized |
| Goon | Grey | Energy blasters; drags citizens away | Energy Blaster, Drag |
| Goon (from B) | Tow Saucer | A small saucer that steals props, citizens and Valuables from range and flies them to a crop circle. Explodes like a motorcycle when destroyed (`world.md`) | Tow Beam |

- **Arrival:** `Arrival:Beam` (`enemies.md`).
- **Champion share:** default (`enemies.md`).
- **Budget costs:** Grey 1, Tow Saucer 2, Tractor Drone 4, Shield Bearer 5, Auditor 5, Notary 6. GleebPeep is outside the budget.
- **Weights:** Mission Weight favors Rescue and Invasion. Location Weight favors banks, museums and parks.
- **Higher-rank entities:** listed in the table with their minimum rank.

## Circus of Calamity
A traveling circus that's also a crime ring.

| Rank | Entity | Description | Modules |
|---|---|---|---|
| Leader | The Ringmaster | Announces each wave like a show. His spotlight buffs every performer near him | Spotlight |
| Champion | Strongman | Grabs citizens, props and goons and throws them at you | Immovable, Drag, Power Throw |
| Champion | Human Cannonball | Launches into you for huge knockback, often into walls | Cannonball Launch |
| Goon | Clown | Throws cream pies | Cream Pie |

- **Arrival:** `Arrival:ClownCar` (`enemies.md`).
- **Champion share:** default (`enemies.md`).
- **Higher-rank entities:** open (`difficulty.md`).

## Hexbound Coven
An overly enthusiastic magic cult that treats every crime as a ritual. Valuables (`world.md`) count as magic items for the Coven.

- While Vex holds Valuables, every Coven entity deals +5% damage per Valuable she holds.
- With no Leader on the mission, there's no power-up. The bonus never carries past the mission.
- Story Arcs: Relic Fever (`StoryArcs/RelicFever.md`).

| Rank | Entity | Description | Modules |
|---|---|---|---|
| Leader | Grand Librarian Vex | Steals magic items. Loots Valuables like a goon, and her goons bring theirs to her | TBD |
| Champion | Hexer | Disables heroes' powers | Hex |
| Champion | Summoner | Summons imps | Summon Imps |
| Goon | Acolyte | Carries a fire wand that can set things on fire | Fire Wand |

- **Arrival:** `Arrival:Portal` (`enemies.md`).
- **Champion share:** default (`enemies.md`).
- **Higher-rank entities:** open (`difficulty.md`).

## Zenthium (neutral)
Hostile creatures from Zenthium (`lore.md`) that come through a Zenthium Fissure (`difficulty.md`). They attack everyone.

| Rank | Entity | Description | Modules |
|---|---|---|---|
| Leader | Zen Commander | TBD | TBD |
| Champion | Zen Soldier | TBD | TBD |
| Goon | Zen Creature | TBD | TBD |

## Open
- Design pass on every faction, including its higher-rank entities.
- Attacks for Kingping, Chad and Vex.
- More factions.
