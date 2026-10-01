# claudeRoutines

State and runbook for John's scheduled Claude routines.

## Daily AI-leverage tip (routine: "stay ahead of the curve")

**Goal:** one tailored tip per day, delivered with the morning email review. Each tip must be
doable in **≤15 minutes**. Workflow improvement is secondary to shipping work that earns money —
so the bar for a tip is "this pays for itself this week", not "this is interesting".

### Files

| File | Purpose |
|---|---|
| `profile/user-profile.md` | Living picture of how John works and how he uses Claude. **Read first every run.** |
| `profile/open-questions.md` | Ranked question bank. Only surface questions answerable inside the 15-min window. |
| `tips/tip-backlog.md` | Ranked tip backlog + sources. Re-rank when the profile changes. |
| `tips/delivered/` | One file per delivered tip. |
| `tips/log.md` | What was sent when, and whether it stuck. |

### Run procedure

1. Read `profile/user-profile.md` and `tips/log.md`.
2. Pull fresh signal (TickTick recent/completed tasks, this repo, anything he's answered since last run).
   Update the profile with anything new — especially answers to open questions.
3. Pick the **top-ranked ready tip** that still fits his current situation. If his situation changed,
   re-rank first. Refresh research periodically rather than every day.
4. Deliver: the tip, plus **at most 2–3 open questions** (only if they fit the 15 minutes alongside the tip).
5. Write the tip to `tips/delivered/`, update `tips/log.md`, commit, push.

### Standing constraints

- **Never create TickTick tasks, cron jobs, or routines on his behalf.** He adds and schedules those
  himself, so they don't collide with value-adding work. Suggest; don't schedule.
- Keep the total daily ask under 15 minutes, tip + questions combined.
- He is an experienced GTD operator and already queues work for Claude (`@Claudeready` tag,
  "🟥Claude questions" project). Don't pitch fundamentals he's already past.
