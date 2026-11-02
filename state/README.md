# Daily planner state (read this first on every run)

- Artifact (db holds answers): https://claude.ai/artifact/WSoZeK8J7st1yPNiX19BMn
- Answers live in the artifact db: `sessions/<YYYY-MM-DD>` and `memory/latest` (read with ArtifactData).
  `status` = `applied` (page already wrote to Todoist) or `pending` (apply it yourself on the next run).
- Page applies changes itself via the Todoist connector (reschedule-tasks / update-tasks / add-tasks). Nothing is ever deleted, archived or completed.
- Schedule: Mon full day, Tue 2h, Wed 09-11, Thu full day, Fri off. Monday (or the first run of a week with no week-plan session) = full week plan.
- Run log:
  - 2026-11-02 (Mon): week plan page published, awaiting answers. Todoist overdue: 5 items; ~150 undated backlog tasks untouched. Only first 200 undated tasks were listed; sweep other pages next time.
