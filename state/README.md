# Morning planner state

Each run publishes a planning form (Artifact) that writes answers to its db (`plans/<id>`, `memory/latest`)
and applies them to Todoist from the page via the Todoist connector.

## Next run checklist
1. Read `plans/2026-W43` and `memory/latest` from the artifact db (ArtifactData).
2. If `status` is `saved-not-applied`, apply `answers.assignments` in Todoist
   (values: mon/tue/wed/thu = 2026-10-19..22, next = 2026-10-26, backlog = remove date, done = complete, keep = no change).
3. Prioritise tasks tied to `memory/latest.outcomes` and `success`; respect `overflow` policy.
4. Never delete, archive or complete without an explicit answer.

## Log
- 2026-10-18 (Sun): week 43 plan form published (artifact CEThmLimsZFPqte8V5QLxk). Awaiting answers.
  Hours: Mon 8, Tue 2, Wed 2 (9-11), Thu 8, Fri off. Week plan for 19-22 Oct not yet completed.
