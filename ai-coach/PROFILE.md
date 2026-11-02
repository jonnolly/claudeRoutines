# John — AI usage profile

Purpose: durable memory for the "daily AI tip" routine so it never has to re-derive
context. Update this file whenever something is learned or changes.

Last updated: 2026-11-02 (run #1 — built from observed signals, NOT yet confirmed by John)

## Who / what (observed, high confidence)

- Email: john@newelectric.nl — New Electric (NL), electric marine propulsion / battery systems.
- Work appears to be engineering + field support on battery packs: live email threads with
  Zeppelin CAT about "330 Z-Line XNB20126 — Pack2 Precharge Timeout". Colleagues seen:
  Sidd, Sam, Rogier van Rooijen, service@newelectric.nl.
- Jira at newelectric.atlassian.net, project key seen: NEP006 (issues assigned to him by
  colleagues, e.g. NEP006-101).
- Heavy GTD user in TickTick (~32 projects), with real discipline: "Daily reset — Inbox to
  zero, pick 3+1 for tomorrow", "Weekly Goal Review", Beeminder logging, appointment
  reminder project, Work→Personal and Personal→Work inbox projects, "Add to Obsidian" queue.
- Also a music student: Zuyd (preparatory + first year), piano practice, trumpet/drums,
  original music, recording projects. Plus counselling, relationship, house, goal-review
  projects — he runs his personal life through the same system as work.
- Reads TLDR newsletter daily (so: already exposed to AI headlines; tips must go deeper
  than newsletter level to be worth his 15 minutes).
- Anthropic seat upgraded recently; invited to a "New Electric on Claude" org seat →
  team/org usage, not just personal.
- Uses Claude Code cloud sessions + scheduled routines (this one). Receives "This week in
  Claude Code" emails.

## Claude/AI usage (INFERRED — needs confirmation, see BACKLOG Q1–Q5)

- Routines/scheduled prompts: yes, at least this one, plus an "email review" in the morning.
- `claudeRoutines` repo existed with only a README → routines are configured in the Claude
  app, not version-controlled, and there was no persistent memory for them until this file.
- No CLAUDE.md, no skills, no subagents, no hooks anywhere → almost certainly using Claude
  as a conversational assistant + routines, not yet as an orchestrated dev system.
- Unknown: how much actual coding/firmware work he does with Claude vs. email/PM/research.

## Constraints he set (treat as hard rules)

1. **≤15 minutes per day.** Workflow improvement is secondary to producing output that
   earns money. A tip that costs 45 minutes is a failed tip even if it's a good idea.
2. **One tip per day**, delivered in the morning with the email review.
3. **He creates his own tasks and schedules his own routines.** This routine must never
   create TickTick tasks, Jira issues, or new scheduled routines on his behalf. Suggest,
   don't schedule.
4. Tips must be tailored and must be things he is **not already doing**.

## Known friction / open issues found

- 2026-11-02: Atlassian MCP connector is on the deprecated v1 HTTP+SSE transport and now
  hard-fails ("being phased out", must move to https://mcp.atlassian.com/v2/mcp and
  re-authorise). Every Jira call from routines/sessions fails until he reconnects it.
  → became Tip #1.
