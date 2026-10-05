# Tip pipeline — researched, ranked, not yet delivered

Ranked by *(expected workflow gain) / (minutes to adopt)*, filtered to what fits John's
situation: solo dev on a Python desktop app, ≤15 min/day, money-output first, music school
eating the calendar. Re-rank as answers to `questions-backlog.md` come in.

## Delivered
- **001 — 2026-10-05 — Stop hook as an enforced quality gate** (`tips/2026-10-05-verification-gate/`).
  Turning the hand-written "keep trying until startup < 1s" instruction into a `Stop` hook.

## Next candidates (highest first)

1. **A fixture-diff regression check for Trace Trimmer.** One known trace file in, byte-compare
   the trimmed output against a saved expected file. ~15 min to create, and it is the single
   thing most likely to catch Claude breaking the `insight` format handling while editing
   something unrelated. Natural follow-on from tip 001; the gate exists, this fills it with a
   real correctness signal. *Gate on Q2/Q6.*

2. **`CLAUDE.md` as a 15-line context file, not a rulebook.** Exact build/run/test commands,
   the file-format quirks (`can_log_[ip]_[start]_[end]`, the `;`-prefixed insight header), and
   the startup budget. Stops re-explaining the project every session. Keep it short — long
   files cause rules to get lost, which is precisely why prose rules failed before. *Gate on Q2.*

3. **Plan mode before big changes.** For multi-file work (the GUI time-selector rework), have
   Claude produce a plan and approve it before any edit. Cheapest possible defence against a
   confidently wrong 10-file diff. Near-zero setup, pure habit change.

4. **Close the TickTick → Claude loop.** The `@claude` tag is already there and task
   descriptions are already written as prompts. Wiring that up so a tagged task flows straight
   into a session removes the daily copy-paste. Needs Q5 answered first (and this one he'd
   schedule as its own routine — a build task, not a morning tip).

5. **Subagents for the review pass, not the writing.** The realistic first use for a solo dev:
   after a change, a read-only reviewer agent (Read/Grep/Glob only) checks the diff against the
   project's own rules. Permissions inherit from the lead session, so a read-only subagent is
   the safe first step. *Gate on Q3 — needs terminal Claude Code.*

6. **Parallel worktrees — deliberately placed late.** Multiple agents sound like the big win and
   are the thing John named first, but for one developer on one desktop app they mostly add
   merge pain. Worth it only once (a) there's a test suite to catch cross-agent breakage and
   (b) there are genuinely independent work streams — e.g. Trace Trimmer features vs. a
   freelance client project. Revisit after 1 and 2 land. Guidance is consistent: don't exceed
   ~3 parallel agents, and only with real ownership boundaries.

7. **Model choice per task.** Haiku for summarising, Sonnet for implementation, Opus for
   security/architecture review. Mostly matters for cost and speed. *Gate on Q11.*

8. **Freelance-specific:** a reusable skill for turning a job post into a tailored proposal from
   a stored CV + project inventory. Directly money-generating rather than workflow polish, so it
   jumps the queue if Q1 says freelance is the engine.

9. **Teaching-specific (Codementor/Wyzant):** packaging explanations and worked examples. Jumps
   the queue if Q1 says teaching.

## Explicitly deprioritised, with reasons
- Heavy multi-agent orchestration / agent teams — cost and coordination overhead don't pay back
  for one person on one small app yet. See 6.
- MCP server authoring — no evidence of a need; the connectors in use already cover it.
- Elaborate custom slash commands — premature before `CLAUDE.md` and a test signal exist.
