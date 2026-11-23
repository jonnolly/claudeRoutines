# Source base (keep current; re-check monthly)

## Primary / authoritative
- **Claude Code best practices** — https://code.claude.com/docs/en/best-practices
  The spine of this series. Key frames: deterministic vs non-deterministic instructions;
  "tell Claude what it can't see"; "give Claude a check to run"; the five pre-flight
  questions for unattended runs; and the **"What you can stop doing"** table (obsolete
  advice: context-window panic, ALL-CAPS emphasis, subagents-for-context,
  delegate-for-a-better-answer, "think harder", architecture dumps in CLAUDE.md).
- Earlier Anthropic post — https://www.anthropic.com/research/claude-code-best-practices
  (`/clear` between tasks; one Claude writes, another reviews)
- Subagents, when they pay — https://claude.com/resources/articles/subagents-in-claude-code
  (worth it for 10+ files or 3+ independent tasks; bad for parallel edits to one file)
- Headless / CI — https://code.claude.com/docs/en/headless ·
  GitHub Actions — https://code.claude.com/docs/en/github-actions ·
  Scheduled tasks/routines — https://code.claude.com/docs/en/routines ·
  Worktrees — https://code.claude.com/docs/en/worktrees ·
  Hooks — https://code.claude.com/docs/en/hooks · Skills — https://code.claude.com/docs/en/skills
- Anthropic course "Claude Code in Action" — https://anthropic.skilljar.com/claude-code-in-action

## Research (handle with care — read originals before quoting numbers)
- **METR** 2025 RCT: experienced OSS maintainers were ~19% *slower* with AI; the 2026
  follow-up is contested and METR itself called the newer data unreliable (selection effects).
  Use as "perceived gain > measured gain", not as a number.
- **DORA**: AI as an *amplifier* of existing team practice — good practices get better,
  weak ones get worse faster. The throughput/stability deltas circulating online are
  second-hand; check the report.
- Stack Overflow survey: ~66% cite "almost right, but not quite" as the top pain;
  ~45% say debugging AI code takes longer → verification cost is the real tax.
- *When Review Alone No Longer Scales: Layered Supervision in AI-Assisted SE* —
  https://arxiv.org/pdf/2608.26316
- *AI Writes Faster Than Humans Can Review* — https://arxiv.org/pdf/2607.01904
- *Agent READMEs: An Empirical Study of Context Files* — https://arxiv.org/html/2511.12884v1
  (devs write context files to make agents *work*, rarely to add security/perf guardrails)
- *A Few Pages of Markdown: Committed AI Configuration and Lower Quality Cost* (2608.25241) —
  **unverified**, direction of effect unclear from the listing. Don't cite until read.

## Personal-knowledge stack (secondary, practitioner blogs)
- Obsidian + Claude Code as the common 2026 "second brain" pairing; recurring advice:
  a ~20-minute weekly review as the keystone habit; keep ~3 core files (identity, active
  projects, decisions); **don't automate a mess** — make it work by hand first; nothing
  enters the vault as fact until a person approves it.
