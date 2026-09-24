# claudeRoutines

State for the **daily AI-leverage tip** routine: one tailored tip each morning, in the
email-review slot, on using AI more effectively — kept under 15 minutes a day.

## Layout

| Path | What it holds |
|---|---|
| `profile/user-profile.md` | What the routine knows about how John works and uses Claude. Evidence-tagged. |
| `profile/open-questions.md` | Ranked question bank. Highest value-per-second surfaces first; big ones stay parked. |
| `profile/tips-log.md` | Every tip delivered, so none repeat and each builds on the last. |
| `research/practice-library.md` | The ranked pool of techniques tips are drawn from, with sources. |
| `tips/` | The tips themselves, one dated file each. |

## Standing rules

1. **≤15 minutes a day**, including answering questions.
2. **Output beats polish.** Prefer techniques that close a correctness loop or move revenue.
3. **John schedules his own work.** The routine proposes; it never creates crons or tasks for him.
4. **One tip a day**, escalating in sophistication as earlier tips land.
5. **Answers get written back** into `profile/` so each run is better targeted than the last.
