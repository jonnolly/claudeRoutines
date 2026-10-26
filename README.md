# claudeRoutines

State and memory for John's scheduled Claude routines.

## Daily AI tip routine
Fires each morning alongside the email review. Contract:

1. Read `PROFILE.md` — who John is and how he actually uses Claude.
2. Read `TIPS_LOG.md` — never repeat a tip; continue the planned series.
3. Read `QUESTION_BACKLOG.md` — ask the top 2–3 `OPEN`/unanswered questions; fold answers back
   into `PROFILE.md` and mark them `ANSWERED`.
4. Refresh `RESEARCH_NOTES.md` about weekly, not daily.
5. Write the day's brief to `briefs/YYYY-MM-DD.md`, log it, commit, push, and send the tip as a
   push notification (that notification is the delivery — nothing else reaches John).

### Hard rules
- **≤15 minutes of John's time per day, total** (tip + questions). Output that earns money beats
  workflow polish; the tip must be an action, not reading.
- **Never create routines, cron jobs, or TickTick tasks for John.** Suggest them in the brief and
  let him schedule them himself at a time that doesn't collide with value-adding work.
- Tailor to the evidence in `PROFILE.md`. A generic tip is a failed tip.
