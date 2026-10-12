# Daily check-in routine: state

Artifact: https://claude.ai/artifact/3suYjSRhhR4XxLXHUt7zS1 (db capability; answers saved at doc `checkins/<YYYY-MM-DD>`, read with ArtifactData).
Template source: `daily/checkin-template.html` (update the same artifact URL each day; keep it ~10 min).

## Rules
- Never delete, archive or bury tasks without explicit permission. Only reschedule what the user marked.
- Use reschedule-tasks (never update-tasks for dates; keeps recurrence).
- Max tasks "Today" follows the capacity answer (low 3 / normal 5 / high 8).
- Step each morning: 1) read yesterday's checkin doc, apply picks (today/week) and overdueRule in Todoist, 2) surface unfinished "today" picks first, 3) republish fresh artifact from live Todoist (+TickTick) data, 4) PushNotification the link.

## Log
- 2026-10-12: first run. 36 Todoist tasks (~30 overdue since 28 Sep), 1 TickTick task due. Nothing changed yet. Awaiting answers.
