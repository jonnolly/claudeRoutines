# Research notes — what the respected sources currently say
_Refresh roughly weekly; don't re-research from zero every morning._

## Official Anthropic guidance (code.claude.com/docs/en/best-practices, read 2026-10-26)
- Everything follows from one constraint: **context fills up and performance degrades as it fills.**
- **"Give Claude a way to verify its work"** is the lead practice: _"Give Claude a check it can run:
  tests, a build, a screenshot to compare. It's the difference between a session you watch and one
  you walk away from."_ Escalation ladder: in-prompt check → `/goal` condition → **Stop hook**
  (deterministic gate) → verification subagent (second opinion).
- Have Claude **show evidence** (test output, command + result, screenshot), not assert success.
- **Explore → plan → code → commit**; plan mode (`Shift+Tab`, `--permission-mode plan`). Skip planning
  if the diff fits in one sentence.
- **CLAUDE.md**: short, human-readable, only what changes behaviour. Bloat makes Claude ignore rules.
  `/init` to start, `/doctor` to prune. Domain knowledge → **skills**, not CLAUDE.md.
- **Hooks** are deterministic where CLAUDE.md is advisory. Claude can write its own hooks.
- Scale: `claude -p` non-interactive, worktrees, cloud sessions, agent view, `/batch` (5–30 subagents),
  Writer/Reviewer across two sessions, adversarial review subagent before "done".
- Named failure modes: kitchen-sink session, correcting over and over, over-specified CLAUDE.md,
  trust-then-verify gap, infinite exploration.

## Evidence base (for honesty about expected gains)
- **DORA 2026 "ROI of AI-assisted software development"**: J-curve — a dip before gains (one summary
  cites a ~15% dip for ~3 months); ROI runs **through code review**; modeled first-year ROI is
  explicitly uncertain. DORA 2025 + Faros telemetry (10k+ devs): individual output up sharply
  (~98% more PRs merged) while **org delivery metrics stayed flat** → the bottleneck moves downstream.
- **METR RCT**: experienced devs were ~19% *slower* with early-2025 tools while believing they were
  ~20% faster. 2026 follow-up trends positive but not significant. → Trust measured checks, not feel.
- **Harness / loop engineering** is the 2026 framing: `Agent = Model + Harness`; layers =
  tool orchestration, **verification loops**, context & memory, guardrails, observability.
  Common failure mode called out: agents marking work complete without verifying the outcome.
- Treat vendor-blog numbers as leads, not facts.

## Sources
- https://code.claude.com/docs/en/best-practices
- https://ingenire.com/blog/dora-2026-ai-amplifier
- https://www.faros.ai/blog/key-takeaways-from-the-dora-report-2025
- https://valueaddvc.com/blog/ai-coding-productivity-2026-what-metr-github-and-dora-studies-actually-show
- https://addyosmani.com/blog/agent-harness-engineering/
- https://arxiv.org/pdf/2608.21884 (loop engineering)
- https://arxiv.org/html/2609.00006v1 (harness anatomy, 11 systems)
