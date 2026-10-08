# ai-edge — daily AI-workflow tip routine

State for the scheduled routine that gives John one tailored AI-usage tip each morning.

- `profile.md`   — how John works and uses Claude. Read first, update whenever he answers something.
- `curriculum.md`— ranked tip bank from research. Pull from the top; re-rank each run.
- `questions.md` — question backlog. Only the top 1–3 ever get asked, only if answerable in-window.
- `tips/`        — one file per tip sent, dated. **Check this before sending — never repeat a tip.**

## How a run should go
1. Read `profile.md`, `questions.md`, and the filenames in `tips/`.
2. Check TickTick for what's actually moving right now (and whether the last tip was acted on).
3. Pick the highest-value unsent tip that fits his current situation — tailored, not generic.
4. Deliver by `PushNotification` (nobody reads the session), with at most 1–3 questions attached.
5. Write the tip to `tips/YYYY-MM-DD.md`, update the other files, commit, push.

## Hard rules
- ≤15 min of his time per day. Output that earns money beats workflow polish.
- **Never create TickTick tasks, routines or cron jobs for him.** He schedules his own follow-ups.
- Refresh the research periodically — weekly is enough; the field moves but not daily.
