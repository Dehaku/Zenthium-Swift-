# Story Arcs

- Chains of Story Arc missions that appear on the mission map (`hq.md`). They lightly change the map's look and nothing else.
- Several arcs can run at once.
- An arc can be run by any faction that lists it in `factions.md`.
- Everything is designer-authored data: arcs, stages, plot sequences, checkpoints and branches. New arcs need no new code.

## Building blocks
| Block | What it is |
|---|---|
| **Arc** | A set of stages linked by branches |
| **Stage** | One Story Arc mission: a mission setup plus its plot sequences, checkpoints and branches |
| **Plot Sequence** | A visual-novel style conversation. Characters appear on the left and right of the screen, and their lines show up as they talk. Skippable like mission cutscenes (`missions.md`) |
| **Checkpoint** | A trigger during a mission and the actions it causes, such as playing a plot sequence, adding a new goal, sending reinforcements or making the Leader try to flee |
| **Branch** | Which stage comes next on success, and which on failure |

## Stage flow
1. **On the map:** only one stage per arc is on the map at a time. It takes 10x longer to expire than a normal mission. Expiring counts as failing.
2. **Briefing:** choosing the stage at HQ plays a plot sequence.
3. **Mission start:** establishing text, then the usual camera sequence (`missions.md`), with a plot sequence playing over each pan: quick chatter about the situation.
4. **During the mission:** checkpoints can fire more plot sequences and change the goals.
5. **Success:** a plot sequence with quips and a lead-in to the next stage ("We did it! Now we must..."). Usually leads to the next stage.
6. **Failure** (including expiring): usually leads to a harder version of the next stage, or a different one entirely. For example, if someone gets kidnapped, the next stage becomes a VIP rescue.

## Arcs

### Relic Fever
A faction steals increasingly valuable magic items. Chain:
1. A monkey's paw, from an antique shop.
2. Pandora's box, from a museum.
3. The Holy Grail, from a private collector's vault.
4. Finale: the Ark of the Covenant.

## Open
- How the story is told overall, and whether arcs build toward anything bigger.
- Does failure also play a plot sequence?
- How do arcs start: how often, how many at once, and are they gated by rank?
- Is an arc's faction picked once when it starts, and kept for every stage?
- Which rank are arc missions played at?
- Arc rewards: normal mission rewards, or a bonus for finishing the arc? What happens when the final stage fails? Can an arc run again later?
- The player picks any hero, so how do plot sequences handle the hero's lines?
- The starting list of checkpoint triggers and actions.
