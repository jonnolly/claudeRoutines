# claudeRoutines — daily AI-workflow tip system

State for the "one tailored AI/Claude workflow tip per day, delivered with the morning email
review" routine. This repo is the routine's memory: without it, every run would repeat itself.

## Files

| File | Purpose |
|---|---|
| `profile.md` | How John actually works, inferred from TickTick / Gmail / repos. The basis for tailoring. Correct it freely. |
| `questions.md` | Prioritised question backlog. Highest-value at the top; only sub-minute ones get presented. |
| `tips/backlog.md` | The tip pipeline, tiered and ordered. Each tip is ≤15 minutes to act on. |
| `tips/log.md` | What's already been sent, so nothing repeats. |
| `tips/YYYY-MM-DD.md` | The full text of each day's tip. |
| `research/sources.md` | Authoritative + community sources, and the consensus distilled from them. |

## How each run should work

1. Read `profile.md`, `tips/log.md` and `questions.md` first.
2. Fold any answers John gave into `profile.md`, mark the questions answered, and **reorder
   `tips/backlog.md`** if the answers change priorities.
3. Pick the top `queued` tip that fits what's now known. Write `tips/<date>.md` with concrete,
   evidence-backed steps — cite something from his own repos/tasks where possible.
4. Refresh research periodically (not daily — weekly is enough) and add new tips to the backlog.
5. Send **one** notification: the tip, then at most 2–3 questions answerable in under a minute.
6. Commit and push.

## Non-negotiables for this routine

- **15-minute ceiling per day, total.** Tip plus questions. If it can't be done in the window,
  it doesn't ship today.
- **Output beats process.** Workflow improvement is the means; earning money is the end. When a
  tip and billable work compete, say so and defer the tip.
- **Never schedule anything on John's behalf.** No TickTick tasks, no cron jobs, no routines.
  Suggest, and let him place it at a time that doesn't collide with value-adding work.
- **Tailored or nothing.** Generic "use plan mode" advice is worthless here. Ground every tip in
  observed behaviour from his own systems.
- **No repeats.** Check `tips/log.md` before choosing.
