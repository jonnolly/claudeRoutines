# Usage profile — John Connolly (john@newelectric.nl)

Last updated: 2026-10-22 (run 1). Everything in **Observed** is evidence-based;
everything in **Assumed** needs confirming via `questions.md`.

## Observed (evidence in brackets)

### Who / context
- Software engineer at **New Electric** (NL, marine electric propulsion) [email domain];
  works on **CAN bus / vehicle-trace tooling** [CanTraceSplitter repo, "insight can converter" tasks].
- Simultaneously a **first-year student at Zuyd** (jazz/music) [TickTick: "Zuyd First Year",
  "Zuyd Preparatory Jazz", piano practice, theory homework, recording + gig projects].
  => time is genuinely scarce; the 15-min cap is not a preference, it is the constraint.
- Actively trying to **generate income**: Upwork / Toptal / Proxify / Codementor profiles,
  teaching, part-time or Christmas-period contracts [TickTick "Remote Work", 10 open tasks,
  stalled since 2025-10-15].
- Languages/stacks seen: **Python** (primary), C#, C++, WPF, LaTeX. Windows + **WSL**
  [hardcoded `/mnt/c/Users/Lenovo/...` paths in test_app.py].
- Tools in orbit: **TickTick** (task system of record), **Obsidian** [“Add to Obsidian” project],
  Gmail (2080 inbox threads, 26 unread), Google Drive [Gratitude_Journal writes to Drive].

### How Claude is used today
- **Claude Code on real repos.** `CanTraceSplitter` ("Trace Trimmer") is the main one —
  a PyInstaller-packaged GUI tool for trimming CAN trace files; `.claude/settings.local.json`
  exists, so he runs the CLI there. `Gratitude_Journal` (Python, Drive-backed) is a second.
- **Scheduled cloud routines.** This repo (`claudeRoutines`) exists purely to back them;
  a morning email-review routine runs daily.
- **TickTick as the prompt inbox.** Tasks tagged `@claude` are work he intends to hand to
  Claude. Several task *descriptions are effectively prompts*, e.g. the insight-converter
  spec and: *"reduce start-up time ... Make a rule that will definitely see whenever I start
  claude in this folder that the start-time must always be under 1 second. Test this each
  time you make a change ... keep trying until you fulfil this requirement."*
- **Claude as an advisor, not just a coder.** A dedicated `🟥Claude questions` project parks
  non-code questions (e.g. retirement-fund strategy, with a note to describe the situation in
  a private browser) — so personal/life-goal use is in scope and wanted.

### Gaps found by inspection (these drive the tip backlog)
- **No `CLAUDE.md`** in CanTraceSplitter (only `.claude/settings.local.json`); project rules
  live in `DEVELOPMENT.md`, which is *not* auto-loaded. Durable rules are therefore being
  retyped into prompts and TickTick tasks instead of being loaded every session.
- **No hooks** → the "test it every time, keep trying until it passes" rule is advisory only.
- **The test suite can pass vacuously.** `test_app.py` tests 4 and 5 point at hardcoded
  absolute WSL paths — and the two paths disagree (`2_Areas` on line 147 vs `2 Areas` on
  line 190). When a path is missing they print a warning and `return 0, 0`, so the suite
  still prints "✅ ALL TESTS PASSED" and exits 0. The repo's own `testfiles/` dir is unused.
- **`parse_timestamp` is re-defined inside the test** (line 45) instead of imported from
  `app.py`, so that test can stay green while the app's version drifts.
- **No CI** (`.github/workflows` absent) → nothing catches the above on push.
- No evidence yet of: subagents, skills, plan-mode discipline, worktrees, parallel sessions,
  `/clear` hygiene, fan-out (`claude -p` / `/batch`).

## Assumed — confirm before relying on it
- Which Claude surfaces he actually uses (CLI vs desktop vs claude.ai chat vs cloud vs mobile)
  and roughly how many hours a week. **Everything about hooks/worktrees/parallel sessions is
  moot if he mostly works in chat.**
- Which plan he's on and whether usage limits bite (decides whether fan-out/multi-agent,
  roughly 15x the tokens of chat, is even affordable).
- Whether work code at New Electric can be touched by Claude at all, and whether it lives
  anywhere Claude can reach (the public repos may be the personal slice of a bigger job).
- What the money target actually is this quarter: Upwork contracts / teaching / productising
  Trace Trimmer / a raise at New Electric.

## Answers from John
*(append answers here, newest first, with the date. Future runs: read this first.)*

- _nothing yet — run 1 asked Q1, Q2, Q4._
