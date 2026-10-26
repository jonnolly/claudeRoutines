# Daily planning routine: memory

Each run publishes a plan page (Artifact) and the page saves John's answers to its own db
collection `daily/<YYYY-MM-DD>` and applies them to Todoist when he presses Save.

At the start of each run:
1. Read `state/runs.json` for the previous page URL.
2. Read that artifact's `daily` collection with ArtifactData (list). Use the latest answers:
   focus per day, week outcomes, notes for tomorrow, what was moved/done. An entry without
   `appliedAt` means the page was not saved yet; carry its tasks forward and say so.
3. Weekly plan: Monday, or the first run of a week with no `type: "week"` entry saved for that
   ISO week. Other days: short daily page only.
4. Never delete, archive or bury tasks without an explicit choice on the page.
5. Append the new run to `state/runs.json`.

Schedule: works Mon + Thu full days, Tue 2h, Wed 9-11, Fri off.
Todoist ids used: Housekeeping project 6hjgj7wwgR829mh7 (holds the Thursday "Backlog skim" task).
