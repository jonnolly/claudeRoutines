# Morning planning routine state

- Planning artifact: https://claude.ai/artifact/31nhaMtJFkE5MhACouccPa (db docs: `plans/<YYYY-MM-DD>`, `memory/latest`)
- Page applies Todoist changes itself on Save; if `memory/latest.pendingApply` is true, apply `plans/<date>` moves/clears/capture on the next run.
- Week plan: first done-flag is `memory/latest.lastWeekPlan` (ISO week). 2026-W44 plan requested 2026-10-28 (not yet completed).
- Todoist is the source of tasks; nothing is deleted/archived without permission.
