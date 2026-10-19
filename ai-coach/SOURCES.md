# Sources

**Primary (Anthropic, verified by reading the page/email):**
- Claude Code best practices — https://code.claude.com/docs/en/best-practices
  (verification loops, `/goal`, Stop hooks, plan mode, CLAUDE.md, skills, subagents,
  adversarial review, `/clear` + two-correction rule, non-interactive `claude -p`,
  `/batch`, worktrees, parallel sessions, permissions/sandboxing)
- "This week in Claude Code", 17 Oct 2026 newsletter (in John's inbox, mostly unread):
  desktop nested sessions, cloud sessions carrying uncommitted changes, network secrets on
  Team, Haiku 5.5, Team API credits, Code Review GA with depth levels, per-subagent effort
  and model (v2.1.292), hooks `onFailure: block` (v2.1.295), idle compaction and `/usage`
  warnings (v2.1.299), the subagent pacing sentence, Managed Agents onboarding
- Supporting Anthropic docs: sub-agents, hooks, skills, claude-code-on-the-web,
  managed-agents, changelog

**Secondary (practitioner blogs — directionally useful, specifics unverified):**
- Spec-driven development and context engineering round-ups (DataCamp, openhands.dev,
  developersdigest, blink.new). The "2 h spec saved 6–10 h" and "80% of disasters" style
  figures are anecdotes, not evidence — used only as framing, never quoted to John as fact.
- Subagent guides (Tembo, explainX, Totalum, nimbalyst): agree on narrow scope, restricted
  tools, explicit context passing. They **contradict each other** on nested subagents, so
  that detail was not used.
- Agent-reliability and founder-workflow guides (mlflow, futureagi, causo, krapton,
  reinventing.ai): workflows beat open-ended autonomy; evals/metrics from day one;
  "agent drafts, human sends" for outward-facing work; treat output like a junior's work.
  Widely repeated failure statistics in this genre could not be traced to primary sources.
