# Story Arcs

- Chains of Story Arc missions that appear on the mission map (`hq.md`). They lightly change the map's look and nothing else.
- An arc can be run by any faction that lists it in `factions.md`. When an arc starts, it picks one of those factions and keeps it until the arc ends. The next time the arc starts, the faction can differ.
- **Starting arcs:** after each mission there's a 10% chance a new arc starts. At most 2 arcs run at once. An arc can require a minimum unlocked rank (`difficulty.md`).
- **First mission of the game:** a Story Arc stage. No other missions appear until it's resolved.
- Everything is designer-authored data: arcs, stages, plot sequences, checkpoints and branches. New arcs need no new code.

## Building blocks
| Block | What it is |
|---|---|
| **Arc** | A set of stages linked by branches |
| **Stage** | One Story Arc mission: a mission setup plus its plot sequences, checkpoints and branches. Designers can fix any mission field (type, location, map size, secondary goal, hazards, Leader present, faction); unset fields roll normally. A stage can also place designer-made named entities, such as a VIP or a named villain, in sockets, built from normal modules |
| **Plot Sequence** | A visual-novel style conversation. Characters appear on the left and right of the screen, and their lines show up as they talk. Skippable like mission cutscenes (`missions.md`). The cast and lines are fixed by designers; characters who aren't on the field talk "from HQ". The regulars are the HQ cast (`lore.md`). No dialogue choices |
| **Checkpoint** | A trigger during a mission and the actions it causes, such as playing a plot sequence, adding a new goal, sending reinforcements or making the Leader try to flee |
| **Branch** | Which stage comes next on success, and which on failure |

## Stage flow
1. **On the map:** only one stage per arc is on the map at a time, shown with a comic-book cover icon and the arc's title. It lasts 600 s (normal missions last 60 s, `hq.md`), and its timer pauses while the player is in a mission. Expiring counts as failing.
2. **Briefing:** choosing the stage at HQ plays a plot sequence. The player picks the rank, up to their highest unlocked.
3. **Mission start:** establishing text, then the usual camera sequence (`missions.md`), with a plot sequence playing over each pan: quick chatter about the situation.
4. **During the mission:** checkpoints can fire more plot sequences and change the goals.
5. **Success:** a plot sequence with quips and a lead-in to the next stage ("We did it! Now we must..."). Usually leads to the next stage.
6. **Failure** (including expiring): a plot sequence plays. Usually leads to a harder version of the next stage, or a different one entirely. For example, if someone gets kidnapped, the next stage becomes a VIP rescue.

## Stage rules
- **Faction:** one per stage. A designer can set it per stage; otherwise it's the arc's locked faction.
- **Intel:** all of a stage's intel is hidden, with no hidden-intel bonus.
- **Hazards:** never rolled. Only designers set them.
- The mission creator can't make arc stages. Arc stages count toward rank unlocks (`difficulty.md`).

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
A faction steals increasingly powerful magic relics.

- **Factions:** Hexbound Coven or Galactic Repo Agency.
- **Minimum rank:** C.
- **Relics** are named Valuables placed by the stage: carried, dropped and stolen like any Valuable (`world.md`).

| # | Stage | Mission | Location | Fixed fields | Checkpoints | Success | Failure |
|---|---|---|---|---|---|---|---|
| 1 | The Paw | Invasion | Antique shop | Secondary goal: Prevent 50% of Valuables from being stolen. Relic: the Monkey's Paw | An enemy picks up the Paw: plot sequence, and a new goal: recover the Paw | Stage 2 | Stage 2, with Night Time ("They wished for endless night") |
| 2 | Don't Open It | Countdown: the thieves are prying the box open | Museum | Relic: Pandora's Box. Leader present | Timer at 50%: the Leader arrives early, with a plot sequence | Stage 3 | Stage 3, with a Zenthium Fissure ("Something crawled out of the box") |
| 3 | The Collector | Rescue. Named VIP: Lord Pemberton, the collector | Collector's vault (a mansion) | Secondary goal: Prevent 50% of Valuables from being stolen | Pemberton rescued: plot sequence ("They already have the Grail!"), and a named courier carrying the Grail spawns and runs for the map edge. New goal: stop the courier | Stage 4 | Stage 3b |
| 3b | Ransom | Rescue: Pemberton has been kidnapped | Warehouse | Leader present | Pemberton rescued: plot sequence | Stage 4 | Stage 4, with Night Time |
| 4 | The Ark (finale) | Invasion | Warehouse ("government storage, don't ask") | Leader present. Map size: Large | The Leader drops to 50% HP: plot sequence, and the Leader flees with the Ark. If the Leader escapes, the mission fails | Arc complete (+50% rewards) | Arc ends |

#### Sample plot sequences
**Stage 1 briefing**
> **Seria:** Ooh, an antique shop break-in! Somebody's after the Monkey's Paw!
> **Tia:** A cursed relic. It grants wishes, at a cost. No one should use it.
> **Shera:** Then go keep it in its dusty little box. Quietly, Brats.

**Stage 1 success**
> **Seria:** Paw secured! ...Can I make just one tiny wish?
> **Tia:** No.
> **Shera:** They'll go for the museum next, I expect. Pandora's box. Try not to open it.

**Stage 1 failure**
> **Tia:** They used the Paw. Their wish: endless night over the museum district.
> **Shera:** How dramatic. Bring a flashlight.

**Finale success**
> **Shera:** The Ark stays where it is. Good. I'd hate to redecorate.

**Finale failure**
> **Seria:** They got away with the Ark!
> **Shera:** Then they'll be back. Thieves always come back for more.

## Open
- Relic Fever can be run by two factions. Do its plot sequences need a version per faction, or should the lines stay faction-neutral like the samples?
- How the story is told overall, and whether arcs build toward anything bigger.
