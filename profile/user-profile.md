# User Profile — John (john@newelectric.nl)

Maintained by the "Daily AI leverage tip" routine. Updated whenever new evidence appears.
Confidence tags: **[obs]** = directly observed, **[inf]** = inferred, **[ask]** = needs confirmation.

## Who / context

- Works at **New Electric** (NL) — EV / electric powertrain conversion. Colleagues seen in mail:
  sidd, sam, jorge, shahbaz. **[obs]**
- Domain work is heavily **CAN bus trace / EV fast-charge diagnostics** — e.g. the live
  `eHilux_DC fast charge issue` thread with evsouth.com, Advantics chargers, trace files
  exchanged with customers (active Aug–Sep 2026). **[obs]**
- Pays the Anthropic subscription personally and forwards receipts to shahbaz@newelectric.nl —
  i.e. **AI spend is expensed to the business**. **[obs]**
- Simultaneously **starting conservatory** (Zuyd, jazz — trumpet/piano). TickTick has
  `🎓Starting School / Move`, `🥁Zuyd First Year`, `🎺Zuyd Preparatory Jazz`. **[obs]**
- Actively building a **remote / part-time freelance dev income stream** — TickTick
  `💻Remote Work` lists Upwork, Toptal, Proxify, Codementor, Wyzant, plus "look for
  opportunities to teach". **[obs]**
- So the money picture is a transition: salaried/consulting EV engineering → study +
  freelance dev + possibly teaching. **[inf]** — confirm split. **[ask]**

## How he uses Claude today

- **Daily, multi-device.** ~28 Claude.ai magic-link sign-ins in 60 days, across the Electron
  desktop app and Firefox. Logs in most working days, sometimes 3–4x/day. **[obs]**
- **Ships real software with it.** `✂Trace Trimmer` — a GUI tool that trims CAN log trace
  files, with a toolbar, update mechanism, startup-time budget, and parsers for vendor
  formats ("insight can converter"). This is a genuine internal tool serving his day job. **[obs]**
- **Writes spec-grade prompts.** His TickTick task bodies read like well-formed Claude
  prompts — exact file-name grammar, worked examples, acceptance criteria. He is already
  well above average at prompting. **[obs]**
- **Has a `@claude` tag** in TickTick to mark tasks he intends to hand to Claude. **[obs]**
- **Runs scheduled Claude routines**, including a morning email review (this tip rides on
  that slot). **[obs, from the routine brief]**
- Follows AI news via **TLDR newsletter** (reads the Opus 5.5 / GPT-6 issues). So he gets
  model news already — he does *not* need me to relay model launches. **[obs]**

## Observed gaps / leverage hypotheses

Ranked by expected payoff. Each becomes a candidate daily tip.

1. **Requirements live in prose, not in executable gates.** His own Trace Trimmer task says:
   *"Make a rule that will definitely see whenever I start claude in this folder that the
   start-time must always be under 1 second. Test this each time you make a change... you
   must keep trying until you do fulfill this requirement."* That is a CLAUDE.md rule + a
   check script + a hook, hand-rolled as English. Highest-value fix. **[obs]** → Tip 001
2. **No evidence of CLAUDE.md / .claude/ config** in his projects. **[inf]** **[ask]**
3. **No evidence of subagents or parallel worktrees** — likely single-threaded sessions. **[inf]** **[ask]**
4. **Backlog decay**: `💻Remote Work` and `✂Trace Trimmer` tasks were last touched Oct 2025
   and are ~11 months stale, while the underlying work (trace files, income) is still live
   in Sep 2026 mail. Suggests capture is good, follow-through is the bottleneck. **[obs]**
5. **Re-auth friction**: signing in via emailed magic link several times a day is minutes/week
   of pure friction. Low value but trivially fixable. **[obs]**
6. **Freelance funnel is manual** — Upwork applications, CV, LinkedIn all sit as undone
   tasks. A strong Claude-assisted candidate, and it is directly revenue-generating. **[obs]**

## Constraints he set for this routine

- **≤15 minutes per day**, total, including answering my questions.
- **Output that earns money beats workflow polish.** Do not optimise the workshop instead of
  building the furniture.
- **He creates his own tasks and schedules his own routines.** I propose; I never create
  crons or TickTick tasks on his behalf.
- One tip per day, delivered in the morning email-review slot.
