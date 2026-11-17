# World

## Walls
- Every wall has HP. Materials, weakest to strongest: **Wood**, **Stone**, **Metal**, **Crystalline**.
- Entities knocked back into a wall deal heavy damage to it.
- Buildings and props block line of sight (`stats.md`).

## Doors
- Same four materials and HP as walls.
- Unlocked doors open when touched and close when you step away.
- Locked doors must be broken, with modules or knockback.
- Enemies plan their paths as if doors weren't there. But locked doors are solid: an enemy collides with one and can't pass through it. It stops and attacks the door until it breaks, then walks on.

## Valuables
Generic money bags. They do nothing on their own and don't affect mission rewards. Some factions use them (`factions.md`).

### Placement
- Banks have a vault holding a lot of Valuables.
- Stores have quite a few.
- Every other building has a small chance to hold one.
- Each civilian has a 10% chance to carry one (below).

### Picking up
- Any entity can pick up Valuables, the player included. A pickup takes about 5 s, and any damage taken resets it.
- Goons go after Valuables they have line of sight to, but only while the player is outside their attack range. Attack range is the longest range among their attack modules, so melee goons often loot while ranged goons fight.
- Every faction loots, Zombies included.

### Carrying
- **Carrying Treasure:** a debuff on every entity holding Valuables, the player included. -5% move speed per Valuable, capped at -50%.
- A carrier shows a money bag icon under it, with the number held at the icon's bottom right. Hidden at 0. The icon grows 5% per Valuable, capped at +50%.
- A carrier drops all its Valuables when defeated, with a "KA-CHING!" comic callout.
- The player can press Kick to launch all their Valuables forward, dropping them.
- Civilians drop theirs when Incapacitated, or while fleeing a goon that came within their fear range (`missions.md`). Incapacitated citizens start with theirs already dropped beside them.

### Goon behavior
- A goon carrying Valuables that sees no more Valuables takes them to its Leader and hands them over.
- With no Leader on the mission, goons keep their normal behavior while carrying Valuables.

### Valuables secondary goal
See `missions.md` for the goal itself.
- A Valuable counts as stolen once it leaves the map.
- The HUD shows a counter, such as "Stolen 2 / Fail at 5".
- With no Leader, goons try to leave the map with their Valuables.
- Once the Leader holds enough Valuables to fail the goal, the Leader tries to flee the map with them.

## Open
- Pickup time for the player: also about 5 s?
- Does Kick still deal damage while launching Valuables, or does it only launch them?
- Numbers: Valuables per bank vault and per store, and the chance per other building.
