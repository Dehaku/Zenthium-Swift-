# World

## Walls
- Every wall has HP. Materials, weakest to strongest: **Glass**, **Wood**, **Stone**, **Metal**, **Crystalline**.
- Entities knocked back into a wall deal heavy damage to it, and take Light damage themselves, using the stat of whoever knocked them (`balance.md`).
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

| Size | Examples |
|---|---|
| Small | Trash cans, benches. Always breaks when thrown |
| Medium | Dumpsters, motorcycles, light poles |
| Large | Cars, trucks, trees |

- Bigger props need more Strength to Drag, have more HP and hit harder when thrown. Values per size are in `data/props.csv`.
- Pressing Kick while dragging a prop throws it, the same way as launching Valuables. It takes the same damage it deals. If you're also carrying Valuables, the prop goes first; the next Kick launches the Valuables.
- **Vehicles** (cars, trucks, motorcycles) have Armor and Damage Reduction, and explode when destroyed. Values in `data/props.csv`.
- An explosion goes off 1 s after the vehicle is destroyed, with a red ring showing its radius. It hurts everyone, the player and civilians included.

## Buildings
Every building is one object that owns everything in it, so fire, loot and arson rules never have to work anything out from geometry.

| Part | What it is |
|---|---|
| **Building** | The root of a handmade building. Has an ID, its location type (`maps.md`) and its state: unburned, burning or burned out |
| **Interior zones** | One or more boxes, drawn by the designer, that define "inside". An L-shaped building uses two |
| **Walls, doors and windows** | Children of the building. Each belongs to exactly one building |
| **Sockets** | Children of the building: arson, Valuables, citizens, Heavy Turret, Countdown target and so on (`maps.md`) |

- **No shared walls:** neighboring buildings each have their own walls, even where they touch.
- **The building registry:** when a mission's map is assembled from blocks, every building registers with an ID, its location type, its sockets, and its neighbors within 20 m. Mission rules, such as Arson Riot's percentage of burning buildings, count from the registry.

**How the rules use it:**

| Rule | Handled by |
|---|---|
| Burn for everyone and every prop inside | The interior zones keep a live list of who and what is inside, updated as things enter and leave |
| A random wall or door destroyed | The building's own list of walls and doors |
| Enemies never enter burning buildings | Interior zones mark their floor area as part of the building; while it burns, enemy pathfinding treats that area as blocked |
| Arson | Goons ignite from the building's arson sockets |
| Valuables melting at burn-out | One check of the interior zones at burn-out; Valuables are never "owned" by a building, since they move around |
| Fire spreading | The neighbor list built once at assembly; no searching at runtime |

- Implementation note: this is the intended code structure; exact components and names are for the build.

## Fire
- **Buildings** burn as a whole. Each is unburned, burning or burned out.
- **A burning building:** every 5 s, everyone and every prop inside gains a Burn of 20 damage over 4 s (`statuses.md`), and a random wall or door of the building is instantly destroyed. After 60 s it's burned out: blackened, and no longer burning.
- **Valuables in a burning building** survive until it burns out, then melt. Until then, the player can go in after them. Melted Valuables count as lost.
- **Props** burn through the Burn status, which lasts 10x longer on them. A burning vehicle explodes only when its HP reaches 0, but Burn ignores Armor and Damage Reduction (`combat.md`), so it gets there fast.
- **Starting fires:** modules with the `Ignites` tag set buildings and vehicles on fire when they hit them. Burn alone doesn't light buildings. An exploding vehicle sets the vehicles in its blast on fire, but not buildings.
- **Putting fires out:** modules with the `Extinguish` tag put out burning buildings and props, and remove Burn from entities. Examples: Water Cannon, Gel Coat, Fireproof Body (`modules.md`).
- **Spreading** (from rank A, `difficulty.md`): every 15 s, each burning building has a 25% chance to ignite each unburned building within 20 m.
- **Damage type:** set by the source, like any module (Fire Wand and Fire Spell Tome deal Magic).

## Valuables
Generic money bags. They do nothing on their own and don't affect mission rewards. Some factions use them (`Factions/`).

### Placement
- Banks have a vault holding 20-40 Valuables.
- Stores have 5-10.
- Every other building has a 75% chance to hold 1.
- Each civilian has a 10% chance to carry one (below).

### Picking up
- The player picks up Valuables instantly with the Drag button (`modules.md`).
- Other entities take about 5 s per pickup, and any damage taken resets it.
- Goons go after Valuables they have line of sight to, but only while the player is outside their attack range. Attack range is the longest range among their attack modules, so melee goons often loot while ranged goons fight.
- Every faction loots, Zombies included. Zenthium creatures are the exception (`Factions/Zenthium.md`).

### Carrying
- **Carrying Treasure:** a debuff on every entity holding Valuables, the player included. -5% move speed per Valuable, capped at -50%.
- A carrier shows a money bag icon under it, with the number held at the icon's bottom right. Hidden at 0. The icon grows 5% per Valuable, capped at +50%.
- A carrier drops all its Valuables when defeated, with a "KA-CHING!" comic callout.
- The player can press Kick to launch all their Valuables forward instead of kicking. Each bag is a projectile that deals a Kick's worth of damage. Bags fly like knocked-back entities, with a small random spread in distance and direction so they scatter.
- Valuables don't take up Drag capacity.
- Civilians drop theirs when Incapacitated, or while fleeing an enemy that came within their fear range (`missions.md`). Incapacitated citizens start with theirs already dropped beside them.

### Goon behavior
- A goon carrying Valuables that sees no more Valuables takes them to its Leader and hands them over. Entities with a `LootDestination:<place>` tag take them there instead: `CropCircle` (the Repo Agency's, `Factions/GalacticRepoAgency.md`) or `MapEdge`. When something needs a destination with no tag and no Leader, such as Tow Beam, it uses the map edge. Goons carrying Valuables by hand still follow the no-Leader rule below.
- With no Leader on the mission, goons keep their normal behavior while carrying Valuables.

### Valuables secondary goal
See `missions.md` for the goal itself.
- A Valuable counts as lost once it leaves the map, melts in a burned-out building, or reaches a loot destination that counts as lost, such as a Repo Agency crop circle (`Factions/GalacticRepoAgency.md`).
- The HUD shows a counter, such as "Lost 2 / Fail at 5".
- With no Leader, goons try to leave the map with their Valuables.
- Once the Leader holds enough Valuables to fail the goal, the Leader tries to flee the map with them.

## Open
- (none)
