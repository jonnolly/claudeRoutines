# Morning Run-Through: routine state

Artifact (reuse this URL every day, republish `daily/index.html`): https://claude.ai/artifact/EVKb8eLqeS7XwhmPRcznHq
Answers live in the artifact db, collection `checkins`, doc id = date (YYYY-MM-DD). Read with ArtifactData `get`/`list`.

## Daily procedure
1. Read yesterday's `checkins/<date>` doc. If missing, treat as "leave everything as is" and say so on the new page.
2. Apply approved answers only:
   - `overdueChoice` per group: keep = no change; split = p1/p2 to this week, rest next Monday; week = spread over this week; next = next Monday; review = list those tasks one by one on the new page.
   - Use `reschedule-tasks` for Todoist (keeps recurrence). Never delete, complete, archive or hide anything.
   - Tasks in `todayPicked` not completed carry over to the top of the next page. `todayDeclined` suggestions are not re-suggested as pre-ticked for 3 days.
   - `pinned` items stay at the top until they have happened. If `samStep1Done` is false, surface TickTick "Decide what to ask Sam" before the Thu 15 Oct conversation.
   - `capacity`/`energy` set how many picks to pre-tick. `nextLength` sets page length. `freeText` and `mustNotSlip`: act on or carry forward.
3. Re-pull Todoist (find-tasks-by-date, overdue) and TickTick (list_undone_tasks_by_time_query) and rebuild the page data, keep a manageable shortlist (<= capacity) and group the overdue rest.
4. Republish the same file path, then send a PushNotification.

## Log
- 2026-10-12: first run. Page published, no answers yet. Group ids: ci, hx70, cat, house.
