# Sources to keep mining

Checked 2026-09-28.

## Primary (authoritative, check for changes)
- Claude Code docs — agent teams: https://code.claude.com/docs/en/agent-teams
  (experimental, `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`; subagents vs teams comparison;
  3–5 teammates recommended; start with research/review not parallel implementation)
- Claude Code docs index: https://code.claude.com/docs/en/ — sub-agents, skills, hooks,
  worktrees, cross-session-messaging, permission-modes, costs
- Anthropic / Claude blog: https://claude.com/blog

## Current developments (Sep 2026)
- **Claude Code Projects** (beta from 2026-09-17): coordinator chat splits a goal into parallel
  cloud session threads, each on its own git branch + repo copy, shared project memory; keeps
  running after you close the laptop. Select Pro and Max subscribers.
  - https://www.marktechpost.com/2026/09/17/anthropic-launches-claude-code-projects-in-beta-parallel-cloud-sessions-that-keep-running-after-you-close-your-laptop/
  - https://www.theregister.com/ai-and-ml/2026/09/18/claude-code-revamps-projects-so-you-can-work-and-pay-in-parallel/5297532
- Opus 5.5 became the Claude Code default (2026-09-23/24), with limit changes.

## Community best-practice writeups
- https://alexop.dev/posts/claude-code-workflows-deterministic-orchestration/
- https://thepromptshelf.dev/blog/claude-code-multi-agent-orchestration-patterns-2026/
- https://hidekazu-konishi.com/entry/claude_code_subagents_and_orchestration_guide.html
- https://smartscope.blog/en/generative-ai/claude/claude-code-best-practices-advanced-2026/
- https://rosmur.github.io/claudecode-best-practices/
- https://www.firecrawl.dev/blog/best-claude-code-skills

## Converging consensus (repeated across independent sources)
- Loop: **research → plan → execute → review → ship**, human approving at the plan gate.
- Context management is the top skill: short CLAUDE.md, path-globbed rules, aggressive `/clear`.
- Skills: write one for any workflow repeated twice.
- Subagents cover ~80% of multi-agent needs; reach for teams/frameworks only past that.
- Fan out only on **independent** units — two agents editing one file will race.
- 3–5 parallel agents is the practical sweet spot for everyday work.

## Leads from John's own unread TLDR issues (worth reading properly)
- "proper agent evals" (2026-09-23) — measuring whether your setup changes actually help
- "harness tax" (2026-09-17) and "don't go all-in on AI" / "don't turn your brain off"
- Hermes: 1393 subagents, ~19h, refactored a million-line Python repo, -34.4% non-test source
- "Google's self-improving harnesses" (2026-09-24)
