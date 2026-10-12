# How John uses Claude / AI — working profile

Last updated: 2026-10-12 (first run, derived from connected systems — **not yet confirmed by John**)
Confidence legend: [OBS] observed in data · [INF] inferred, worth confirming · [ASK] unknown, in question backlog

## Person & context
- John, john@newelectric.nl. Works at **New Electric** (NL) — electric/marine propulsion. [OBS]
- On the **New Electric Claude Team plan** (invited by jorge@newelectric.nl, 2026-10-07; seat upgraded 2026-10-08). Colleagues are on Claude too → team leverage is available. [OBS]
- Timezone Europe/Amsterdam (some tasks Europe/Berlin). [OBS]
- Also a serious musician/student: trumpet + piano, Zuyd conservatory first year, jazz theory, original music, recording. Big non-work load. [OBS]
- Uses **TickTick** as primary task system (~30 projects, GTD-ish: inbox projects, "Admin Power Hours", "Goal Reviews", "Someday/Reference"), **Obsidian** for notes, **Gmail**, **Atlassian/Jira**, **GitHub**. [OBS]
- Reads TLDR newsletter daily; subscribed to Claude Code release emails → already tracking AI news passively. Tips must beat TLDR, not duplicate it. [OBS]

## How Claude is actually used
- **Claude Code on a real product: "Trace Trimmer"** — a desktop GUI tool that trims **CAN bus trace logs** (parses `;`-comment headers, Unix-epoch start/end times, `can_log_[ip]_[start]_[end]` filenames from an "insight can converter"). Work tool, not a toy. [OBS]
- **TickTick is his prompt backlog.** Task descriptions in ✂Trace Trimmer are written as full Claude Code prompts, pasted in later. Smart — but means prompts are re-typed rather than versioned. [OBS]
- **Repeats standing rules inside one-off prompts.** The "reduce start-up time" task literally asks Claude to "make a rule that will definitely see whenever I start claude in this folder" and to "test this each time you make a change… keep trying until you do fulfill this requirement." → He wants persistent invariants + verification loops but is expressing them as prose per-prompt. **Biggest single gap found.** [OBS]
- **Uses cloud/scheduled routines.** This repo (`jonnolly/clauderoutines`) exists purely to hold routines; a separate daily **email review** routine already runs. [OBS]
- Has a TickTick project **🟥Claude questions** — parks things to ask Claude (currently: retirement-fund planning via private browser). So he already treats Claude as an advisor beyond code. [OBS]
- Frequent claude.ai magic-link sign-ins (Sep 20, 21, 22, Oct 5, 8) → likely mixes web/desktop app with CLI. [INF]

## Stated goals & constraints (from the routine brief, authoritative)
- Wants to be **ahead of the curve** on effective AI use: dev, project management, engineering, and personal development/life goals where genuinely useful.
- **Hard cap: 15 minutes/day.** Workflow improvement must never crowd out revenue-generating output.
- Interested in: multiple agents, assigned roles, continuously-working agents — and explicitly wants things he is **not already doing**.
- **He schedules his own follow-ups.** Do NOT create TickTick tasks or routines for him; surface the suggestion, let him file it.

## Things NOT to suggest (already doing)
- Scheduled/cloud routines, Gmail+TickTick+Jira MCP integration, keeping a prompt backlog, following AI news.
