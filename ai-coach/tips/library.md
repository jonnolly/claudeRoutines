# Tip library — researched candidates, ranked

Source grounding (checked 2026-10-15):
- Anthropic, *Best practices for Claude Code* — https://code.claude.com/docs/en/best-practices (primary; everything below marked **[official]** comes from here)
- Claude Code subagents docs — https://code.claude.com/docs/en/sub-agents
- Spec-driven development overviews 2026 — https://www.deeplearning.ai/courses/spec-driven-development-with-coding-agents , https://dev.to/krlz/spec-driven-development-in-2026-what-it-is-the-tooling-and-how-teams-actually-use-it-2fk2
- Context engineering as the core 2026 skill — https://www.forbes.com/sites/nehamehra/2026/08/03/why-ai-agent-startups-are-becoming-the-new-solo-founder-playbook/
- Practitioner guides (lower confidence, vendor/SEO-adjacent): https://www.openhands.dev/blog/claude-code-best-practices-agentic-coding , https://software.rajivprab.com/2026/07/13/using-subagents-to-improve-claude-code/

The single organising idea across all credible 2026 sources: **context is the scarce resource,
and anything you can turn into a check the agent runs itself is work you stop doing.**

Ranked for John specifically — effort ≤15 min, highest expected payoff first.
Status: `queued` → `sent (date)` → `adopted` / `declined` / `no answer`.

| # | Tip | Est. | Why him | Status |
|---|---|---|---|---|
| T1 | **Put your standing rules in `CLAUDE.md`, not in every prompt.** Run `/init` in the project, then prune to only rules Claude would otherwise get wrong — build/test commands, the <1 s startup budget, "run the check before you say it's done". **[official]** | 10 min | He literally wrote *"make a rule that will definitely see whenever I start claude in this folder"* into a task description. He's describing CLAUDE.md from first principles. | sent 2026-10-15 |
| T2 | **Give every task a check the agent can run**, then tell it to iterate until green. Anthropic's #1 principle: without a runnable check, "looks done" is the only signal and *you* become the verification loop. **[official]** | 5 min/task | He already does this by instinct in prose; formalising it (a script / test command named in CLAUDE.md) makes it stick across sessions. | queued |
| T3 | **Move the Trace Trimmer backlog out of TickTick and into the repo** (`BACKLOG.md` or GitHub issues). Prompts an agent can't see are prompts that never run. Unlocks unattended runs. | 15 min | 7 shelf-ready prompts, idle since Oct 2025. Highest "workflow → money" conversion available. | queued |
| T4 | **Plan mode before multi-file work** (`Shift+Tab` → explore → plan → implement → commit). Skip it for one-sentence diffs. **[official]** | 0 min setup | Cheapest guard against the agent solving the wrong problem when he's time-boxed. | queued |
| T5 | **`/clear` between unrelated tasks**; after two failed corrections, clear and re-prompt rather than arguing. **[official]** | 0 min | Pure habit change, no setup, immediate reliability gain. | queued |
| T6 | **Writer/Reviewer: two sessions.** One implements, a second reviews the diff in a fresh context (or `/code-review`). A fresh context isn't biased toward code it just wrote. **[official]** | 10 min | His named interest ("multiple agents, assigning roles") and the safest first use of parallelism. | queued |
| T7 | **Subagents for research**, so file-reading doesn't eat the main context: *"use subagents to investigate X"*. **[official]** | 0 min | Directly addresses the context constraint; zero setup cost. | queued |
| T8 | **Let Claude interview you, then write `SPEC.md`**, and execute it in a fresh session. The prompt is in the official docs. **[official]** | 15 min | Best fit for a feature-sized chunk of Trace Trimmer; spec survives his fragmented schedule. | queued |
| T9 | **Stop hook as a hard gate** — a script that blocks the turn ending until tests/startup budget pass. Deterministic where CLAUDE.md is only advisory. **[official]** | 15 min | The real answer to "make a rule that will *definitely* apply". Needs T1 first. | queued |
| T10 | **Git worktrees for genuine parallelism** — separate checkouts so two sessions don't collide. **[official]** | 15 min | Step 2 of multi-agent, only worth it once T6 pays off. | queued |
| T11 | **`claude -p` non-interactive + fan-out** over a file list for repetitive changes. **[official]** | 15 min | Only if a batch-shaped job shows up; don't push it before then. | queued |
| T12 | **Prune your MCP connector set per session.** Every connected server costs context before you type anything; curate a small high-signal set. | 5 min | He has Gmail + TickTick + Jira + GitHub all attached at once. | queued |
| T13 | **Skills for occasional workflows**, CLAUDE.md only for always-on rules — keeps the always-loaded file short. **[official]** | 15 min | Natural follow-on once CLAUDE.md starts growing. | queued |
| T14 | **Personal: the private-browser advice pattern.** His own "retirement funds" question already uses it — generalise it to a repeatable decision brief (situation → constraints → options → recommendation → review date). | 15 min | Covers the life-goals half of the brief without leaking work context. | queued |

## Deliberately not recommending (yet)

- **Agent teams / large fan-outs.** Coordination overhead and conflicting edits are real; several
  2026 write-ups flag multi-agent fragility. Not until T1/T2/T6 are habits.
- **Buying a context-engineering tool.** For a solo dev the native features are enough.
