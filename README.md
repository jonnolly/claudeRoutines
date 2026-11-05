# claudeRoutines

State for the **daily AI-workflow tip** routine (runs with the morning email review).

| File | What it is |
|---|---|
| `profile.md` | How John actually uses Claude — the thing that makes tips tailored. Correct it freely. |
| `tips/backlog.md` | Prioritised tip queue, highest value first. One per day, ≤15 min each. |
| `tips/delivered/` | Already sent — don't repeat these. |
| `questions.md` | Calibration questions, highest-value first. Answers get folded into `profile.md`. |

## How the routine behaves
- One tip per day, ≤15 min, tailored to the current profile.
- Research-backed, with the caveat stated when a source is a blog rather than official docs.
- **Never auto-creates TickTick tasks or Claude routines** — John schedules those himself, at times
  that don't collide with value-adding work.
- Re-ranks the backlog when the profile changes.
