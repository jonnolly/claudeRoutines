# Sources (refresh roughly every 2 weeks)

## Read 2026-11-19
- **Anthropic / Claude Code — Best practices** (primary, authoritative):
  https://code.claude.com/docs/en/best-practices
  Covers: deterministic vs non-deterministic instructions, CLAUDE.md discipline (<200 lines,
  `/doctor prompt-audit`), path-scoped `.claude/rules/`, team procedures as skills
  (`disable-model-invocation`), "give Claude a check to run", `/goal`, Stop hooks,
  `/code-review`, `/verify`, subagent costs and read-only reviewers, effort levels and
  `ultrathink`, auto mode, `/usage` and context cost, `/clear` / `/rewind` / `Esc`,
  the five questions before an unattended run, headless `claude -p --bare`, `/loop` and
  cloud routines, worktrees / `.worktreeinclude` / `/batch`, and a "what you can stop doing"
  table retiring several 2025-era habits.
- **Spec-driven development consensus (2026)** — practitioner + preprint:
  - SDAD: Spec-Driven Agentic Development for the AI-Native SDLC — https://arxiv.org/pdf/2608.20341
  - Spec Kit Agents: Context-Grounded Agentic Workflows — https://arxiv.org/html/2604.05278v1
  - Process taxonomy of frameworks for AI software agents — https://arxiv.org/pdf/2606.04967
  - Mise en Place for Agentic Coding (context engineering) — https://arxiv.org/pdf/2605.05400
  - Codified Context: infrastructure for agents in a complex codebase — https://arxiv.org/pdf/2602.20478
  Caveat: largely preprints and community posts; treat specific numbers as opinion.
- **Safety-critical / embedded specifics** (relevant to New Electric):
  - Agentic Agile-V: From Vibe Coding to Verified Engineering — https://www.alphaxiv.org/abs/2605.20456
  - AI for embedded code review — what it catches and misses —
    https://www.designnews.com/artificial-intelligence/ai-code-reviews-excel-at-text-but-miss-hardware-context-in-embedded-systems-development
  - GenAI for firmware: where LLM code generation fails — https://promwad.com/news/genai-for-firmware-llm-code-generation-certification-risks
  - Agentic AI in the automotive V-cycle — https://www.eejournal.com/fish_fry/winning-the-v-cycle-agentic-ai-accelerates-safety-critical-automotive-software/
  Consensus: strong on text-level review, weak on register/ISR/timing semantics;
  the real opening is requirement↔code traceability and repetitive safety documentation,
  with human approval gates kept in place.
- **Subagent / parallel-agent practice** (secondary, community):
  https://claudefa.st/blog/guide/agents/sub-agent-best-practices ,
  https://www.aakashx.com/blog/parallel-claude-code-agents/
  Consistent rule of thumb: parallel *writers* need isolation (worktrees / strict file
  ownership); keep parallel subagents read-only otherwise; don't over-parallelise small tasks.

## Not yet mined
- Anthropic engineering blog (agent evals, context engineering posts).
- `code.claude.com/docs/en/llms.txt` full docs index — routines, skills, hooks pages in depth.
- Whether New Electric's Atlassian has Jira automation worth pairing with Claude.
