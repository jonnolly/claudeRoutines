# Profile — how John works and uses AI

Last updated: 2026-11-16 (run 1 — built from observed data, **not yet confirmed by John**)
Confidence key: `[OBS]` observed in data · `[INF]` inferred · `[ASK]` needs confirming (see QUESTIONS.md)

## Situation

- `[OBS]` Developer on the software team at **New Electric** (newelectric.nl, NL — electric propulsion).
  Colleagues seen in mail: Frank de Boer, Rogier van Rooijen, Adarsha BN, Sam Peach, Shahbaz M.
- `[OBS]` **A "New Workflow" rollout is live right now at work.** Frank mailed dev-env + workflow docs on
  2026-11-02 ("New workflow, new collegue", mentions a "devdock") and again 2026-11-16
  ("New Workflow — What happened in the last 2 weeks"). He asked people to read carefully and write down questions.
  → This is the highest-leverage place for AI workflow improvements to land *at work* in the next few weeks.
- `[OBS]` Simultaneously a **first-year jazz student at Zuyd** (trumpet/piano). Commutes by train.
  TickTick shows school logistics dominating completed tasks (pack bag, train, Focusmate, log piano Beeminder).
- `[OBS]` Stated priority: **money-generating output beats workflow polish.** Budget for workflow work: <=15 min/day.
- `[OBS]` Anthropic subscription is expensed through the company (receipt forwarded to Shahbaz).

## Money / goals context

- `[OBS]` TickTick `Remote Work` project: Upwork / Toptal / Proxify / Codementor / Wyzant profiles,
  "apply for 1 upwork post", "buy upwork connects". **Created 2025-10, untouched since.** Stalled ~13 months.
- `[OBS]` TickTick `Trace Trimmer`: a real tool he built (trims CAN-bus trace logs; handles "insight can
  converter" file formats, unix timestamps in filenames). 7 open items, **last touched 2025-10-22.** Stalled.
- `[OBS]` Goal system is mature: weekly goal review (Wed, 10-min inbox-zero timebox), monthly→30-year goal
  reviews, "My Amazing Life" entries, Trading212 pies per instrument (grand piano, Nord Stage, double bass),
  emergency-fund target €3000 @ €100/mo, Beeminder for piano, Anki, Focusmate, Obsidian.
- `[OBS]` A `Claude questions` TickTick project exists (currently 1 item: retirement-fund tactics).
  He already treats Claude as an advisor, not only a coder.

## How he uses Claude today (observed)

| Evidence | What it tells us |
| --- | --- |
| `[OBS]` This `claudeRoutines` repo + a scheduled "email review" routine | **Already ahead of the curve on cloud routines.** Most people never automate a recurring question. |
| `[OBS]` MCP connected: Gmail, TickTick, Atlassian, GitHub | Uses Claude across tools, not just in a code editor. |
| `[OBS]` `@claude` tag on TickTick tasks (`Remote Work`) | Has an intake habit for delegating to Claude — but the tagged tasks are a year old, so the loop never closes. |
| `[OBS]` Trace Trimmer task bodies are written as prompts, e.g. *"Make a rule that will definitely see whenever I start claude in this folder that the start-time must always be under 1 second. Test this each time you make a change… If you can't you have to let me know"* | He runs Claude Code **in project folders**, and he is **reaching for deterministic enforcement in prose** — the exact job of a `Stop` hook. Big, cheap win. |
| `[OBS]` Subscribes to TLDR, TLDR Dev, TLDR AI — **mostly unread** | Information intake is saturated. He does not need more AI news; he needs one action per day. Tips must be *do this now*, never *read this*. |
| `[INF]` Single long sessions, prose rules in CLAUDE.md, little use of hooks/subagents/worktrees | Working hypothesis driving the first tips. Needs confirming. |

## Working hypotheses about the biggest gaps

1. `[INF]` **No deterministic layer.** Rules live in prose (CLAUDE.md / task text) where the model *may* comply,
   instead of hooks + deny rules where the harness *must*. Directly costs reliability — one of his stated aims.
2. `[INF]` **No independent reviewer.** Same session that writes the code judges it.
3. `[INF]` **No spec-then-fresh-session split**, so stalled projects (Trace Trimmer) have no written "done".
4. `[INF]` **Serial, not parallel.** No worktrees / `/batch` / parallel cloud sessions.
5. `[OBS]` **Intake without a closing loop.** `@claude` tags and backlogs accumulate; nothing is scheduled to drain them.
6. `[OBS]` **Income work is the real bottleneck, not tooling.** Two stalled money projects beat any speed gain.

## Tip-selection rules for this routine

- One tip per day, <=15 minutes to *do*, not to read. Concrete commands/files, not concepts.
- Bias to: reliability (he asks for it), and anything that unblocks **Trace Trimmer** or **remote-work income**.
- Never recommend reading a newsletter or a long article.
- Never create TickTick tasks or routines for him — propose, he schedules.
- Prefer practices he is *not* already doing; he is already strong on routines, goal reviews, and tool delegation.
