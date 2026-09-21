# Tip backlog — ranked

Re-ranked 2026-09-21 after John answered round 1. Ranked by (leverage) ×
(evidence he isn't doing it) ÷ (effort). Strike items through when delivered.

## Tier 1 — next up

1. ~~**Stop being the runtime.** Drain the "ask claude …" queue with a scheduled
   routine + subagent per task.~~ → delivered as Tip 001, 2026-09-21.

2. **One set of standards, loaded everywhere.** *(next tip)* He has
   `claudeCodingStandards.md`, doesn't know if anything reads it, and explicitly
   wants "a standardised way to use claude across all projects … unless otherwise
   specified". The answer is the memory hierarchy: `~/.claude/CLAUDE.md` loads in
   **every** session regardless of project; project `CLAUDE.md` and directory-level
   files layer on top, more specific winning on conflict. So the standards file
   lives once, is imported by the global file, and each project overrides only what
   it must. Include: keep it lean (a line earns its place only if removing it would
   make someone pick the wrong file or command), and the distinction between
   *stating* a rule and *enforcing* one.

3. **Make the verification loop run, not just be written.** His standards already
   say reproduce → test → fix → verify. A document is a hope; a skill is a
   mechanism. Package it so every session applies the same checks. This is the
   single most-cited 2026 practice. Deliver right after #2 — they're two halves.

4. **Documentation that updates itself.** *(new — his own top pain point)* Confluence
   pages at New Electric go stale because nobody remembers to update them after a
   change. He has the Atlassian MCP connector already. Shape: a routine that takes
   the week's merged changes and flags or drafts the Confluence updates they imply,
   rather than trying to auto-publish silently. Start with *detecting* staleness —
   pages whose subject changed and page didn't — before writing anything back.

5. **Consolidating Confluence + BookStack without breaking BookStack.**
   *(new)* `https://wiki.newelectric.ovh/shelves`, abandoned by the software team,
   still load-bearing for other teams. The tip is the safe pattern: agent produces
   an *inventory and overlap map* first (what exists where, what's duplicated, what's
   contradictory, what only exists in BookStack), then a migration proposal with
   BookStack left read-only in place. Never a bulk move. Gate on round-2 question 3.

6. **Async before concurrent.** *(new — answers his question 3 directly)* He has
   never run two Claudes at once. Given a 3.5-day contract, conservatoire days and
   gigs, the win for him is work happening *while he is elsewhere*, not four
   worktrees competing for an attention he doesn't have. Parallelism converts his
   time into review time — and review time is exactly what he's short of. Sequence:
   subagents for context isolation → background/async tasks → worktrees only if a
   project ever genuinely needs two independent edits at once.

## Tier 2 — multi-agent material, once #6 has landed

7. **Subagents for bounded, noisy work.** `.claude/agents/<name>.md`, YAML
   frontmatter, scoped tools, isolated context, only the summary returns. Right for
   research sweeps, test runs, audits.

8. **Choose the parallel mode from the failure you're preventing.** Context overload
   → subagent; file collision → worktree; coverage across many areas → teams.
   Stops him buying worktrees for a context problem.

9. **Git worktrees.** 4–8 concurrent per developer is what teams report working in
   2026; past that the bottleneck is review. Frame honestly for a solo, time-poor dev.

10. **Assign roles deliberately** (implementer / reviewer / sceptic) — he named roles
    as an interest. Best demonstrated with an adversarial reviewer on his own diff.

11. **Agent teams / dynamic workflows.** Parallel instances coordinating through a
    shared git workspace. Hold until he's comfortable with 7–9; flag token cost.

## Tier 3 — reliability, cost, craft

12. **Hooks as guardrails** — deterministic enforcement that doesn't rely on the
    model remembering. The tier above CLAUDE.md. Natural successor to #2 and #3.
13. **Plan mode before any edit.** The five-minute tip; hold in reserve for a week
    where the big tips aren't landing.
14. **Token efficiency is the real cost lever** — fewer retries, stronger first
    passes. His spend is expensed, so argue it in time, not money.
15. **Trust calibration.** Only ~29–46% of developers trust AI output; 46–68% report
    quality problems. The teams who do well have checks, not faith.
16. **Context transfer between sessions** — ending a session so the next starts warm.
    Fits his short, scattered work windows.
17. **Spec-driven work for anything non-trivial** — the productivity/reliability
    paradox: speed gains evaporate without specification discipline.

## Tier 4 — personal, life, learning

18. **A practice-plan agent that remembers.** He keeps asking for jazz piano plans
    ad hoc ("scales / chords", "minor, melodic minor"). Make it persistent, with his
    level, repertoire and lesson feedback, so plans compound instead of restarting.
19. **The CBT / reflection profile he already wanted**, as a persistent project with
    the gratitude journal and goal reviews as context — not a fresh chat each time.
20. **Decision-support for the big open questions** — mortgage, retirement,
    Maastricht vs. Utrecht. One maintained document beats twelve restarted chats.
21. **The two-account TickTick problem.** Parked at his request. Revisit if round-2
    question 1 comes back with a real number. Note: moving work to Todoist would
    likely break the cross-account inbox bridge he relies on — flag that before he
    does it, not after.
22. **Job-hunt agent** for the 1.5 free days: standing brief, sources, weekly
    shortlist. Turns a recurring task he keeps re-creating into output.

## Answered inline, not worth a tip

- **Desktop app vs. VS Code extension for multi-repo folders** — `/add-dir` and
  `--add-dir` make both work. Logged in `profile/QUESTIONS-FOR-JOHN.md`.
