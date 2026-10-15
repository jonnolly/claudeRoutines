# Profile — how John uses Claude / AI

Living document. Updated by the "AI tip of the day" routine. Everything marked
**[inferred]** is a guess from observable data; **[confirmed]** means John told me directly.
Replace inferences with confirmations as answers come in (see `questions.md`).

Last updated: 2026-10-15 (run 1 — first run, no prior state existed)

## Who / context

- John Connolly, based in the Netherlands (Europe/Amsterdam). Email `john@newelectric.nl`.
- Works at **New Electric** — EV / electric drivetrain conversions. **[inferred]**
- **[inferred]** Embedded / tooling developer: works with **CAN bus trace logs**
  (`can_log_<ip>_<startUnix>_<endUnix>`, "insight can converter" files).
- **Also a first-year jazz/music student at Zuyd Conservatorium** ("🥁Zuyd First Year",
  "🎓Starting School / Move", piano practice, solfège, Beeminder-tracked piano).
  Work is part-time / remote around school. **Time is the binding constraint.**
- Stated priority: *"it is more important to generate meaningful output that we can earn
  money with"* than to keep polishing workflow. Hard cap: **15 min/day on this.** **[confirmed]**

## Tooling observed

| Tool | Evidence | Notes |
|---|---|---|
| Claude Code (local folders) | Trace Trimmer task: *"Make a rule that will definitely see whenever I start claude in this folder"* | Runs it per-project on his machine |
| Claude routines (cloud) | This routine; a daily **email review**; a TickTick daily-reset assistant | Already comfortable with scheduled agents |
| TickTick | 30+ projects, GTD-ish, heavy | **Used as a prompt backlog** — writes full Claude prompts into task descriptions |
| Gmail | 2 803 inbox / 654 unread | Daily email review routine exists |
| Jira + Confluence | Atlassian connector attached | Work PM — usage depth unknown |
| GitHub | `jonnolly`, 5 public repos | `jonnolly/clauderoutines` is the routines repo |
| Obsidian | "♦Add to Obsidian" project | Claude already writes research write-ups into TickTick for filing |
| Beeminder | daily piano logging | Quantified-self streak habit |

## How he actually prompts (from his own task text)

Real example he wrote (Trace Trimmer, "reduce start-up time"):

> *"Reduce the start-time to under 1 second. Make a rule that will definitely see whenever
> I start claude in this folder that the start-time must always be under 1 second. Test this
> each time you make a change. If it doesn't fulfill this requirement, you must keep trying
> until you do fulfill this requirement. If you can't you have to let me know and let me know
> the new start-time."*

What this tells us:
- ✅ He instinctively gives **measurable acceptance criteria** and **"keep going until green"** —
  this is the single most important agentic habit and he already has it.
- ✅ He asks for honest reporting on failure.
- ⚠️ He is **re-typing standing rules into every prompt** instead of putting them in a
  `CLAUDE.md` / hook. He is describing CLAUDE.md without knowing it exists. → **Tip #1.**
- ⚠️ Prompts live in TickTick, not in the repo — so the agent can't see the backlog itself.

## Known projects

- **✂ Trace Trimmer** — GUI tool to trim CAN trace files by start/end time. 7 open tasks,
  all written as Claude-ready prompts, **untouched since Oct 2025** → a year of shelf-ready
  agent work sitting idle. Biggest visible "convert workflow into output" opportunity.
- **🟥 Claude questions** — his own project for things to ask Claude. Currently 1 item
  (retirement/investment planning). Confirms he wants Claude for life/finance decisions too.
- **💻 Admin Power Hours**, **💼 Personal↔Work Inbox** — batching rituals already in place.

## Gaps / hypotheses to test (highest leverage first)

1. No per-project `CLAUDE.md` → every session restarts from zero. **[inferred, high confidence]**
2. One Claude at a time; no parallel sessions, no worktrees, no writer/reviewer pattern. **[inferred]**
3. No automated verification gate (tests / Stop hook / `/goal`) → he *is* the verification loop.
4. Backlog lives in TickTick, so unattended runs can't pick work up on their own.
5. Unknown: whether he uses plan mode, subagents, skills, or `claude -p` at all.
