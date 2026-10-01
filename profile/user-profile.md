# User profile — John (john@newelectric.nl)

Living document. Each daily run reads this first, then updates it with anything new.
Confidence tags: `[observed]` = inferred from his own data, `[confirmed]` = he told me, `[?]` = unknown / needs asking.

Last updated: 2026-10-01 (run 1 — first run, built from observed data only)

## Context

- Works at **New Electric** (NL) — EV / electric powertrain conversions. `[observed: email domain, CAN-bus tooling]`
- **Jazz student, first year at Zuyd conservatory** (trumpet + piano). Large, fixed time commitment —
  "Pack bag for school", "Student meeting (mandatory)", "Zuyd First Year", "Djam Theory Homework". `[observed]`
- Active music projects: Fingertips Recording, Key May (w/ Kymé), Ecstatic Dance Band, original music. `[observed]`
- Partner: **Kymé**. Lots of relationship/coordination tasks. `[observed]`
- Based NL, timezone **Europe/Amsterdam**. Commutes by train (project "🚆Todo on the go"). `[observed]`

**Implication:** his time is fragmented and scarce. School + day job + music + relationship. The 15-minute
ceiling he set is not arbitrary — it is the real budget. Tips must be *one concrete action*, never a project.

## How he already works (this is a sophisticated operator — don't condescend)

- **TickTick is the operating system.** 32 projects, GTD-shaped: Inbox → routed projects, explicit
  "🚆 Daily reset — Inbox to zero, pick 3+1 for tomorrow" (near-daily), "Daily checkin",
  "Weekly Goal Review", "💻Admin Power Hours". `[observed]`
- **Two-inbox routing**: "🧔Work to Personal Inbox" / "💼Personal to Work Inbox" — he deliberately
  shuttles items between work and personal contexts. `[observed]`
- **Beeminder** for habit accountability (piano, gym). `[observed]`
- **Obsidian** vault ("♦Add to Obsidian" project); recently added Zettlr as a lighter markdown editor. `[observed]`
- **Context-tagged projects** — "🚆Todo on the go", "🎹At the piano", "💻Remote Work". Classic GTD contexts. `[observed]`

## How he already uses Claude / AI

- **`@Claudeready` tag on tasks** — e.g. "@Claudeready find the best free simple markdown editor options
  (not obsidian)". He *queues work for Claude* as a deliberate habit. This is already ahead of most users. `[observed]`
- **"🟥Claude questions" TickTick project** — a standing backlog of questions to put to Claude
  (currently: retirement fund tactics, with instructions to himself to use a private browser). `[observed]`
- **Claude for personal/financial research** — "continue asking claude about maastricht mortgage". `[observed]`
- **Claude Code for a real dev project: Trace Trimmer** — a desktop GUI tool that trims CAN-bus trace
  files (automotive diagnostics). Open backlog in TickTick written *as prompts*, with acceptance criteria
  and test instructions baked in. `[observed]`
- **This repo (`claudeRoutines`)** — he is building scheduled Claude routines, incl. a daily email review. `[observed]`
- Reads the Claude Code newsletter (several unread in inbox — Opus 5.5, plugins/evals, subagent model
  picking, mobile). Interested but not necessarily acting on it. `[observed]`

### The single sharpest observation from run 1

In the Trace Trimmer task "reduce start-up time", he wrote to Claude:

> "**Make a rule that will definitely see whenever I start claude in this folder** that the start-time must
> always be under 1 second. Test this each time you make a change. If it doesn't fulfill this requirement,
> you must keep trying until you do fulfill this requirement."

He is **hand-rolling persistent project memory and verification loops in prose, per task**. That is exactly
what `CLAUDE.md` + a hook does automatically and permanently. This is the highest-leverage gap found so far
and is the basis of tip #1.

## Known gaps — see `profile/open-questions.md`

- `[?]` Which Claude surfaces (CLI / web / desktop / mobile) and which plan.
- `[?]` What actually earns the money, and which part he most wants sped up.
- `[?]` Whether Trace Trimmer has any CLAUDE.md / skills / hooks / subagent use today.
- `[?]` Whether Trace Trimmer is commercial or internal.
- `[?]` What his existing routines are and when they fire.
