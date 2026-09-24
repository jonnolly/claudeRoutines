# Technique Library

The pool future daily tips are drawn from. Each entry: what it is, why it pays, how it maps to
John's situation, and a time estimate. Ordered by expected payoff **for him specifically**.

Refreshed periodically against current sources (see Sources at the bottom).

## The framing that governs everything here

The most important result in this literature is a caution, not a technique. METR's randomized
controlled trial found experienced open-source developers were **19% slower** with AI tooling on
codebases they already knew well — while believing they had been faster. Anthropic's own Societal
Impacts work finds developers use AI in ~60% of their work but can *fully* delegate only 0–20% of
tasks.

Read together: AI leverage is real but concentrated. It shows up in unfamiliar code, boilerplate,
breadth-first search, and anything with a mechanical verifier — and it goes *negative* when you
babysit an agent through work you could have typed yourself. This is exactly John's stated
instinct ("output that earns money beats workflow polish"), so the programme should be biased
toward techniques that either (a) close a correctness loop without him in it, or (b) move revenue.

## Tier A — highest payoff for John

### A1. Executable verification gates  → **Tip 001**
"It should work" is not a signal; a passing test, a diff, or a log is. Any requirement stated as
prose to an agent is a requirement that will silently rot. Convert it to something that exits
non-zero.
*Fit:* He literally wrote "test this each time you make a change... keep trying until you fulfil
it" into a task description. That is a hook + check script described in English. **12 min.**

### A2. CLAUDE.md as the project's standing brief
Under ~300 lines: stack, commands, conventions, invariants, gotchas. Read automatically at session
start, so it is the cheapest possible way to stop re-explaining things.
*Fit:* Gated on Q4. If absent from Trace Trimmer, this is the second tip. **10 min.**

### A3. Context engineering as a maintained loop, not a one-off file
Zhang et al.'s Agentic Context Engineering (ICLR 2026) treats context as an evolving document:
generate strategies, reflect on what worked, curate — add what succeeded, delete what failed.
The practical version: end sessions by asking Claude what belongs in CLAUDE.md, and prune.
*Fit:* Pairs with A2 as the follow-up. Prevents the classic bloated-CLAUDE.md failure. **8 min.**

### A4. Subagents for anything that reads a lot and returns a little
Agents defined in `.claude/agents/` run in their own context window with their own tools. Research,
log-trawling and codebase sweeps return a conclusion instead of dumping 40 files into your main
context.
*Fit:* Direct hit on CAN trace analysis — reading large trace files is exactly "reads a lot,
returns a little". Potentially his single biggest domain win. **15 min.**

### A5. Revenue-side delegation: the freelance funnel
The Upwork/Toptal/Codementor tasks are stale and manual. Proposal drafting, CV/LinkedIn rewriting
and portfolio copy are high-volume, low-judgement, templatable work — the ideal delegation shape.
*Fit:* The only technique here that directly makes money rather than saving minutes. Rank high
once Q3 confirms freelance matters. **15 min, repeatable.**

## Tier B — strong, but sequence them later

### B1. Plan mode before large edits
Separate "decide what to do" from "do it". Cheapest known fix for agents confidently doing the
wrong thing at scale.

### B2. Parallel agents in git worktrees
Multiple independent sessions on isolated checkouts of the same repo — his own stated curiosity
("using multiple agents... continuously working"). Real, but only pays once single-session work is
already clean; otherwise it multiplies mess. Deliberately sequenced *after* A1–A4.

### B3. Hooks as guardrails
Deterministic shell commands the harness runs on tool events — auto-format, block edits to
protected paths, run a check after every write. The enforcement layer under A1.

### B4. Skills as institutional knowledge
Packaged, reusable procedures ("Knowledge Activation", arXiv 2026, frames skills as the
institutional-knowledge primitive). For John: a repeatable "analyse this CAN trace" or "draft an
Upwork proposal" procedure that doesn't get re-invented each time.

### B5. Long-running / continuously working agents
The 2026 Anthropic Agentic Coding Trends framing: coordinated agent teams running for hours, with
the engineer orchestrating rather than typing. Aspirational end-state — gated on Q8, and on
verification (A1) being solid, because unattended work without a verifier compounds errors.

## Tier C — personal / life, use sparingly

### C1. Reviews and goals with a thinking partner
He already has `✨Goal Reviews`, `🧠Councilling`, `❤Gratitude Journal` — structure exists; AI adds
synthesis across entries, not more structure.

### C2. Practice-log analysis for conservatory work
Zuyd year + `🎹Piano Practice` kanban. Trend-spotting across practice logs is a genuine, if modest,
use. Keep rare — he asked for efficiency, not more things to maintain.

### C3. Reduce auth friction
Magic-link sign-in several times daily is pure tax. Trivial, not a full tip — fold into a Friday
round-up of small wins.

## Anti-patterns to warn about

- Optimising the workflow instead of shipping (his own stated risk, and METR's finding).
- CLAUDE.md bloat — past a few hundred lines it stops being read carefully and starts being noise.
- Multi-agent before single-agent hygiene — parallelism multiplies an unverified process.
- Trusting agent self-reports of success with no mechanical check (the core of A1).

## Sources

- [Best practices for Claude Code — Anthropic Engineering](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Anthropic's 2026 Agentic Coding Trends Report: From Assistants to Agent Teams](https://rits.shanghai.nyu.edu/ai/anthropics-2026-agentic-coding-trends-report-from-assistants-to-agent-teams/)
- [Knowledge Activation: AI Skills as the Institutional Knowledge Primitive (arXiv)](https://arxiv.org/pdf/2603.14805)
- [A Phased Workflow for Operating LLM-Based Coding Agents (arXiv)](https://arxiv.org/pdf/2608.30701)
- [Harness Engineering for Agentic AI Coding Tools (arXiv)](https://arxiv.org/pdf/2602.14690)
- [(Im)Paired Programming: Coding Agents Improve Productivity but Harm Understanding (arXiv)](https://arxiv.org/pdf/2607.26375)
- [Context Engineering Research: Papers & Benchmarks (2026)](https://www.iwoszapar.com/p/context-engineering-research-2026)
- [10 Claude Code Best Practices for Agentic Coding: A 2026 Guide](https://www.openhands.dev/blog/claude-code-best-practices-agentic-coding)
- [Loop Engineering: Build Agent Loops in Claude Code](https://www.kunalganglani.com/blog/loop-engineering-agent-loops)
