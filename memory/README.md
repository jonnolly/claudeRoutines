# Daily planning routine: memory

Owner schedule: Mon full day, Tue 2h, Wed 9-11am, Thu full day, Fri off. Timezone Europe/Amsterdam.
Rules: <=15 min/day, few tasks per day, never delete/archive/bury without permission, bulk questions over per-task ones.
Monday = full week plan. If no week plan was completed for the current week, do one on whichever day it is.

## Every run, in order
1. Read `memory/state.json`. For every artifact with `saved: true` and `applied: false`, read it
   (Artifact action=read), then APPLY its answers to Todoist before building today's page (see mapping), then
   republish that artifact with `state.applied` set to a one-line summary, and update state.json + daily log.
   (Remote sessions cannot be woken by a save, so the next run is where saved answers get applied unless the user is in a live session.)
2. Use previous answers (rows placed on days, cluster choices, stale choices, "must" and "remember" text) to prioritise.
3. Build a new page from the template `memory/day-plan.template.html` (state JSON is in `<script id="state">`), publish, notify.

## Applying a saved page
- rows[].day tue/wed/thu -> set due date 2026-10-27/28/29 on every id in rows[].ids (reschedule-tasks keeps recurrence and time; update-tasks dueString for undated tasks). Set duration from est only if the user changed it. `later` = no change.
- house[].on true: planday -> reschedule 6hq2vc3CW9Q96QvC to 2026-10-29; sendyne9 -> reschedule 6hqwqvq24wcvVCr9 to 2026-10-28T09:00:00.
- stale[].c: mon -> reschedule id to the next Monday; done -> complete; keep -> nothing.
- clusters[].c: memory only (push/normal/park). Never touch Todoist for these. List parked clusters on every page.
- capture lines -> add-tasks in Inbox if addTasks. remember/must -> carry into next page's step 5 prompt.
