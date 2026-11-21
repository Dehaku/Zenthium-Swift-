# Story Arcs

- Chains of Story Arc missions that appear on the mission map (`hq.md`).
- An arc can be run by any faction that lists it in its file in `Factions/`. When an arc starts, it picks one of those factions and keeps it until the arc ends. The next time the arc starts, the faction can differ.
- **Arc triggers:** *Random* (the default) or *Milestone*. A milestone arc starts as soon as its condition is met, such as unlocking a rank, and ignores the limit of 2 arcs. If it fails, it comes back with the next mission, guaranteed, until it's been completed once.
- **Starting arcs:** after each mission there's a 10% chance a new random arc starts. At most 2 arcs run at once. The arc is picked at random among eligible ones: its minimum rank is unlocked (`difficulty.md`) and it isn't already running. Each arc can have an optional weight to make it more or less likely.
- **First mission of the game:** the first stage of the Hostile Takeover arc (`StoryArcs/HostileTakeover.md`). Until the first run of Hostile Takeover is finished, win or lose, no normal missions appear and no other arcs start.
- Everything is designer-authored data: arcs, stages, plot sequences, checkpoints and branches. New arcs need no new code.

## Building blocks
| Block | What it is |
|---|---|
| **Arc** | A set of stages linked by branches |
| **Stage** | One Story Arc mission: a mission setup plus its plot sequences, checkpoints and branches. Designers can fix any mission field (type, location, map size, secondary goal, hazards, Leader present, faction); unset fields roll normally. Stages can also override faction settings, such as Champion share. A stage can also place designer-made named entities, such as a VIP or a named villain, in sockets, built from normal modules |
| **Plot Sequence** | A visual-novel style conversation. Characters appear on the left and right of the screen, and their lines show up as they talk. Skippable like mission cutscenes (`missions.md`). The cast and lines are fixed by designers; characters who aren't on the field talk "from HQ". The regulars are the HQ cast (`lore.md`). No dialogue choices. Portraits have a few expressions each, with name plates. Click to advance, or auto-advance as an option. The background is HQ or the field, depending on where the speaker is. Gibberish voice blips instead of voice acting. Lines are faction-neutral by default. Designers can mark a line *(Neutral)* and follow it with faction-specific versions; when that faction is running the stage, its version replaces the neutral line |
| **Checkpoint** | A trigger during a mission and the actions it causes, such as playing a plot sequence, adding a new goal, sending reinforcements or making the Leader try to flee |
| **Branch** | Which stage comes next on success, and which on failure |

- Implementation note: look for a visual novel asset or library to build plot sequences with.

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
- Every arc stage gives +100% rewards, on top of all other bonuses.
- An arc can name an unlock for finishing its final stage: a hero, an extra Recruit slot (room for one more Recruit), or Recruits themselves, the Create-a-Hero system (`heroes.md`).
- If the final stage fails, the arc ends without its unlock. Arcs can come back later.

## Checkpoints
Designers combine any trigger with any actions. Both lists can grow.

| Triggers | Actions |
|---|---|
| Time elapsed | Play a plot sequence |
| The mission timer passes a mark | Add or replace a goal (below) |
| Objective progress reaches a % | Send a reinforcement wave (`enemies.md`) |
| An entity is defeated, or drops to a % of HP | Spawn a specific entity |
| The player enters a tagged area (`maps.md`) | Make the Leader flee |
| A Valuable count is reached (`world.md`) | Apply a mission modifier (`difficulty.md`) |
| A number of citizens are rescued | Add a Meeting Room line (`hq.md`) |
| A secondary goal is completed or failed | Show a tutorial tip |
| | End the mission, as success or failure |
| The Leader escapes | |

### Goals
Goal types a checkpoint can add. The list can grow.
- Recover an item.
- Defeat or capture a named entity.
- Stop an entity from escaping.
- Escort or rescue a named entity.
- Hold an area.
- Survive for a time.

Each added goal is either **required** (failing it fails the mission) or **optional** (it works like a secondary goal and gives a bonus).


## Arcs
Each arc has its own file in `StoryArcs/`. Start new arcs from `StoryArcs/_Template.md`.
- `StoryArcs/HostileTakeover.md` (the opening arc)
- `StoryArcs/Headhunted.md` (unlocks Recruits)
- `StoryArcs/RelicFever.md`

## Open
- How the story is told overall, and whether arcs build toward anything bigger.
