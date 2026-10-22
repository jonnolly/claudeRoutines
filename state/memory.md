# Daily planning routine: memory

Artifact (same URL every day, republish `daily-plan.html` with new content): https://claude.ai/artifact/Jps1PwKEqjP4CaVy1DmHAa
Answers are saved by the page into the artifact db: collection `days`, doc id = date (YYYY-MM-DD). Read with ArtifactData (list `days`) at the start of each run.
Page applies changes to Todoist itself on Save (reschedule-tasks, update-tasks, complete-tasks, add-tasks via the Todoist connector). Nothing is deleted or archived without an explicit user choice.

## Schedule
Mon full day, Tue 2h, Wed 9-11am, Thu full day, Fri off. Monday = full week-planning session. If a week plan is not marked done (`weekPlan.done`) in any `days` doc for the current week, run the week plan that day.

## Run log
- 2026-10-22 (Thu, wk 43): first run. No week plan existed, so the page combines today + week plan. Awaiting answers. Defaults: p1 overdue -> today, small p4 -> Mon 26 Oct.

## Next run checklist
1. Read `days/*` docs (latest first); check which decisions were Leave/overdue and what the user said in `notes`, `win`, `weekPlan`.
2. Pull today's Todoist tasks + overdue + top undated p1/p2; surface anything the user left overdue first so it is not buried.
3. Cap tasks by `energy` (full 5, normal 4, low 2). Respect day capacity (see schedule).
4. Rebuild the page from `daily-plan.html` for the new date, republish to the same URL, push notification to user.
