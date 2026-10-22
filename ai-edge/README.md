# ai-edge — daily "how to use AI better" drip

Backing store for the scheduled routine *"stay ahead of the curve on AI usage"*.
One tip per day, delivered by push notification at the start of the day so it can be
read during the morning email review.

## Hard rules for the routine (read these every run)

1. **Budget: 15 minutes per day, total.** One tip whose action fits in ~10-12 min,
   plus at most 2-3 calibration questions that take ~1 min each to answer.
   Earning money beats improving workflow — never deliver a tip that costs a whole morning.
2. **Never create tasks, TickTick entries, cron jobs or routines on John's behalf.**
   He schedules his own work. Park proposals in `suggested-routines.md` and name them in the tip.
3. **One tip per day, popped off the top of `tip-backlog.md`.** Re-rank before popping;
   skip anything invalidated by `profile.md`.
4. **Only tell him things he is not already doing.** Check `profile.md` first.
   Evidence beats assumption: look at the actual repos/tasks before claiming a gap.
5. **Ask the highest-value unanswered question**, from the top of `questions.md`.
   Mark it asked. Fold any answers he gave into `profile.md` and re-rank everything.
6. **Stay silent on nothing-to-say days?** No — this routine's whole output *is* the
   notification. But keep it to one notification, under ~1200 characters of body.
7. **Commit every change** to the designated branch so the next run inherits the state.

## Files

| file | purpose |
|---|---|
| `profile.md` | what we know about how John uses Claude/AI, with evidence + his answers |
| `tip-backlog.md` | ranked tip queue; each entry has evidence, a <=15 min action, a source |
| `delivered.md` | log of what was sent, when, and whether it landed |
| `questions.md` | ranked calibration questions; highest value first, asked/answered state |
| `suggested-routines.md` | routines/automations worth scheduling — for John to schedule himself |

## Run order

1. `git pull`, read all five files.
2. Read any new answers (section "Answers" in `profile.md`, or anything he left in the repo).
3. Re-rank `tip-backlog.md` and `questions.md` against the updated profile.
4. Refresh research when the backlog drops below ~7 entries, or every 2 weeks.
5. Pop tip #1 + question #1 (and #2 if both are one-liners). Send one notification.
6. Append to `delivered.md`, mark questions asked, commit, push.
