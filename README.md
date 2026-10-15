# claudeRoutines

Persistent state for John's Claude routines. The cloud container is wiped between runs,
so anything a routine needs to remember has to live here, committed.

## ai-coach/ — "AI tip of the day"

Feeds one tailored tip per day into the morning email review.

| File | What it's for |
|---|---|
| `ai-coach/profile.md` | What we know about how John works and uses Claude. Inferences are marked; confirmations replace them. |
| `ai-coach/questions.md` | Ranked backlog of questions for John. Highest-value at the top, max 2 asked per day, each answerable inside the 15-minute window. |
| `ai-coach/tips/library.md` | Researched, ranked, sourced tip candidates with effort estimates and status. |
| `ai-coach/tips/log.md` | What was actually sent, and whether it stuck. |

### How a run should go

1. Read `profile.md`, `questions.md`, `tips/log.md`.
2. Fold any answers John gave since the last run into `profile.md`; move those questions to Answered.
3. Pick the top `queued` tip that still fits the profile. Re-rank if an answer changed things.
4. Send **one** tip + **at most two** questions, total ≤ 15 minutes of John's time.
5. Update `log.md` and `questions.md`, commit, push.

### Standing constraints

- **≤15 minutes a day.** Shipping paid work beats polishing workflow.
- **The routine never creates tasks or schedules routines.** If a tip implies one, say so
  and let John add and time it himself so it doesn't collide with value-adding work.
- Tips must be things he isn't already doing, and must be grounded in a real source
  or in observed evidence about his own workflow — not generic advice.
