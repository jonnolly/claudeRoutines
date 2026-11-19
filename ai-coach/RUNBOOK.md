# AI Coach — daily runbook

Purpose: each weekday morning, deliver **one** tailored tip on using AI/Claude more
effectively, plus **1–3 questions** that fill gaps in the profile. Hard budget:
**15 minutes total of John's time**, including any action the tip suggests.

Priority order when in doubt: *money-making output > workflow improvement*. A tip that
costs more than ~10 minutes to try gets split or dropped.

## Each run, in order

1. Read `profile.md` (what we know), `delivered-log.md` (what's been sent, what he answered).
2. If the previous run asked questions and answers have arrived (push-notification reply,
   a note in this repo, or a TickTick item in `🟥Claude questions`), fold them into
   `profile.md` and **re-rank** `tips-backlog.md` — answers are the main re-ranking signal.
3. Pick the top undelivered tip whose preconditions are met (see `Blocked-by` on each tip).
   Re-rank rather than going down the list blindly: pick what is highest value *given what
   we now know*. If nothing fits, deliver the highest-value question batch alone.
4. Pick 1–3 questions from `questions-backlog.md` — total answer time ≤5 min.
5. Send **one** `PushNotification` with `<routine_summary>`: tip (what / why it fits John /
   the ≤10-min action), then the questions. Phone banner = first sentence, so lead with the tip.
6. Append to `delivered-log.md`, mark the tip `delivered: YYYY-MM-DD`, mark questions `asked`.
7. Commit and push to `claude/blissful-galileo-ls69hm`.

## Rules

- **Never** create TickTick tasks, Claude routines, cron jobs or calendar entries for him.
  He schedules his own follow-ups. Tips may *suggest* "add a task for this" — that's it.
- No tip twice. If a tip was delivered and the profile shows it wasn't adopted, it may be
  re-raised **once**, max 3 weeks later, with a smaller first step.
- Refresh research roughly every 2 weeks (`sources.md` holds what's been read and when);
  he reads TLDR AI / TLDR Dev daily, so a tip that just restates a newsletter headline is
  wasted. Aim for things he is *not* already doing.
- Keep the notification short enough to read on a phone. Detail goes in the email body
  (same `<routine_summary>` text), not in a separate file he has to open.
