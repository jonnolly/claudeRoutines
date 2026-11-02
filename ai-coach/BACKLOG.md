# Ranked backlog — one item per day, each ≤15 minutes

Ordering rule: (direct effect on money-earning output) × (reliability gained) ÷ (minutes).
Anything that can't be done or answered inside 15 minutes gets split until it can be.
Mark items `DONE`, `SKIPPED` or `BLOCKED` with the date. Delivered tips are logged in TIPS.md.

---

## Tier 0 — profile questions (answer these and every later tip gets sharper)

These are questions *for John*, each answerable in 1–3 minutes. Highest-value first.
Answers get written into PROFILE.md by the next run.

- [ ] **Q1. Rough weekly split of your Claude use?** Code/firmware · log & fault diagnosis ·
      customer/colleague email · Jira & planning · research/learning · personal/music.
      Even "60/0/20/10/10/0" is enough. *This single answer re-ranks this whole backlog.*
- [ ] **Q2. What is the one task that eats the most of your week and feels most repetitive?**
      (Say it in one sentence, as you'd say it to a colleague.)
- [ ] **Q3. What may Claude do unattended, and what must it always ask first?**
      e.g. draft Gmail replies = OK unattended, send = never; create Jira issues = ask;
      open PRs = OK on a branch. This unlocks "agents working while you're at school".
- [ ] **Q4. Where do you actually run it?** claude.ai chat · Claude Code in a terminal ·
      cloud sessions from the app · desktop app. And: do you have a code repo you work in
      regularly that this session could be granted access to?
- [ ] **Q5. Which output converts most directly to money** — for New Electric, and separately
      for you? (Faster fault resolution? Fewer service callouts? Proposals? Something else?)

## Tier 1 — reliability & memory (cheap, compounding)

- [x] **T1.1 Fix the Atlassian MCP connector (v1→v2).** ~5 min. Jira is currently invisible
      to every routine and session. *Delivered as Tip #1, 2026-11-02.*
- [ ] **T1.2 One context file, read by everything.** Put your standing context in
      `ai-coach/PROFILE.md` (already started) and mirror the work-specific part into a
      `CLAUDE.md` in whatever repo you work in: company, products, pack/BMS vocabulary,
      who's who, how you like replies written. Stop re-explaining yourself every session.
      ~15 min, pays back the same week.
- [ ] **T1.3 Make the morning email review write its own state.** Have it append a one-line
      ledger (threads seen, what it drafted, what it deferred) to a file in this repo, so
      tomorrow's run knows what yesterday did instead of starting blind. ~10 min of prompt
      editing. This is the single biggest weakness of routine-based workflows.
- [ ] **T1.4 Name the "never do this" rules once, in writing.** A short policy block in
      PROFILE.md (never send email, never transition Jira, never push to main) is what makes
      it safe to let routines do more. ~5 min.

## Tier 2 — turn your actual job into reusable assets

- [ ] **T2.1 A `diagnose-pack-fault` skill.** Your precharge-timeout threads look like the
      same shape every time: symptom → log/CAN evidence → likely cause → what to ask the
      customer → escalation. Write that once as a Claude Skill (a folder with a SKILL.md)
      and every future fault starts at step 3 instead of step 0. Draft the SKILL.md in 15
      min from one past thread; refine it the next time a fault comes in.
- [ ] **T2.2 Reply-draft routine, drafts only.** A routine that, each morning, reads
      overnight customer threads and leaves *Gmail drafts* (never sends) in your voice.
      You review and hit send. Needs Q3 answered first. Setup is one prompt; you schedule it.
- [ ] **T2.3 Jira hygiene pass.** Once the connector is fixed: a 10-min weekly routine that
      lists your open NEP issues, flags the ones with no movement and drafts the status
      comment you'd have written. You post them.
- [ ] **T2.4 Field-report → Jira issue in one step.** Paste the raw customer email, get a
      properly-structured issue draft (summary, steps, evidence, suspected subsystem).

## Tier 3 — working style (habits, near-zero setup cost)

- [ ] **T3.1 Plan before diff.** For anything touching more than one file or one subsystem,
      make Claude write the plan first and approve it before it acts. The most consistently
      reported quality win in 2026 agentic-coding practice ("spec is the source of truth").
      0 min setup, saves the rework hour.
- [ ] **T3.2 Make it reproduce before it fixes.** Demand a failing test / a repro of the
      fault *first*, then the fix, then the same check passing. Turns plausible answers into
      verified ones — the main failure mode of AI debugging on hardware problems.
- [ ] **T3.3 Fan out, don't queue.** When a question needs several independent lookups
      (three log files, two docs, one datasheet), ask for them in parallel subagents and keep
      the main thread for the conclusion. Minutes instead of a long serial crawl.
- [ ] **T3.4 One task per session, short sessions.** Long sessions degrade; a fresh session
      with a good context file beats a 200-message one. Scratch files, not scrollback, are
      the memory.
- [ ] **T3.5 Review the diff with a second pass.** `/code-review` (and `/security-review`
      before anything leaves your machine) catches what the writer missed, because the
      reviewer isn't anchored on having just written it.

## Tier 4 — orchestration (only once Tier 1–2 are real)

- [ ] **T4.1 Role-based agents** (`.claude/agents/*.md`): a diagnostician, a reviewer, a
      writer-in-your-voice. Roles beat one general prompt mainly because each gets a clean,
      narrow context — not because of the persona.
- [ ] **T4.2 Continuously-working agents**: `/loop` and background tasks for things that
      genuinely wait on external state (a long test run, a CI job, a field log arriving).
      Honest caveat: continuous agents mostly burn tokens unless there's a real external
      signal to wait on. Worth doing *after* T2.2, not before.
- [ ] **T4.3 Hooks over instructions.** A hook always fires; a line in CLAUDE.md is advice
      the model may skip. Use hooks for lint/format/test gates.
- [ ] **T4.4 Version-control your routines.** Keep each routine's prompt in this repo so you
      can diff and improve them instead of editing blind in the app UI.

## Tier 5 — personal / life-goal use (lower priority, he asked for it when strong)

- [ ] **T5.1 Weekly Goal Review co-pilot.** Feed completed TickTick tasks + Goal Reviews
      project into one 10-min retro that names a single bottleneck and one experiment.
      Fits a system he already runs — low adoption cost.
- [ ] **T5.2 Obsidian inflow.** The "♦Add to Obsidian" queue is a backlog; a weekly routine
      can turn it into filed, linked notes instead of a growing list.
- [ ] **T5.3 Practice-plan generation.** Zuyd assignments → a week of concrete, timed piano
      practice blocks. Useful only if the music work is time-pressured right now.

---

## Parked (good ideas, >15 min or need something first)

- Prompt caching / API-level work — only relevant if he builds something on the API.
- MCP code-execution patterns, custom mods/panels, plugin authoring.
- Multi-agent Workflow scripts — expensive; needs a real repeated pipeline to be worth it.
