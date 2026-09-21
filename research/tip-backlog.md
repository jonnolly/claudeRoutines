# Tip backlog — ranked

Built 2026-09-21. Ranked by (leverage for John) × (evidence he isn't doing it)
÷ (effort). Re-rank as the profile fills in. Strike items through when delivered.

## Tier 1 — highest leverage, evidence-backed

1. ~~**Stop being the runtime.** Drain the "ask claude …" queue with a scheduled
   routine + subagent per task.~~ → delivered as Tip 001, 2026-09-21.

2. **Promote `claudeCodingStandards` to a loaded artefact.** He wrote the doc in
   Sept 2025 and asked that it apply across projects — but a doc only works if
   something reads it. Turn it into `~/.claude/CLAUDE.md` (user-level, inherited by
   every project) plus a skill that *runs* the loop rather than describing it.
   Current guidance: lean CLAUDE.md, durable instructions only; a sentence earns
   its place only if removing it would make a contributor pick the wrong file or
   command. Verify first whether he already did this (question 2).

3. **Give Claude a way to check its own work — as a skill, not a paragraph.**
   The single most-cited 2026 practice: a verification loop packaged so every
   session applies the same checks automatically. He has the *policy*; the tip is
   the *packaging*. Pair with #2 or deliver after it.

4. **Plan mode before any edit.** Cheapest reliability win there is, and it costs
   one keystroke. Good "five-minute tip" if a run of big tips goes unadopted.

5. **Point Claude Code at the Obsidian vault.** The vault is plain Markdown on
   disk; Claude Code can `cd` into it and work directly — which turns his
   `♦Add to Obsidian` capture backlog into something an agent can file, link and
   de-duplicate. Also the fix for "my life context lives in chat and evaporates":
   the vault becomes durable, re-readable context. Gate on question 4.

## Tier 2 — the multi-agent material he explicitly asked about

6. **Subagents for bounded, noisy work.** The entry point to parallelism: a
   Markdown file with YAML frontmatter in `.claude/agents/`, scoped tools, its own
   context window, only the summary returning to the main conversation. Right for
   research sweeps, test runs, audits — i.e. anything that would otherwise flood
   his main session.

7. **Choose the parallel mode from the failure you're preventing.** The cleanest
   mental model going: context overload → subagent; file collision → worktree;
   incomplete coverage across many areas → teams/workflows. Stops him adopting
   worktrees for a problem that was only ever context bloat.

8. **Git worktrees for genuinely independent work.** Teams report 4–8 concurrent
   worktrees per developer working reliably in 2026; above that the bottleneck is
   *review*, not Claude. Important framing for a solo dev: parallelism converts
   his time into review time, so don't scale past what he can read.

9. **Assign roles deliberately** (reviewer, implementer, sceptic) rather than
   asking one agent to do all three — he named roles as an interest. Best paired
   with an adversarial reviewer on his own diffs.

10. **Background / async agents** for long-running work: kick it off, get woken
    when it's done, don't sit and watch. Directly serves "continuously working".

11. **Agent teams / dynamic workflows** — parallel instances coordinating through a
    shared git workspace; workflows generate an orchestration script to fan work
    out. Powerful, but research-preview-shaped: hold until he's comfortable with
    6–8, and flag the token cost honestly.

## Tier 3 — reliability, cost, craft

12. **Token efficiency is the real cost lever** — fewer retries and stronger first
    passes save more than a cheaper model. Relevant: his Claude spend is expensed,
    so the argument is time, not money.

13. **Trust calibration.** Only ~29–46% of developers trust AI output; 46–68%
    report quality problems. The teams who do well aren't the trusting ones, they're
    the ones with checks. Frame: build the check, then you can stop reading every line.

14. **Hooks as guardrails** — deterministic enforcement (format, test, block) that
    doesn't depend on the model remembering. The reliability tier above CLAUDE.md.

15. **Context transfer between sessions** — how to end a session so the next one
    starts warm. Relevant to his short, scattered work windows between gigs,
    lessons and a 3.5-day contract.

16. **Spec-driven work for anything non-trivial** — the productivity/reliability
    paradox research: speed gains evaporate without specification discipline.

## Tier 4 — personal, life, learning

17. **A repeatable practice-plan agent** for jazz piano/trumpet: he keeps asking
    Claude for practice plans ad hoc ("scales / chords", "minor, melodic minor").
    Make it a skill with his actual level, repertoire and lesson feedback, so each
    plan builds on the last instead of starting cold.

18. **The CBT/reflection profile he already wanted** ("Create claude profile as cbt
    therapist") — as a persistent project with the gratitude journal and goal
    reviews as context, not a fresh chat each time.

19. **Decision-support agent for the big open questions** — mortgage, retirement
    modelling, Maastricht vs. Utrecht. These are exactly the tasks rotting in his
    list because each needs an uninterrupted hour. One structured document that an
    agent maintains and updates beats twelve restarted conversations.

20. **Let an agent clean the capture system.** ~40 duplicate copies of one
    recurring task sit in `🧔Work to Personal Inbox`. A weekly hygiene routine —
    de-duplicate, surface anything older than 90 days, flag recurrence rules that
    are misfiring — protects the daily review he already does.

21. **Job-hunt agent** for the 1.5 free days: standing brief, sources, weekly
    shortlist. Turns a vague recurring task he keeps re-creating into output.
