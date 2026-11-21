# Zombies

A biological infestation spreading out of Dr. Edd's lab.

Shared faction rules are in `../factions.md`.

## Faction rules
- **Infection:** anything reduced to 0 HP while Infected rises as a zombie on the spot, civilians included (`../statuses.md`).
- **Pandemic** (from rank S): anything reduced to 0 HP rises as a zombie, Infected or not.
- **Risen and hatched zombies** are new Zombie goons. They don't count toward the population cap (`../enemies.md`).
- **Faction tags:** none. Loot goes to Dr. Edd (`../world.md`).
- **Leader behavior:** standard. His goons bring him their loot. Why does he want it? Research.
- **Countdown target:** a horror egg.
- **Comic callouts:** "BRAAAINS!", "GRRAAAH!", "FOR SCIENCE!" (Dr. Edd).
- **Story Arcs:** none yet.

## Entities
| Rank | Entity | Min rank | Description | Modules | Locked until | Tags |
|---|---|---|---|---|---|---|
| Leader | Dr. Edd | D | Tentacled bioweapon gone mad | Outbreak, Engulf, Tentacle Sweep, Meat Slap, Regeneration, Mutate | Outbreak (C), Mutate (A) | |
| Champion | Stalker | D | Half invisible, ranged attacker. Bone Spike is unrelated to the invisibility | Bone Spike, Half-Invisible | | |
| Champion | Breaker | D | Durable; hits break limbs | Smash, Broken Limb, Durability | | |
| Champion | Brood Mother | B | Spawner: lays horror eggs and grabs heroes | Lay Egg, Engulf | | |
| Champion | Abomination | A | Heavy tank | Ram, Durability, Immovable | | |
| Goon | Zombie | D | Slow, infectious and hard to keep down | Bite, Infectious Bite, Turn on Death, Shamble, Undying | | |
| Goon | Spitter | C | Ranged infector | Acid Spit | | |

- Modules are in AI priority order. Locked modules are skipped below their rank (`../factions.md`).
- No entity here has `Coward`: zombies don't run.

## Spawning
- **Arrival:** `Arrival:Sewer` (`../enemies.md`).
- **Champion share:** D 10%, C 20%, B 30%, A and up 40% (tilted toward goons).
- **Budget costs:** Zombie 1, Spitter 2, Stalker 4, Breaker 5, Brood Mother 6, Abomination 8. Dr. Edd is outside the budget.
- **Mission Weight:** Rescue 3, Countdown 2, Invasion 2, Arson Riot 1.
- **Location Weight:** hospitals 3, labs 3, houses 2; everything else 1.

## Open
- Story Arc idea: "Patient Zero", the first outbreak at Blazithion General, ending with Dr. Edd's reveal.
- Numbers for Outbreak, Tentacle Sweep, Meat Slap, Engulf, Regeneration, Bite, Smash, Acid Spit, Lay Egg and Bone Spike, for the numbers pass.
