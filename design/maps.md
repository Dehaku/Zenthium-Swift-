# Maps

## Generation
- Designers build city blocks and key buildings by hand. Each mission lays them out at random on a street grid.
- Single ground floor only.

## Size
| Size | About |
|---|---|
| Small | 150 x 150 m |
| Medium | 250 x 250 m (roughly 3 x 3 blocks) |
| Large | 400 x 400 m |

- Difficulty sets the size (`difficulty.md`). The mission creator can override it (`hq.md`).

## Blazithion
- Every mission takes place in the city of Blazithion (`lore.md`).
- The HQ mission map shows Blazithion's real districts (`hq.md`). Each mission's map is built from its district's blocks.

## Districts
| District | Blocks include |
|---|---|
| Downtown | Banks, stores, clubs, hospitals, museums, libraries |
| Industrial | Labs, armories, warehouses |
| Residential | Houses, small shops, antique shops, mansions (such as a collector's vault), parks (trees, benches, ponds) |

- A mission's location decides its district.

## Sockets
- Designers place sockets on blocks and buildings.
- Each socket has tags with weights for what can spawn in it. Example: a vault socket might spawn Valuables or citizens, at whatever odds the designer sets.
- Each mission fills the sockets by its own rules: citizens, Valuables, goons, exit zones, Countdown targets, crop circles.

## Visibility
- Fog of war: the player's line of sight reveals the map. They can see inside buildings through windows, doors and broken walls as they pass.
- Implementation note: if the game is built in Unity, there's already a fog of war asset for this.

## Open
- One master list of location names, for Location Weight and arc stages. It needs apartment buildings, a records office and SWIFT Tower (from Hostile Takeover).
