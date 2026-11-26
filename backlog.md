# Tip backlog — ranked, one per day, each ≤15 min

Ranking = (reliability or time saved) × (fits John's actual stack) ÷ (minutes to adopt).
Re-rank whenever `profile.md` changes. **Never schedule anything for him** — tips end with a
suggestion he books himself.

## Delivered

| Day | Date | Tip | Status |
|-----|------|-----|--------|
| 1 | 2026-11-26 | Turn the "must start in under 1s" wish into a hook + executable check | sent |

## Tier 1 — reliability of unattended work (his own stated pain)

2. **CLAUDE.md as the project's always-on facts**, not its wishes. Build/run/test commands, where the
   CAN parsers live, the <1s rule. Under 200 lines; anything longer is a skill or a rule.
3. **Scoped `.claude/rules/` with a `paths:` field** instead of one swelling CLAUDE.md — a parser rule
   that only loads when touching the trace-parsing files costs nothing on a GUI-only session.
4. **Evidence-based "done"**: require the pasted command output *and* exit code in the completion
   message. A "done" without them isn't done. One line in CLAUDE.md.
5. **Fresh-context reviewer before merge** — `/code-review` or a reviewer subagent that never saw the
   code being written, to defeat self-grading bias.
6. **Spec the acceptance criteria in the TickTick item itself.** He already writes prompt-shaped
   tasks; adding 2 lines of "done when: X exits 0, Y under 1s" makes them runnable unattended.

## Tier 2 — throughput (his own suggestions: multiple agents, roles, continuous work)

7. **Subagents for noisy exploration.** CAN traces and logs are the perfect case: the subagent burns
   its own context reading a 200k-line trace and returns only the finding.
8. **Git worktrees for genuine parallelism** — one worktree per task, never two agents in the same
   files, 2–3 concurrent max because *he* becomes the merge bottleneck.
9. **Coordinator → specialists → verifier** role split, with the verifier checking against the spec
   rather than against the implementation.
10. **`/loop` with a checkable goal** for self-paced autonomous work — and the rule that no test means
    no definition of done, which means no loop.
11. **Background tasks instead of babysitting**: long builds/test runs in the background, notification
    on exit, rather than watching the terminal.
12. **Skills for the repeatable procedures** — packaging/releasing Trace Trimmer, the new-parser
    checklist. A 30-line procedure belongs in a skill, not in his head.

## Tier 3 — the TickTick → Claude pipeline he half-built already

13. **Drain the `@claude` tag**: a routine that picks up tagged tasks, researches, writes the answer
    into the task, and leaves the decision to him.
14. **Weekly backlog grooming routine** for Trace Trimmer — turn vague items into specs with
    acceptance criteria, so weekday sessions start from runnable work.
15. **One task per session, clear context between** — cheapest reliability win there is.
16. **`/fewer-permission-prompts`** to build an allowlist, killing the approval fatigue that makes
    long unattended runs stall.

## Tier 4 — time-to-money

17. **Project inventory → CV/LinkedIn/Upwork profile in one pass.** He already has the checklist task
    (A45, CAT 330z, Hilux, Fendt, HX90, HBM, BellMarine, CCS Discharge); Claude turns it into three
    artifacts from one input.
18. **Proposal drafting loop for Upwork** — a skill holding his positioning, so each proposal is
    5 minutes not 30.
19. **Trace Trimmer as a portfolio artifact** — a README, a screenshot, a 60-second demo. Embedded
    contracting clients buy evidence.
20. **Teaching positioning** (Codementor/Wyzant): embedded + CAN + Python is a thin, well-paid niche.
21. **AIM award application** — deadline 1 Dec; a draft from his own notes is a 15-minute job.

## Tier 5 — personal / learning (only if he wants them in rotation — Q9)

22. **Obsidian as the output sink** — Claude writes notes in, he reviews, instead of chat scrollback.
23. **Dutch vocabulary**: his `🇳🇱Nederlands Woordenschat` list → spaced-repetition drills.
24. **Transcription and practice-plan generation** for Zuyd theory/piano homework.
25. **Goal-review prep**: a routine that assembles the review inputs so the review itself is thinking,
    not gathering.

## Tier 6 — hygiene

26. **Model and effort choice**: higher-capability model for planning and gnarly debugging, cheaper for
    mechanical edits; effort is the first dial, not the model.
27. **Prompt the plan, review the plan, then let it run** — plan mode for anything touching the parsers.
28. **`/simplify` after a feature lands**, to stop AI-written code sprawling.
