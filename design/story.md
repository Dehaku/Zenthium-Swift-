# Story Arcs

- Chains of Story Arc missions that appear on the mission map (`hq.md`). They lightly change the map's look and nothing else.
- An arc can be run by any faction that lists it in `factions.md`. When an arc starts, it picks one of those factions and keeps it until the arc ends. The next time the arc starts, the faction can differ.
- **Starting arcs:** after each mission there's a small chance a new arc starts. At most 2 arcs run at once. An arc can require a minimum unlocked rank (`difficulty.md`).
- **First mission of the game:** a Story Arc stage. No other missions appear until it's resolved.
- Everything is designer-authored data: arcs, stages, plot sequences, checkpoints and branches. New arcs need no new code.

## Building blocks
| Block | What it is |
|---|---|
| **Arc** | A set of stages linked by branches |
| **Stage** | One Story Arc mission: a mission setup plus its plot sequences, checkpoints and branches |
| **Plot Sequence** | A visual-novel style conversation. Characters appear on the left and right of the screen, and their lines show up as they talk. Skippable like mission cutscenes (`missions.md`). The cast and lines are fixed by designers; characters who aren't on the field talk "from HQ" |
| **Checkpoint** | A trigger during a mission and the actions it causes, such as playing a plot sequence, adding a new goal, sending reinforcements or making the Leader try to flee |
| **Branch** | Which stage comes next on success, and which on failure |

## Stage flow
1. **On the map:** only one stage per arc is on the map at a time. It takes 10x longer to expire than a normal mission. Expiring counts as failing.
2. **Briefing:** choosing the stage at HQ plays a plot sequence. The player picks the rank, up to their highest unlocked.
3. **Mission start:** establishing text, then the usual camera sequence (`missions.md`), with a plot sequence playing over each pan: quick chatter about the situation.
4. **During the mission:** checkpoints can fire more plot sequences and change the goals.
5. **Success:** a plot sequence with quips and a lead-in to the next stage ("We did it! Now we must..."). Usually leads to the next stage.
6. **Failure** (including expiring): a plot sequence plays. Usually leads to a harder version of the next stage, or a different one entirely. For example, if someone gets kidnapped, the next stage becomes a VIP rescue.

## Rewards
- Each stage gives normal mission rewards. Finishing the arc's final stage gives +50% on top.
- If the final stage fails, the arc ends without the bonus. Arcs can come back later.

## Checkpoints
Designers combine any trigger with any actions. Both lists can grow.

| Triggers | Actions |
|---|---|
| Time elapsed | Play a plot sequence |
| Objective progress reaches a % | Add or replace a goal |
| An entity is defeated, or drops to a % of HP | Send a reinforcement wave (`enemies.md`) |
| The player enters a tagged area (`maps.md`) | Spawn a specific entity |
| A Valuable count is reached (`world.md`) | Make the Leader flee |
| | Apply a mission modifier (`difficulty.md`) |
| | End the mission, as success or failure |


## Arcs

### Relic Fever
A faction steals increasingly valuable magic items. Chain:
1. A monkey's paw, from an antique shop.
2. Pandora's box, from a museum.
3. The Holy Grail, from a private collector's vault.
4. Finale: the Ark of the Covenant.

## Open
- How the story is told overall, and whether arcs build toward anything bigger.
- The chance after each mission that a new arc starts.
