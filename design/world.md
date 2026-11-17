# World

## Walls
- Every wall has HP. Materials, weakest to strongest: **Wood**, **Stone**, **Metal**, **Crystalline**.
- Entities knocked back into a wall deal heavy damage to it.
- Buildings and props block line of sight (`stats.md`).

## Doors
- Same four materials and HP as walls.
- Unlocked doors open when touched and close when you step away.
- Locked doors must be broken, with modules or knockback.
- Enemies pathfind as if doors weren't there. When one touches a locked door, it attacks the door until it breaks.

## Valuables
- Generic money bags placed around the map.
- Goons want them. Picking one up takes about 5 s.
- A goon goes for Valuables only while the player is outside its attack range. Its attack range is the longest range among its attack modules, so melee goons often loot while ranged goons fight.
- A goon carrying Valuables that sees no more Valuables takes them to its Leader and hands them over.
- With no Leader on the mission, goons keep their normal behavior while carrying Valuables.
- During the Valuables secondary goal (`missions.md`):
  - With no Leader, goons try to leave the map with their Valuables instead.
  - Once the Leader holds enough Valuables to fail the goal, the Leader tries to flee the map with them.
- A Valuable counts as stolen once it's carried off the map.
- Any unit carrying Valuables shows a small money bag icon under it, with the number held at the icon's bottom right. Hidden at 0.
- A carrier drops all its Valuables when defeated.
- Valuables do nothing on their own and don't affect mission rewards. Some factions use them (`factions.md`).

## Open
- (none)
