# Tip pipeline

One per day, each **under 15 minutes to act on**. Ordered by (impact on earning capacity)
x (fit to a fragmented student/work day) / (setup cost). Reorder freely as answers land.

Status: `queued` / `sent` / `dropped`. Sent tips move to `log.md`.

## Tier 1 — reliability foundations (must come first; everything else stacks on these)

1. `sent 2026-09-28` **Encode the "done" contract in CLAUDE.md** instead of re-typing it per
   task. Direct evidence: your startup-time ticket spells out test-after-each-change /
   keep-going-until-met / report-the-number. Write it once.
2. `queued` **One hook beats ten reminders.** A `PostToolUse` hook that runs the fast test or
   lint after every edit turns "please test it" from a hope into a mechanism. ~10 min for one hook.
3. `queued` **Plan mode as a gate, not a formality.** The 2026 consensus loop is
   research → plan → execute → review → ship with you approving at the plan gate. Costs 2
   minutes, saves whole wrong implementations. Try it on the next Trace Trimmer GUI ticket.
4. `queued` **CLAUDE.md ≤ 200 lines + `.claude/rules/*.md` with path globs.** Long CLAUDE.md
   files get diluted; scoped rules load only when the matching files are touched.
5. `queued` **Never let an unattended agent push to main.** Branch + PR gate. This is the
   precondition for trusting anything that runs while you're at the conservatory.

## Tier 2 — throughput multipliers (the things you asked about)

6. `queued` **Parallel review with three lenses.** Spawn subagents for correctness, then
   performance, then tests on your own diff before you read it. Cheap, no setup, and it's the
   single best-documented subagent win.
7. `queued` **Agent teams for competing hypotheses** (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`).
   Built for exactly your class of bug: several teammates each test a different theory and try
   to *disprove* each other, which beats one agent anchoring on its first plausible answer.
   Start on research/debug tasks, not parallel code-writing.
8. `queued` **Claude Code Projects (beta, Sep 2026): cloud threads that keep running after you
   close the laptop.** Potentially the best fit for your schedule of anyone — queue work before
   a lecture, review after. Check whether your tier has the beta.
9. `queued` **Turn your repeated Trace Trimmer workflow into a Skill.** "Add a new trace
   format" is clearly a recurring shape of task. Write the skill once, stop re-explaining.
10. `queued` **Close the `@claude` loop.** You already tag TickTick tasks `@claude` and nothing
    consumes them. A routine that picks up tagged tasks, drafts the work on a branch, and
    reports back is the highest-leverage routine you don't have yet.
11. `queued` **Git worktrees** so two sessions can run on one repo without fighting over files.
12. `queued` **Cheap workers, expensive lead.** `CLAUDE_CODE_SUBAGENT_MODEL` lets parallel
    workers run on a smaller model while the lead stays sharp — the usual fix when fan-out
    gets expensive.
13. `queued` **3–5 agents is the sweet spot**, not more. Coordination overhead and
    summary-merging eat the gains past that. Useful guardrail before you over-invest.

## Tier 3 — money-facing (promote hard if Q1 says freelance)

14. `queued` **Upwork proposal skill.** Store your CV, Trace Trimmer case study and rate once;
    generate a tailored proposal in ~2 minutes. "Apply for 1 upwork post" stops being a chore.
15. `queued` **Generate the Trace Trimmer case study** — a CAN-trace tooling story is a
    credible, specific portfolio piece for Toptal/Proxify screening.
16. `queued` **Make the TLDR backlog self-processing.** You have a fortnight of unread AI
    newsletters. A routine that extracts only items actionable *for your stack* converts
    reading debt into a two-line digest.
17. `queued` **Rate/scope sanity check before you bid** — have Claude estimate the job against
    your actual velocity so you don't underbid student-hours.

## Tier 4 — measurement and restraint

18. `queued` **Eval your own setup.** Before/after on a fixed task after you change CLAUDE.md,
    otherwise you're tuning blind. ("Proper agent evals" was in your unread TLDR.)
19. `queued` **The harness tax.** Some tasks genuinely lose to agent overhead — small, local,
    well-understood edits. Knowing when to just type the code is a real skill and it was also
    in your unread newsletters ("don't go all-in on AI", "don't turn your brain off").

## Tier 5 — personal (gate on Q7)

20. `queued` Dutch vocabulary spaced-repetition routine off `🇳🇱Nederlands Woordenschat`.
21. `queued` Obsidian vault as durable agent memory across sessions.
22. `queued` Goal-review routine that reads `✨Goal Reviews` and asks the three questions you'd
    otherwise skip.
