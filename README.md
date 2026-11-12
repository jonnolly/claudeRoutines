# claudeRoutines

Working memory for the **"AI workflow tip of the day"** routine (runs with the morning email review).

| File | What it holds |
|---|---|
| `profile.md` | What we know about how John works and how he uses Claude/AI. The routine reads this first and tailors every tip to it. |
| `questions.md` | Ranked backlog of questions for John. Only the ones answerable inside the 15-min morning window get surfaced. Answers get folded into `profile.md`. |
| `tips/log.md` | Every tip delivered, with date and status. Prevents repeats and tracks what actually stuck. |
| `tips/YYYY-MM-DD.md` | The full text of each day's tip. |

## Rules for the routine
1. **Budget: 15 minutes/day total**, tip + questions included. Workflow improvement is secondary to shipping paid work.
2. **Never schedule anything for John.** No cron jobs, no TickTick tasks, no calendar entries. Suggest; he adds and times them himself so they don't collide with value-adding work.
3. One tip per day. It must be something he is **not already doing**, and it must be actionable in well under the daily budget.
4. Prefer tips that improve reliability/throughput on **paid work** over tips that are merely interesting.
5. Update `profile.md` whenever he answers a question; re-rank `questions.md` each run.
