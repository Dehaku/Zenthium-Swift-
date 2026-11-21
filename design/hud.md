# HUD

Hybrid layout: vitals and resources stay near the character; abilities and objectives sit on the screen edges. Rules for each element live in the file named; this file says where and how it's shown.

## Near the player
- Health bar, with the effective Defiance chance beside it (`stats.md`).
- Resource bars under the player: Stamina, Mana, Charge, Ammo (`combat.md`).
- The player's status row beside the health bar, with timers (`statuses.md`).

## Ability bar (bottom center)
- The 4 active power slots, with their key or button (`controls.md`).
- The 4 gear actives, plus Kick and Drag.
- Passive slots as small icons beside it.
- Cooldowns show as a sweeping overlay. A slot you can't afford is tinted. A disabled slot (Hex, Numbing Toxin, Slot Disable) is crossed out.

## Objective tracker (top right)
- Mission type and goal, with its live number: a timer for Countdown, "Rescued 4 / 12 (need 3)" for Rescue, a loss timer bar for Invasion, "% burned / fail at" for Arson Riot (`missions.md`).
- Below it: the secondary goal, including the Valuables counter ("Lost 2 / Fail at 5", `world.md`), and icons for active Hazards (`difficulty.md`).

## Screen edges
- **Edge arrows:** icons at the screen edge point to off-screen things: the objective, the nearest exit, the Leader, incoming reinforcements. No distances.
- **No map** for now. Fog of war (`maps.md`) and edge arrows do the job.

## Enemies
- Goons and Champions show a small health bar once damaged.
- Leaders get a big bar with their name across the top of the screen, appearing at their entrance (`enemies.md`).

## Feedback
- **Damage numbers:** comic-style floating numbers, bigger and bolder for big hits. Toggle in the options menu.
- **Warning banners:** short comic banners for big moments, such as "REINFORCEMENTS INCOMING!", "THE LEADER HAS ARRIVED!" and "A FISSURE IS OPENING!".

## In-world indicators
| Indicator | Defined in |
|---|---|
| Status icons and comic callouts above heads | `statuses.md` |
| Awareness bar, "!" and grey alert circle over enemies | `stats.md`, `enemies.md` |
| Money bag icon and count under carriers | `world.md` |
| Red rings and countdowns: Breaching Charge, vehicle explosions, drop-in areas | `modules.md`, `world.md`, `enemies.md` |
| Telegraph red flash | `enemies.md` |
| Pied screen smear | `modules.md` |
| "Skipping" with a growing circle | `missions.md` |
| Module formula breakdown while holding "more info" | `modules.md` |
| Drawn-module icons above Infinity Anarchous entities and Leaders' random extras | `factions.md` |
| Hackable icon on `Hackable` entities, shown only if the player has a module that can hack (such as Reprogram) | `modules.md` |

## End-of-mission screen
- A comic-panel results page: success or failure, Zenny earned by family, multipliers (hero bonus, rank, hidden intel), secondary goal results, and Valuables recovered or lost.
- Zenny is only awarded here, never picked up mid-mission. Crystals fly in from the screen edges into each family's Zenny count, making it grow. Bigger rewards show as bigger crystals (`economy.md`).

## Options menu
- HUD scale.
- Colorblind-safe colors for red rings and alerts.
- Pied smear intensity.
- Screen shake intensity.
- Damage numbers on or off.
- Population cap (`enemies.md`).

## Open
- (none)
