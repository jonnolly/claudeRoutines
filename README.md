# claudeRoutines

State for John's Claude routines.

## Daily AI-workflow tip routine

Runs each weekday morning (Europe/Amsterdam) alongside the email review. Each run:

1. Reads `profile.md` — the evidence-based picture of how John actually uses Claude.
2. Picks the top undelivered item from `tips/backlog.md`, re-ranking if new evidence changed
   the priorities, and writes it up in full to `tips/delivered/`.
3. Presents **one** tip plus the top few questions from `questions.md` in a push notification.
4. Folds any answers received into `profile.md` and retires those questions.

### Design constraints (from John, 2026-10-29)
- **≤15 minutes per day.** Tips must be adoptable inside that, and questions must be answerable
  inside it. Anything needing a real sit-down goes to the PARKED section of `questions.md` and is
  never shown in the morning window.
- **Earning beats polishing.** Workflow improvement is the means; revenue-generating output is the
  end. When ranking, money impact outranks elegance.
- **He schedules his own work.** This routine proposes; it must never create TickTick tasks or
  cron jobs on his behalf. Follow-up actions are surfaced as suggestions for him to add himself,
  at times that don't collide with value-adding work.

### Files
| File | Purpose |
| --- | --- |
| `profile.md` | How John uses Claude. Updated as evidence arrives. Assumptions marked `[assumed]`. |
| `tips/backlog.md` | Prioritized tip queue, ranked by impact ÷ minutes-to-adopt. Cites sources. |
| `tips/delivered/` | Full write-up of each delivered tip, dated. |
| `questions.md` | Tailoring questions, highest-value first. Only 15-min-answerable ones get asked. |
