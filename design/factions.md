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

## Shared rules
- **Minimum ranks:** every entity has a minimum rank to spawn.
- **Locked modules:** an entity can use all its modules at every rank by default. Its entry can optionally list modules locked until a higher rank, so designers can weaken an entity at low difficulties. The lock belongs to the entity, never the module, so any module works anywhere (Recruits, Infinity Anarchous' random draws).
- An entity's module list is also its AI priority order (`enemies.md`). Locked modules are skipped.
- **Flying** is only a look. Drones and saucers use normal movement and hit rules.
- **Entity tags** such as `Hackable`, `Coward` and `LootDestination:<place>` are listed per entity.

## Faction files
Each faction has its own file in `Factions/`. Start new factions from `Factions/_Template.md`.
- `Factions/Zombies.md`
- `Factions/Technomafia.md`
- `Factions/InfinityAnarchous.md`
- `Factions/GalacticRepoAgency.md`
- `Factions/CircusOfCalamity.md`
- `Factions/HexboundCoven.md`
- `Factions/Zenthium.md` (neutral)

## Open
- Design pass on every faction except the Galactic Repo Agency, following `Factions/_Template.md`.
- More factions.
