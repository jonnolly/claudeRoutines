# John's Claude / AI usage profile

Last updated: 2026-09-21 (first build — inferred, not yet confirmed by John)

Everything below marked **[inferred]** came from his own connected accounts
(TickTick, Gmail metadata, GitHub) during the 2026-09-21 routine run. Anything
marked **[confirmed]** was stated by John. Correct freely — the point of this
file is that tips land on his real situation, not a generic developer.

## Who / context

- John Connolly, `john@newelectric.nl`, GitHub `jonnolly`. Europe/Amsterdam–Berlin. **[inferred]**
- Works at New Electric on a **3.5-day contract**, deliberately keeping ~1.5 days
  free — a recurring task reads "use extra 1.5 days for finding remote employment",
  and he is actively hunting remote work. **[inferred]**
- Simultaneously a **music student** — Zuyd conservatoire first year (jazz, trumpet,
  piano), plus gigs, recording and theory homework. Projects: `🥁Zuyd First Year`,
  `🎹Piano Practice`, `🎺Zuyd Preparatory Jazz`, `☝Fingertips Recording`. **[inferred]**
- Mid-life reorganisation in progress: `🎓Starting School / Move`, `🏡House`,
  mortgage decisions (Maastricht vs. Utrecht commute), long-term savings /
  retirement modelling, `🧠Councilling`, `❤Gratitude Journal`, `✨Goal Reviews`. **[inferred]**
- So: **time is the scarce resource, not ideas.** Tips should buy back hours and
  reduce the number of things needing his personal attention.

## Tooling he already has

- Claude paid plan; receipts forwarded to a colleague, so partly expensed. **[inferred]**
- Claude Code desktop (Electron trusted device added 2026-09-09) + frequent
  claude.ai web sign-ins via magic link (several per week). **[inferred]**
- **Scheduled routines** — including a daily **email review** and this tip routine. **[confirmed]**
- MCP connectors live: **TickTick, Gmail, Atlassian (Jira/Confluence), GitHub**. **[inferred]**
- **Obsidian** vault, with a `♦Add to Obsidian` capture project and a Templater +
  gratitude-journal entry setup. **[inferred]**
- **TickTick** as the system of record, GTD-ish: project-per-area, kanban views,
  `🧔Work to Personal Inbox` / `💼Personal to Work Inbox` bridges, a **daily review**,
  `💻Admin Power Hours` for batching admin. **[inferred]**

## Coding projects

- `✂Trace Trimmer` (task: "reduce start-up time") **[inferred]**
- `❤Gratitude Journal` — an app he is building; tasks reference importing from
  Presently and giving Claude a backup file as an example. **[inferred]**
- `claudeRoutines` (this repo). **[confirmed]**
- Public GitHub is thin (5 repos) — most work is likely local or private. **[inferred]**

## How he uses Claude today

1. **Heaviest pattern by far: queued one-off conversations.** His TickTick is full of
   tasks that *are* Claude prompts — "ask claude what the state of music therapy is
   in southern france", "ask claude which jazz albums have no chordal instruments",
   "Get Claude to create spreadsheet for long term savings", "continue asking claude
   about maastricht mortgage". At least one (`sangomas`, 2026-07-14) has a **fully
   drafted prompt in the task body** — the thinking was finished; only the *running*
   was outstanding, and it sat four days. Others are months old and still open. **[inferred]**
2. **Claude as adviser across life domains**, not just code: jazz practice plans,
   ADHD notes, ethics reading lists, mortgages, retirement maths, a "claude profile
   as cbt therapist", spiritual-jazz research. **[inferred]**
3. **Coding standards already exist** — a `claudeCodingStandards` document he had
   Claude write in Sept 2025, specifying self-verification: reproduce the bug, turn
   it into a test, fix, re-run, and report if it *can't* reproduce. He explicitly
   wanted it readable across projects, not just one. (Task completed 2025-09-19.)
   → He is already on the verification-loop practice. Don't sell it back to him;
   check instead whether it has since become a real `CLAUDE.md` / skill. **[inferred]**
4. **Automation curiosity is live**: "investigate training your own AI specialist
   models", "Update Claude plan", and this very routine. **[inferred]**

## Stated interests for improvement **[confirmed]**

Multiple agents; assigning roles; agents working continuously; anything that
improves efficiency / workflow / speed / reliability that he is not doing yet.

## Working hypotheses about the biggest gaps

- **He is the runtime.** Work is queued *for him to hand to Claude* rather than
  handed to Claude directly. This is the #1 addressable inefficiency.
- Likely single-session, single-agent usage — no evidence of subagents, worktrees,
  parallel sessions or background agents.
- Personal/life work is done in claude.ai chat, so it has **no persistent memory
  across sessions** beyond what he re-pastes; the Obsidian vault is not (yet)
  wired in as Claude-readable context.
- His capture system has real noise (~40 duplicate copies of one recurring task),
  which an agent could clean up.
