# John — Claude / AI usage profile

Last updated: 2026-10-29 (first build, from observed evidence)
Maintained by the daily "AI workflow tip" routine. Update on every run when new evidence appears.

## How this was built
No prior stored profile existed. This was inferred from connected systems
(TickTick projects + task content, Gmail metadata) rather than self-report.
Items marked **[assumed]** need confirmation — see `questions.md`.

## Who / context
- Works at **New Electric** (NL) — electric/marine powertrains. Deals with **CAN bus trace logs**
  and diagnostic data.
- Also a **jazz musician**, first year at **Zuyd conservatory** (trumpet / piano / drums projects,
  original music, recordings). Recently moved / started school → **time-poor, term-time**.
- Timezone Europe/Amsterdam (some tasks tagged Europe/Berlin).
- Claude seat **upgraded 2026-10-12**.
- Reads **TLDR newsletter** → already exposed to AI/dev news headlines.

## Active projects where Claude is / could be used
- **Trace Trimmer** — a desktop GUI tool that trims CAN trace files. Real backlog: GUI
  constraints on selectable start/end times, reading end-time from file, "minutes after start"
  input, auto-update popup + File→Update menu, **start-up time must drop from 4s to <1s**,
  detection of "insight can converter" trace format (parse start/end from
  `can_log_[ip]_[startUnix]_[endUnix]` filenames), STARTTIME update when not trimming from
  first entry.
- **Remote work / freelancing push** (the money thread): Upwork (connects bought, "apply for 1
  post"), Toptal, Proxify, Codementor/Wyzant, teaching opportunities, LinkedIn + CV refresh.
  **These tasks have been open and stale since 2025-10-13/14.**
- Admin Power Hours, Goal Reviews, gratitude journal, Obsidian capture, piano practice,
  Dutch vocabulary — a well-developed GTD-ish personal system.

## Observed Claude/AI habits
- **TickTick is the command centre.** ~30 projects, two-way work↔personal inbox routing,
  a dedicated **`🟥Claude questions`** capture project, and an **`@claude` tag** already used
  on tasks he intends to hand to Claude.
- Writes **long, spec-like task descriptions** — e.g. the start-up-time task reads as a prompt,
  including acceptance criteria and "keep trying until you fulfil this requirement".
- Asked, in prose inside a task: *"Make a rule that will definitely see whenever I start claude
  in this folder that the start-time must always be under 1 second. Test this each time you
  make a change."* → He wants **enforced, persistent project rules** but is expressing it as
  a wish inside a ticket rather than as `CLAUDE.md` + a hook.
- Uses **Claude routines** (this one), so has the cloud/web surface.
- No sign yet of: subagents, plan mode discipline, custom slash commands, hooks, git worktrees,
  headless/scripted Claude, spec files in repo. **[assumed — see questions.md]**

## Working hypotheses for tip selection
1. **Reliability > novelty.** His own words ("definitely", "test this each time") say his pain is
   Claude not consistently honouring constraints, not a lack of raw capability.
2. **Money thread is stalled on activation energy**, not on ability. Anything that turns the
   Upwork/teaching backlog into a batch-generated, low-friction output is high value.
3. **Term-time means low time budget.** Tips must be ≤15 min and ideally pay back inside a week.
4. He already has the *habit* infrastructure (tags, capture projects). The gap is **automation
   that consumes it**, not more capture.

## Constraints to respect (stated by him)
- ≤15 minutes per day total.
- Output that earns money beats workflow polish.
- **He creates his own tasks and schedules his own routines.** This routine proposes; it must
  not create TickTick tasks or cron jobs on his behalf.
