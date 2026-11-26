# John — AI/Claude usage profile

Maintained by the daily "AI tip" routine. Updated whenever new signal appears.
Last updated: 2026-11-26 (first build, inferred from TickTick + Gmail — **not yet confirmed by John**)

## Who / context

- John Connolly, Embedded Software Engineer, **New Electric** (Breukelen, NL) — electrification
  retrofits. Project names seen: A45, CAT 330z, Hilux, Fendt, HX90, HBM, BellMarine, CCS Discharge.
- Small team: "effectively act as my own project manager … lots of experience project and task planning."
- **Conservatory student in parallel** — Zuyd, first year (jazz/piano/trumpet), plus a move to Maastricht.
  Wants a WFH day (Monday) to make room for study.
- Second track: music as income/vocation — original music, band plan (chant/affirmation + rhythmic
  acoustic), AIM innovation award (deadline 1 Dec), gigs.
- Income diversification in progress: Upwork / Toptal / Proxify, Codementor or Wyzant teaching.
- **Time is the binding constraint.** Full-time job + first-year conservatory + move. 15 min/day cap on
  workflow improvement is a hard limit, and output that earns money beats workflow polish.

## How he uses Claude today (inferred)

- **Claude Code on a real project**: `Trace Trimmer` — a desktop GUI tool that trims CAN-bus trace
  files (handles "insight can converter" format, unix-timestamp filenames, start/end-time parsing).
  Clearly built and maintained with Claude.
- **Backlog items are written as prompts.** TickTick task descriptions read like pasted Claude
  instructions, e.g. the start-up-time task: *"Reduce the start-time to under 1 second. Make a rule
  that will definitely see whenever I start claude in this folder that the start-time must always be
  under 1 second. Test this each time you make a change. If it doesn't fulfill this requirement, you
  must keep trying until you do fulfill this requirement."*
  → He is **describing CLAUDE.md + a verification hook + a perf test in prose**, without the mechanism.
  This is the single clearest gap and the anchor for the first tips.
- **A `@claude` tag already exists in TickTick** on research-type tasks (remote-work platforms,
  Codementor vs Wyzant, music therapy in Switzerland, trance activities). So an intake queue for
  Claude already exists informally — it is just not drained automatically.
- Uses **Obsidian** (project "♦Add to Obsidian"), TickTick as the system of record, Gmail, and this
  `claudeRoutines` repo for scheduled routines.
- Has at least one scheduled Claude routine (this one) and a goal-review habit ("✨Goal Reviews").
- Pays for Claude (receipts forwarded to Shahbaz at New Electric) — so work-sanctioned.

## Assumed-not-yet-used (the tip pipeline targets these)

Hooks · scoped `.claude/rules/` · skills · subagents for noisy exploration · git worktrees /
parallel agents · `/loop` · permission allowlists · evidence-based completion · fresh-context review.

*(All of this is inference. The checklist in `questions.md` Q1 settles it in two minutes.)*

## Standing constraints for this routine

1. One tip per day, deliverable in **under 15 minutes**, at email-review time.
2. Tailored to his stack: Python/desktop GUI, embedded/CAN, solo-PM, severe time poverty.
3. **Never create TickTick tasks or cron jobs for him.** Suggest; he schedules them himself at
   sensible times so they don't collide with value-adding work.
4. Bias to tips that increase reliability of unattended work and shorten time-to-money.
