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
- A goon carrying Valuables shows a small money bag icon under it, with the number stolen at the icon's bottom right. Hidden at 0.
- Some factions use Valuables in their own way (`factions.md`).

## Open
- What happens to stolen Valuables? Do they drop when the goon is defeated, can goons escape with them, and do they affect rewards or fail conditions?
