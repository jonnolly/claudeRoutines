# Tip backlog — ranked

Re-ranked 2026-09-21 after round 2. The ranking test that now governs everything:
**does this subtract from his Monday/Thursday review load, or add to it?** He has
two office days and two 2-hour remote days. Agent capacity is free; his attention
is not.

Strike items through when delivered.

## Tier 1 — next up

1. ~~**Stop being the runtime.** Drain the "ask claude …" queue with a scheduled
   routine + subagent per task.~~ → Tip 001, 2026-09-21.

2. **One set of standards, loaded everywhere.** *(next tip)* `~/.claude/CLAUDE.md`
   loads in every session regardless of project; project and directory files layer
   on top, more specific winning. So `claudeCodingStandards.md` lives once, the
   global file imports it, projects override only what they must. Keep it lean: a
   line earns its place only if removing it would make someone pick the wrong file
   or command.

3. **Make the verification loop run, not just be written.** His standards already
   specify reproduce → test → fix → verify. A document is a hope; a skill is a
   mechanism. **This is the highest-value tip in the list for him specifically**,
   because it is the one thing that directly shrinks Thursday's review pile: work
   that has checked itself needs less of him. Deliver immediately after #2.

4. **Widen the Tue/Wed hand-off from one lane to several.** He already plans tasks
   on his remote days, hands them to Claude, and reviews in the office — and says
   it works. The upgrade is not a new habit, it's throughput: several independent
   tasks handed off per remote day instead of one, each in its own context, each
   arriving pre-verified. Pair with #3 so widening doesn't multiply his reading.

5. **A better hand-off spec.** The other half of #4. Two remote hours is a small
   window to specify work in; what he writes on Tuesday determines what he reads on
   Thursday. Cover: what a task must contain to survive unattended execution, how
   to say what "done" means, and when to insist on a plan before any edit.

6. **Automate the out-of-date half of the TickTick tidy.** *(promoted — he costed
   it)* 5 minutes to 1.5 hours a day, mostly rescheduling stale tasks; he estimates
   partial automation gets it to ~15 minutes. At the top of the range that is the
   biggest single block of time any tip here can return. Scope it to the mechanical
   part only — surfacing overdue items, proposing reschedules, catching misfiring
   recurrence rules, flagging duplicates (≈40 copies of one recurring task exist) —
   and leave the judgement calls to him.

## Tier 2 — New Electric: the weekly meeting complex

These four are one programme, not four tips. Sequence them.

7. **Revive the NESL board as the source of the weekly ball.** The board is dead —
   tasks get added when someone remembers, never reviewed. An agent can groom it
   into something a 10-minute meeting slot can actually work from: deduplicate,
   age-sort, break the big items into week-sized pieces.

8. **Break long-term goals into week-sized tasks, one owner per week.** His own
   design: "who has the ball this week?", a physical ball on a desk, returned to the
   middle table by the next meeting. The scaffolding he's missing is the generator —
   something that takes a long-term goal (CI improvements first) and keeps producing
   the next genuinely achievable weekly slice.

9. **A vision worth looking at.** He asked for this directly: the motivating picture
   is currently "a google doc… which is very dry." Build it — but the content must
   come from him. Needs the current doc, or 20 minutes of him talking. Never invent
   New Electric's roadmap. Candidate for a published artifact the team opens each
   week, ideally showing live progress rather than a static poster.

10. **A meeting agenda that assembles itself.** Once 7–9 exist, the weekly meeting
    prep becomes: what moved, whose ball it was, what the board says, what's next.

## Tier 3 — documentation

11. **Structure first, in the empty space.** `NE_EMBEDDED_SOFTWARE_LIBRARY` is
    completely unused — a greenfield Confluence space is the safest possible place
    to prove a documentation structure before touching `Software Development`,
    `CAT_330z_Battery` or `NEP_006_HX70`, which are in active use but poorly
    organised. Demonstrate there, then migrate.

12. **Documentation that notices it has gone stale.** Work repos are on GitHub and
    he wants them wired to Confluence so a code change that invalidates a page
    updates it. Start with **detection** — pages whose subject changed and whose
    text didn't — before anything writes. **Blocked**: this session's GitHub access
    covers only `jonnolly/claudeRoutines`; the work repos need access granted.

13. **BookStack consolidation.** Inventory and overlap map first, migration proposal
    second, BookStack left read-only in place for the teams still using it. Never a
    bulk move. **Blocked** on API access — the responsible colleague is on holiday;
    John has a task to ask next week.

## Tier 4 — reliability, craft, held in reserve

14. **Hooks as guardrails** — deterministic enforcement that doesn't depend on the
    model remembering. The tier above CLAUDE.md; natural successor to #2 and #3.
15. **Subagents for bounded, noisy work** — isolated context, only the summary returns.
16. **Choose the parallel mode from the failure you're preventing.** Context overload
    → subagent; file collision → worktree; coverage → teams.
17. **Git worktrees** — only if a project genuinely needs two independent edits at
    once. Teams report 4–8 per developer; for him the review ceiling binds first.
18. **Assign roles deliberately** (implementer / reviewer / sceptic).
19. **Plan mode before any edit.** The five-minute tip; reserve for a week where the
    larger tips aren't landing.
20. **Context transfer between sessions** — ending a session so the next starts warm.
    Fits his fragmented week exactly.
21. **Trust calibration** — ~29–46% of developers trust AI output; 46–68% report
    quality problems. The teams who do well have checks, not faith.
22. **Spec-driven work** — speed gains evaporate without specification discipline.
23. **Token efficiency** — fewer retries, stronger first passes. Argue it in time.

## Tier 5 — personal, life, learning

24. **Claude as mentoring support** for the colleague he's covering on Tue/Wed —
    onboarding notes, worked examples, review explanations that teach rather than
    just correct. Reduces a recurring load nobody has costed.
25. **A practice-plan agent that remembers** — jazz piano plans that compound
    instead of restarting each time.
26. **The CBT / reflection profile**, persistent, with the gratitude journal and
    goal reviews as context.
27. **Decision support for the big open questions** — mortgage, retirement,
    Maastricht vs. Utrecht. One maintained document beats twelve restarted chats.
28. **Job-hunt agent** for the free days: standing brief, sources, weekly shortlist.
29. **The two-account TickTick problem.** Revisit only if #6 doesn't get him to ~15
    minutes. Warn before any Todoist move: it would likely break the cross-account
    inbox bridge he relies on and uses heavily.

## Answered inline, not worth a tip

- **Desktop app vs. VS Code extension for multi-repo folders** — `/add-dir` and
  `--add-dir` make both work. Logged in `profile/QUESTIONS-FOR-JOHN.md`.
