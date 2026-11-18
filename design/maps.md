# Maps

## Generation
- Designers build city blocks and key buildings by hand. Each mission lays them out at random on a street grid.
- Single ground floor only.

## Size
| Size | About | Notes |
|---|---|---|
| Small | 150 x 150 m | |
| Medium | 250 x 250 m (roughly 3 x 3 blocks) | Default |
| Large | 400 x 400 m | |

## Blazithion
- Every mission takes place in the city of Blazithion (`lore.md`).
- The HQ mission map shows Blazithion's real districts (`hq.md`). Each mission's map is built from its district's blocks.

## Districts
| District | Blocks include |
|---|---|
| Downtown | Banks, stores, clubs |
| Industrial | Labs, armories, warehouses |
| Residential | Houses, small shops, parks (trees, benches, ponds) |

- A mission's location decides its district.

## Sockets
- Designers place sockets on blocks and buildings.
- Each socket has tags with weights for what can spawn in it. Example: a vault socket might spawn Valuables or citizens, at whatever odds the designer sets.
- Each mission fills the sockets by its own rules: citizens, Valuables, goons, exit zones, Countdown targets, crop circles.

## Visibility
- Fog of war: the player's line of sight reveals the map. They can see inside buildings through windows, doors and broken walls as they pass.
- Implementation note: if the game is built in Unity, there's already a fog of war asset for this.

## Open
- What decides a mission's map size: random, mission type, difficulty, or the mission creator?
- Which districts hold hospitals, museums, antique shops and collectors' vaults?
