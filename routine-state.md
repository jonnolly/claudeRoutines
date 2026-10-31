# Daily planning routine: state

Memory for the scheduled daily-plan routine. Update every run.

## Rules from the owner
- Work pattern: Mon full day, Tue 2h, Wed 9-11am, Thu full day, Fri off.
- Max ~15 min per session. Few, manageable tasks per day, but never lose reminders.
- Never delete, archive or bury tasks without permission. "Leave as is" = untouched, and re-show next run.
- Monday = in-depth week plan. If the week plan for a week was not completed, do it on whatever day the run happens.
- After the owner saves answers in the page, they are applied to Todoist immediately (the page does it via the Todoist connector).
- Habits (project "Habits", labels *_streak) are recurring routines: leave alone.

## Plans
| Week | Date run | Artifact | Status |
|------|----------|----------|--------|
| 2026-W45 (Mon 2 - Thu 5 Nov) | Sat 2026-10-31 | https://claude.ai/artifact/FWwDcq4eVUYYqWBSBHj71Y | Published, awaiting answers |

Answers are stored in the artifact's db at doc `plans/2026-W45` (read with ArtifactData: `get`, collection `plans`).
Check `applied` and `answers`. If `answers` exist but `applied` is false, apply them with Todoist reschedule-tasks / add-tasks.

## Next run checklist
1. Read `plans/2026-W45` from the artifact db. If missing, the week plan is not done: remind the owner (push notification) and re-publish if needed.
2. Prioritise: items the owner chose for the current day, then overdue items left as is, then p1 backlog items.
3. Items the owner left alone (choice `keep`) must be re-shown if `reshow` is true.
