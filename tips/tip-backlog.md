# Tip backlog — ranked

Rules: one tip per day. **Each must be doable in ≤15 minutes, standalone, and tailored.**
Re-rank whenever the profile changes (especially after Tier-1 questions are answered).
Move a tip to `tips/delivered/` and log it in `tips/log.md` once sent.

Ranking = (leverage for John specifically) × (how far ahead of his current practice) ÷ (minutes to adopt).

## Ready to send

| Rank | Tip | Hook into his situation | Min | Status |
|---|---|---|---|---|
| 1 | **Turn your per-task prose rules into a `CLAUDE.md`** | He literally wrote "make a rule that will definitely see whenever I start claude in this folder". That's CLAUDE.md. | 10 | SENT 2026-10-01 |
| 2 | **Spec-first: 10 bullet points before any feature prompt** | His Trace Trimmer tasks are already half-specs. Formalising gets reported ~3–10× first-pass success on non-trivial tasks. | 10 | ready |
| 3 | **Plan mode before code mode** on anything touching >1 file | Cheapest guard against Claude confidently going the wrong direction for 20 minutes. | 5 | ready |
| 4 | **One `Stop` hook that runs your build/test** | His "test this each time you make a change, keep trying until it passes" becomes automatic and non-negotiable. | 12 | ready |
| 5 | **Subagents for search, not for answers** — fan out exploration, get back a summary | Keeps the main context clean; the #1 cited 2026 practice. Directly fixes "Claude forgot what we were doing". | 8 | ready |
| 6 | **Git worktrees → two Claude sessions at once** | Lets one agent grind a slow refactor while he drives a second. Fits his fragmented, interrupted days. | 15 | ready |
| 7 | **A `DECISIONS.md` next to CLAUDE.md** | Stops re-litigating choices he already made months ago on a project he touches intermittently. | 8 | ready |
| 8 | **Make `@Claudeready` a real pipeline, not a tag** | He already tags tasks for Claude. Next step: a routine that drains the tag into actual prepped prompts. | 12 | ready |
| 9 | **Write the test first, let Claude make it pass** | Converts "did it work?" from a judgement call into a boolean. Biggest reliability win available. | 10 | ready |
| 10 | **Skills for anything he's explained more than twice** | Packages repeated instructions once. Candidates: CAN-trace file formats, his release/packaging steps. | 15 | ready |
| 11 | **Give Claude the error, not your description of the error** | Highest-frequency small win. Paste the stack trace + the command, not a summary. | 2 | ready |
| 12 | **"Ask me 3 questions before you start"** as a standing opener | Cheap way to surface wrong assumptions before they cost an hour. | 3 | ready |
| 13 | **Checkpoint + `/compact` discipline on long sessions** | Context is the binding constraint; pruning deliberately beats hitting the wall mid-task. | 6 | ready |
| 14 | **Scheduled routine that drains "🟥Claude questions"** | He has a standing question backlog. Let a routine pre-research answers overnight. | 12 | ready |
| 15 | **A weekly "what did Claude get wrong" note** | Failure log → feeds straight back into CLAUDE.md. Compounding reliability. | 8 | ready |
| 16 | **Separate the "research" repo from the "build" repo** | Keeps personal/financial research (mortgage, pensions) out of work context and vice versa. | 10 | ready |

## Blocked / needs an answer first

| Tip | Blocked on |
|---|---|
| MCP server for New Electric internal data | Q8 (what's allowed with company data) |
| Packaging/distribution + auto-update pipeline for Trace Trimmer | Q4 (is it commercial?) |
| Obsidian-as-context (Claude reading the vault) | Q9 |
| Multi-agent orchestration / Workflow scripts | Q2 + Q3 (needs CLI + fundamentals in place first) |

## Sources

- [Effective context engineering for AI agents — Anthropic](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Effective Claude Code Workflows in 2026: What Changed and What Works Now](https://medium.com/data-science-collective/effective-claude-code-workflows-in-2026-what-changed-and-what-works-now-c93ebc6f8f50)
- [Claude Code Git and Parallel Workflows: Branches, Worktrees, Subagents](https://blog.restatolabs.com/claude-code-git-parallel-workflows/)
- [Claude Code Worktrees Guide (2026)](https://www.claudedirectory.org/blog/claude-code-worktrees-guide)
- [Spec-Driven Development: Writing Specs Is the Highest-ROI Engineering Move in the AI Era](https://iaiuse.com/en/posts/spec-driven-development-writing-specs-is-the-highest-roi-engineering-move-in-the-ai-era-ai-era-software-engineering-transformation)
- [Spec-Driven Development for Solo Developers](https://daily.dev/posts/spec-driven-development-for-solo-developers-the-plan-i-use-affao26um)
- [Claude Code Subagents and Multi-Agent Workflows: Complete Guide 2026](https://explainx.ai/blog/claude-code-subagents-multi-agent-workflows-2026)
- [Making Your Second Brain AI-Compatible](https://juanjofuchs.github.io/productivity/2025/12/16/making-second-brain-ai-compatible.html)
