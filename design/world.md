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
- Generic money bags placed around the map.
- Goons go after Valuables they have line of sight to. Picking one up takes about 5 s.
- A goon goes for Valuables only while the player is outside its attack range. Its attack range is the longest range among its attack modules, so melee goons often loot while ranged goons fight.
- A goon carrying Valuables that sees no more Valuables takes them to its Leader and hands them over.
- With no Leader on the mission, goons keep their normal behavior while carrying Valuables.
- During the Valuables secondary goal (`missions.md`):
  - With no Leader, goons try to leave the map with their Valuables instead.
  - Once the Leader holds enough Valuables to fail the goal, the Leader tries to flee the map with them.
- A Valuable counts as stolen once it's carried off the map.
- Any entity carrying Valuables shows a small money bag icon under it, with the number held at the icon's bottom right. Hidden at 0.
- A carrier drops all its Valuables when defeated.
- **Carrying Treasure:** a debuff on goons holding Valuables. -5% move speed per Valuable, capped at -50%.
- **Civilians:** each has a 10% chance to carry a Valuable. They drop it when Incapacitated, or while fleeing a goon that came within their fear range (`missions.md`). Incapacitated citizens start with theirs already dropped beside them.
- Valuables do nothing on their own and don't affect mission rewards. Some factions use them (`factions.md`).

## Open
- Does the money bag icon show over civilians carrying a Valuable, or is theirs a hidden surprise?
