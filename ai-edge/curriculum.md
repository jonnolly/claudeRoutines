# Tip bank — ranked by expected value for John

Scored on: does it move a money thread? is it ≤15 min to adopt? is he not already doing it?
Re-rank each run. Pull from the top; log what was sent in `tips/`.

## Tier 1 — highest leverage (income-moving, he isn't doing it)
1. **Async backlog drain / "Tier 3" agents.** Convert standing TickTick tickets into cloud sessions
   that run while he's in a lesson or on the train; review diffs in the existing admin slot.
   Fits him unusually well: his tickets are already independently scoped with acceptance criteria.
   *(SENT 2026-10-08)*
2. **Acceptance criteria as the delegation unlock.** Anthropic's 2026 report: devs use AI for ~60% of
   work but fully delegate only 0–20%. The gap is verification, not capability. A ticket that states
   how it will be checked is a ticket an agent can finish unattended.
3. **Spec-first / plan mode before any edit.** Read-only exploration → reviewed plan → code. Cited
   across every 2026 guide as the single biggest determinant of agentic output quality.
4. **Skills over re-explaining.** Package the repeat context (Trace Trimmer conventions, CAN trace
   formats, his writing voice for Upwork proposals) as `SKILL.md` files so it loads automatically.
   Progressive disclosure: lean SKILL.md, detail in `references/`.
5. **Turn the stalled Upwork thread into an agent job.** Profile copy, proposal drafting from his CV
   + New Electric work, job-post triage. Pure text work — ideal for delegation, zero terminal needed.

## Tier 2 — strong, adopt once Tier 1 lands
6. **Separate reviewer session.** Never let the agent that wrote the code be the one that approves it.
7. **CLAUDE.md as a project constitution**, kept short (~200 lines); detail pushed into skills.
8. **Context hygiene** — clear/rewind after a failed attempt rather than stacking corrections;
   community heuristic is to wrap up past ~60% context.
9. **Small, revertible commits at logical checkpoints** instead of one large agent-authored rewrite.
10. **Role-specialised subagents**: reviewer, test writer, doc generator, security auditor.
11. **Git worktrees / isolated clones** so parallel agents can't collide on the same files.

## Tier 3 — real but conditional (needs scale or a desk)
12. **Agent teams** — shared task list, dependency tracking, peer messaging, file locking.
    Caveat: expensive (each teammate loads full project context) and reportedly unnecessary for
    ~95% of agent-assisted tasks. Only once there's a genuinely parallel backlog.
13. **Long-running autonomous runs** (the Rakuten 7-hour / 12.5M-line example).
14. **Hooks** for deterministic enforcement (lint/test gates the model can't skip).
15. **Non-engineering automation surfaces** — the report's "coding democratises" trend; relevant to
    his music/teaching admin, not his dev income.

## Personal-development / life-goals angle (use sparingly, he's already strong here)
16. **AI as thinking partner for the "no slot exists" problem** — the recurring failure mode in his
    own task notes is a good task with no home in the week, not a lack of intent.
17. **Transcription & aural-skills drilling support** — the ~27% "work that wouldn't otherwise exist"
    finding applied to practice tooling.

## Sources
- Anthropic, 2026 Agentic Coding Trends Report (via secondary write-ups — figures to verify at source):
  https://tessl.io/blog/8-trends-shaping-software-engineering-in-2026-according-to-anthropics-agentic-coding-report
- Addy Osmani, "The Code Agent Orchestra": https://addyosmani.com/blog/code-agent-orchestra/ (tiering model)
- Warp, multi-agent productivity: https://www.warp.dev/articles/multi-agent-systems-developer-productivity
- VS Code, multi-agent development: https://code.visualstudio.com/blogs/2026/02/05/multi-agent-development
- Claude Code plugins/skills docs: https://code.claude.com/docs/en/plugins
- OpenHands, Claude Code best practices 2026: https://www.openhands.dev/blog/claude-code-best-practices-agentic-coding

## Caveat carried forward
Most 2026 "best practice" writing is vendor blogs without citation counts. Treat specific percentages
as community heuristics unless traced to Anthropic's primary report.
