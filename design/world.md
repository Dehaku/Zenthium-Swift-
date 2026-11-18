# World

## Walls
- Every wall has HP. Materials, weakest to strongest: **Glass**, **Wood**, **Stone**, **Metal**, **Crystalline**.
- Entities knocked back into a wall deal heavy damage to it.
- Buildings and props block line of sight (`stats.md`).
- Broken walls leave a gap you can walk and see through.
- **Windows** are small, fragile Glass walls you can see through.

## Doors
- Same materials and HP as walls.
- Unlocked doors open when touched and close when you step away.
- Locked doors must be broken, with modules or knockback.
- Enemies plan their paths as if doors weren't there. But locked doors are solid: an enemy collides with one and can't pass through it. It stops and attacks the door until it breaks, then walks on.

## Heavy Turrets
- Building defenses that appear from rank B (`difficulty.md`).
- Neutral: they attack heroes and enemies, never civilians.
- Follow Champion rules and scaling. Can be destroyed.
- `Hackable`: Reprogram can take one over (`modules.md`).
- Module: Heavy Gun.

## Props
- Cars, dumpsters, lampposts, trees, benches and so on.
- Props block movement and line of sight.
- Like walls, each prop has HP and a material.
- Any prop can be Dragged and Power Thrown (`modules.md`), if you're strong enough:

| Size | Examples | Strength needed | HP | Thrown damage |
|---|---|---|---|---|
| Small | Trash cans, benches | Any | 1 (always breaks when thrown) | 1x Kick |
| Medium | Dumpsters, motorcycles, light poles | 50 | 50 | 2x Kick |
| Large | Cars, trucks, trees | 250 | 100 | 3x Kick |

- Pressing Kick while dragging a prop throws it, the same way as launching Valuables. It takes the same damage it deals.
- **Vehicles** have Armor and explode when destroyed:

| Vehicle | Armor | Damage Reduction | Explosion |
|---|---|---|---|
| Car, truck | 20 | 50% | 500 damage, 15 m radius |
| Motorcycle | 10 | 50% | 250 damage, 15 m radius |

- An explosion goes off 1 s after the vehicle is destroyed, with a red ring showing its radius. It hurts everyone, the player and civilians included.

## Valuables
Generic money bags. They do nothing on their own and don't affect mission rewards. Some factions use them (`factions.md`).

### Placement
- Banks have a vault holding 20-40 Valuables.
- Stores have 5-10.
- Every other building has a 75% chance to hold 1.
- Each civilian has a 10% chance to carry one (below).

### Picking up
- The player picks up Valuables instantly with the Drag button (`modules.md`).
- Other entities take about 5 s per pickup, and any damage taken resets it.
- Goons go after Valuables they have line of sight to, but only while the player is outside their attack range. Attack range is the longest range among their attack modules, so melee goons often loot while ranged goons fight.
- Every faction loots, Zombies included.

### Carrying
- **Carrying Treasure:** a debuff on every entity holding Valuables, the player included. -5% move speed per Valuable, capped at -50%.
- A carrier shows a money bag icon under it, with the number held at the icon's bottom right. Hidden at 0. The icon grows 5% per Valuable, capped at +50%.
- A carrier drops all its Valuables when defeated, with a "KA-CHING!" comic callout.
- The player can press Kick to launch all their Valuables forward instead of kicking. Each bag is a projectile that deals a Kick's worth of damage. Bags fly like knocked-back entities, with a small random spread in distance and direction so they scatter. Luck doesn't affect the spread.
- Valuables don't take up Drag capacity.
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
- (none)
