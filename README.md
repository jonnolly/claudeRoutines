# claudeRoutines

Scheduled Claude routines and their state.

## Daily AI tip (runs with the morning email review)

Gives John one tailored, under-15-minute tip per day on using Claude/AI more effectively — as a
developer, as his own project manager, and occasionally for personal goals. Biased toward what most
improves reliability, speed and time-to-money, and toward things he isn't already doing.

| File | What it holds |
|---|---|
| `profile.md` | What we know about how John actually uses Claude. The basis for tailoring. |
| `backlog.md` | Ranked tip backlog + log of what's been delivered. One per day, each ≤15 min. |
| `questions.md` | Question queue, highest-value first. Only 15-min-answerable ones get asked. |
| `tips/` | The tips as delivered, one file per day. |

### Rules the routine follows

- Under 15 minutes per day. Improving the workflow matters; shipping work that earns money matters more.
- Tips must be things he isn't already doing — hence the question queue.
- **The routine never creates tasks or schedules cron jobs on his behalf.** It suggests; he books them
  himself, at times that don't collide with value-adding work.
