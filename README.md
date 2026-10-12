# claudeRoutines

Working state for John's scheduled Claude routines.

## Daily AI tip routine
Runs each morning alongside the email review. Delivers **one tip + up to two questions**, total
budget **15 minutes** — workflow improvement must never crowd out revenue-generating work.

| Path | Purpose |
|------|---------|
| `profile/usage-profile.md` | What's known about how John uses Claude/AI. Read first, every run. |
| `backlog/tips.md` | Ranked tip backlog. One per day. Re-rank each run on new evidence. |
| `backlog/questions.md` | Ranked questions, with time-to-answer. Top 2 per day, then retired. |
| `daily/YYYY-MM-DD.md` | What actually went out that day. |
| `state.json` | Cursor: last run, tips delivered, questions outstanding. |

### Standing rules for this routine
1. **≤15 min/day total.** A tip must be adoptable in ≤10 min.
2. **Only suggest things John isn't already doing** — check the "NOT to suggest" list in the profile.
3. **Never create tasks or routines on his behalf.** Surface the suggestion; he files and schedules it.
4. **Tailor to evidence**, and cite the evidence (his own tasks, repos, habits) so tips are arguable.
5. Fold every answer back into the profile so the routine compounds instead of restarting.
