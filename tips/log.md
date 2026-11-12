# Tip log

| # | Date | Tip | Theme | Status |
|---|---|---|---|---|
| 001 | 2026-11-12 | Blind second-Claude review of the diff before approving Alex's push | multi-agent / roles / reliability | delivered |

## Queued (do not repeat; re-rank each run against new answers)
- **Plan-first**: a read-only plan phase before Alex touches a file; plan committed to a file, executed in a fresh session. _Most-cited single practice of 2026; Alex's docs don't mention it._
- **Worktree fan-out** for the `convert-plc-repo` migration across the 11 PLCs pinning divergent library commits — one worktree per repo so parallel agents can't collide. _High value but setup >15 min; queue for a day he has slack, and check his Windows/Docker setup first (Q9)._
- **Continuously-working agents**: cloud routines/background sessions for the long migration; `subscribe_pr_activity`-style watching on Forgejo equivalents.
- **Verification loop**: make `nepkg check all` + `test.sh` a pass/fail the agent must satisfy before it reports done, rather than a thing it reports on.
- **Retrospective habit**: end-of-task "what should have been in `NE_ALEX`?" — turns every correction into permanent team capability.
- **Frank angle**: John has an open invitation (2 Nov email) to send questions/concerns on the new workflow — a chance to get these patterns adopted team-wide rather than personally.
- **Non-work**: Claude for Zuyd theory homework / Dutch vocabulary spaced repetition; only if he says the life track is in scope (Q10).
