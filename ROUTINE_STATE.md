# Daily check-in routine state

- Answers are stored by the check-in artifact in its `db`, collection `checkins/<YYYY-MM-DD>` (fields: energy, stars, decisions, laptop, weekNote, tomorrowNote, applied, weekPlanDone).
- Week plan completed for: none yet (first page published 2026-11-05 includes the week-45 plan; `weekPlanDone: "2026-W45"` is written on save).
- 2026-11-05 artifact: https://claude.ai/artifact/X8F47nUBDcfDbF2JSU6sBN
- Next run: read the previous `checkins/*` doc via ArtifactData; apply any decision whose `applied` entry is missing or failed; use `stars` and `tomorrowNote` to prioritise.
- Work pattern: Mon full, Tue 2h, Wed 9-11, Thu full, Fri off.
