# Profile: how John uses Claude / AI

Last updated: 2026-11-23 (first run). Everything below is **inferred** from connected
tools unless marked "Confirmed by John". No prior session history existed to read —
the cloud container starts fresh, so this file is the memory.

## Who / what he works on
- John Connolly, john@newelectric.nl. **New Electric** (Dutch) — electrification of heavy
  machinery / marine. Systems-software side.
- Live work seen in Jira/Confluence/GitHub (Nov 2026):
  - `NEP007` — **W150Fi review**: a large set of requirement tickets he is driving
    (pack current limits 300 A / 700 A, DC-link <60 V wait timeout, LOW_POWER_MODE at
    170 kW on one pack, welded-contactor warning, precharge checks, OBS bench test plan
    OT1–OT11, LV verify on the "Beast" motor controller).
  - `NEP006` — HX70 HVAC, fan PWM control (repo `NEP_006_HX70_HVAC`, PR #1).
  - `NE124` — tickets auto-assigned to him.
  - Internal web tools: `NEDCKR_MECH_bomBOM` (PR #41, perf work), `NEDCKR_LOG_eShelf`
    (PRs #82/#83, label queue + lean stock). PR titles on these read as AI-authored and
    are ticket-numbered — **unconfirmed whether these are his, a colleague's, or Copilot's.**
  - Colleagues: Frank, Rogier, Adarsha, Sam, Jorge. Sam sends "Notes + your actions"
    software-team summaries; Frank sends a "New Workflow — what happened in the last 2 weeks"
    digest. Both look AI-generated → there is already an AI culture in the team.
  - Jira on a new Standard trial; Atlassian usage-based billing starts Dec 3 2026.
- **Personal side project: Trace Trimmer** — a GUI tool that trims CAN log trace files
  (handles "insight can converter" format, `can_log_<ip>_<startUnix>_<endUnix>`). Clearly
  work-adjacent tooling he owns. This is where his Claude Code habits are most visible.
- Studying jazz at **Zuyd** conservatorium (first year): piano, trumpet/sax, theory,
  original music, recording, gigs. Also: counselling, gratitude journal, goal reviews,
  retirement planning, house, Dutch vocabulary.

## How he uses Claude today (observed)
- **Writes prompts as task-manager entries.** TickTick Trace Trimmer tickets are written
  directly at Claude, e.g. *"Make a rule that will definitely see whenever I start claude in
  this folder that the start-time must always be under 1 second. Test this each time you make
  a change… you must keep trying until you do fulfill this requirement."* So: capture in
  TickTick → paste into Claude Code. Good instinct, wrong mechanism (see Tip 001).
- Keeps a TickTick project **"🟥Claude questions"** for things to ask Claude later
  (currently 1 item: retirement-fund strategy, to be asked in a private browser).
- Keeps a **"♦Add to Obsidian"** project → Obsidian is likely his knowledge store.
- Running **Claude Code cloud routines** (this one). Connected MCP: Gmail, TickTick,
  Atlassian, GitHub. Atlassian MCP is on the deprecated v1 SSE endpoint and **currently
  fails** — needs re-auth to v2 (`https://mcp.atlassian.com/v2/mcp`).
- Reads **TLDR newsletter** daily → he tracks AI news already; tips must beat TLDR's level.
- Inbox: ~930 messages, 27 unread in inbox, 785 unread overall, 90 drafts. A "beginning of
  the day email review" is part of his routine. Heavy Jira/Confluence notification load.
- Account note: extra-usage credits show `out_of_credits` → cost per task is a real constraint,
  so tips should favour cheap levers (checks, hooks, `/clear`, effort down) over fan-out.

## His own hypotheses (from the brief, 2026-11-23)
> "using multiple agents, assigning roles, having them continuously working etc."

Partly outdated — see Tip 001's heads-up. Subagents-for-context and
delegation-for-a-better-answer are both on Anthropic's "what you can stop doing" list.
What survives: parallel independent work, keeping noisy output out of the main session,
and independent review.

## Confirmed by John
_(nothing yet — first run)_

## Known gaps
See `questions.md`.
