# John — AI/Claude usage profile

> State file for the **daily AI tip** routine. Updated each run.
> Last updated: 2026-10-05 (run 1)

## Confidence legend
- **[observed]** — inferred from connector data (TickTick / Jira / repo). Reasonably reliable.
- **[assumed]** — my inference, not yet confirmed. Correct me and it gets fixed here.
- **[unknown]** — open question, see `questions-backlog.md`.

## Who / context
- Email `john@newelectric.nl`; Atlassian site `newelectric.atlassian.net` (Jira + Confluence scopes). **[observed]**
- Based in NL, timezone Europe/Amsterdam (some TickTick items Europe/Berlin). **[observed]**
- Domain: electric drivetrains / embedded — works with **CAN bus trace logs**, IP-addressed loggers, "insight CAN converter" file formats. **[observed]**
- Simultaneously a **music student**: Zuyd conservatory (preparatory + first year), jazz, piano, trumpet, voice, original music projects, gigs. Heavy time competitor with dev work. **[observed]**
- Actively building a **second income stream**: Upwork / Toptal / Proxify, plus teaching via Codementor / Wyzant. Tasks for buying Upwork connects, CV + LinkedIn updates. **[observed]**
- Stated priority (own words): *"it is more important to generate meaningful output that we can earn money with"* than to polish workflow. Workflow time budget: **≤15 min/day**. **[observed]**

## How Claude is currently used
- **Claude Code on a real project: "Trace Trimmer"** — a desktop GUI tool that trims CAN trace/log files by start/end time. Python-ish desktop app with a GUI, an update mechanism, a toolbar, a startup-time budget. **[observed]**
- **TickTick is used as a prompt queue.** Feature requests are written in TickTick task descriptions in full Claude-prompt prose, then presumably pasted into Claude Code. Several tasks carry an **`@claude` tag**. **[observed]**
- **Claude routines (scheduled prompts)** — this repo (`claudeRoutines`) exists for them; a daily email review routine is referenced. **[observed]**
- Obsidian is in the stack ("♦Add to Obsidian" project). **[observed]**
- Already reaching for **self-verification and persistent rules** without knowing the mechanism. Direct quote from a Trace Trimmer task:
  > "Make a rule that will definitely see whenever I start claude in this folder that the start-time must always be under 1 second. **Test this each time you make a change.** If it doesn't fulfill this requirement, you must keep trying until you do fulfill this requirement. If you can't you have to let me know."

  That is a hand-rolled request for a **verification loop + enforced project rule**. This is the single biggest identified gap-to-capability match. **[observed]**

## Working hypotheses about the gaps
- Works **one session at a time, interactively**, pasting prompts in and watching. No evidence of subagents, parallel sessions, or worktrees. **[assumed]**
- Likely **no CLAUDE.md, no hooks, no skills** in the Trace Trimmer repo — otherwise the "make a rule" request would not have been phrased that way. **[assumed]**
- Likely **no automated test suite** on Trace Trimmer; verification is manual (open the GUI, try a file). **[assumed]**
- Re-explains project context at the start of sessions. **[assumed]**

## Constraints to respect (from the user)
- **≤15 min/day** on workflow improvement. Hard ceiling.
- Money-generating output beats workflow polish. Tips must pay back fast.
- **The user creates and schedules their own follow-up tasks/routines.** Do not create TickTick tasks, crons, or routines on their behalf — suggest, and let them schedule.
