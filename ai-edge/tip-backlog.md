# Tip backlog — ranked

Rank = (effect on reliable, money-making output) ÷ (minutes to adopt).
Every action must fit in ~10-12 minutes. Pop from the top; re-rank each run.
`[D]` = delivered (see `delivered.md`). Strike nothing out — move it to delivered.

---

## 1. [D 2026-10-22] Your test suite can report green while testing nothing
**Evidence:** `test_app.py` tests 4 and 5 use hardcoded absolute WSL paths that disagree
with each other (`.../2_Areas/...` line 147 vs `.../2 Areas/...` line 190); on a missing
path they warn and `return 0, 0`, so `main()` still prints "✅ ALL TESTS PASSED" and exits 0.
The repo's own `testfiles/` directory is never used. `parse_timestamp` is re-defined inside
the test (line 45) rather than imported from `app.py`.
**Why it is the #1 tip:** the official guidance is that the one thing that lets you walk away
from a session is a check Claude can run. A check that silently degrades to green is worse
than no check — it converts "I verified it" into "I believe it".
**Action (~12 min):** one prompt in the repo, then review and commit.
> In test_app.py the fixture dir is hardcoded twice with different absolute paths and a
> missing dir returns (0,0) so the suite exits 0 having tested nothing. Make the fixture
> dir repo-relative (`testfiles/`, overridable by env var), make a missing or empty fixture
> dir a FAILURE not a warning, and import parse_timestamp from app.py instead of redefining
> it. Then run the suite and show me the output before and after.
**Source:** code.claude.com/docs/en/best-practices — "Give Claude a way to verify its work".

## 2. Turn the rule you keep retyping into a Stop hook
**Evidence:** TickTick task: *"Make a rule that will definitely see whenever I start claude
in this folder that the start-time must always be under 1 second. Test this each time you
make a change ... keep trying until you fulfil this requirement."* There is no startup-time
test and no hook — so the rule only exists while that sentence is in the prompt.
**Action (~12 min):** ask Claude to add `test_startup_time.py` asserting cold start < 1.0 s,
wire `python test_app.py` into a **Stop hook** in `.claude/settings.json` so a turn cannot end
until it exits 0, then delete that sentence from your prompts forever.
Hooks are deterministic; CLAUDE.md lines are advisory. Depends on tip 1 (fix the check first).
**Source:** best-practices, "As a deterministic gate" + /docs/en/hooks.

## 3. A 15-line CLAUDE.md per repo, and `/context` to prove it loaded
**Evidence:** CanTraceSplitter has only `.claude/settings.local.json`; the conventions live in
`DEVELOPMENT.md`, which is not auto-loaded. So every session starts without them.
**Action (~10 min):** `/init`, then cut it to the lines that would cause a mistake if removed:
build command, how to run the suite, the <1 s startup rule, WSL path conventions, release
ritual. Run `/context` to confirm it loaded. Prune anything Claude already gets right —
a bloated CLAUDE.md means the real rules get ignored.
**Source:** best-practices, "Write an effective CLAUDE.md".

## 4. Explore → Plan → Code for anything multi-file
**Evidence:** open GUI tasks ("only the available start/end times selectable", default
end-time read from the file, update-notification pop-up + toolbar entry) each touch several
files — exactly where jumping straight to code solves the wrong problem.
**Action (~2 min to learn, saves hours):** `Shift+Tab` to plan mode, have Claude read the
relevant files and write a plan, `Ctrl+G` to edit the plan in your editor, then approve and
implement. Skip it when you could describe the diff in one sentence.
**Source:** best-practices, "Explore first, then plan, then code".

## 5. Let Claude interview you, then implement in a fresh session
**Evidence:** his TickTick task bodies are already half-specs (the insight-converter one is
two paragraphs of real requirements) — but they are written once, by hand, in the dark.
**Action (~12 min):** paste the minimal idea and *"Interview me in detail using the
AskUserQuestion tool. Ask about implementation, edge cases and tradeoffs. Don't ask obvious
questions. Keep going until we've covered everything, then write a complete spec to SPEC.md."*
Then `/clear` and implement from SPEC.md with clean context. Precise specs beat watching
the implementation. Also the single best fix for stalled tasks: the interview does the
thinking you've been postponing.
**Source:** best-practices, "Let Claude interview you"; echoed by the 2026 spec-driven-development consensus.

## 6. Adversarial review in a fresh context before you call it done
**Evidence:** the two latent test defects above survived in a repo he actively works in —
that is precisely what a reviewer that never saw the code being written catches.
**Action (~5 min):** run `/code-review` on the diff, or
*"Use a subagent to review this diff against SPEC.md. Report gaps that affect correctness or
the stated requirements, not style."* A fresh context is not biased toward code it just wrote.
Tell it to flag only correctness gaps, or it will invent findings and you will over-engineer.
**Source:** best-practices, "Add an adversarial review step".

## 7. Subagents for investigation, never for the edit
**Why:** context is the fundamental constraint — performance degrades as it fills, and
codebase exploration is what fills it. *"Use subagents to investigate how X works and what
I should reuse"* keeps the reading out of the main window and returns a summary.
**Action (~1 min):** use it on the next "how does this work?" question instead of letting
the main session read 30 files.
**Source:** best-practices, "Use subagents for investigation".

## 8. `/clear` discipline, and the two-correction rule
**Why:** the cheapest reliability win available. Long sessions with stale context make
Claude forget earlier instructions. If you have corrected it twice on the same thing, the
context is polluted with failed approaches — `/clear` and re-prompt with what you learned
beats a third correction almost every time. `Esc` to interrupt, `/rewind` to roll back.
**Action (~0 min, it's a habit):** one week of clearing between unrelated tasks.
**Source:** best-practices, "Manage context aggressively" / "Avoid common failure patterns".

## 9. A skill for the release ritual
**Evidence:** `auto_build.py`, `build.bat`, `start_auto_build.bat`, `TraceTrimmer.spec`,
`dist/`, `build/` — there is clearly a repeated build-and-ship sequence, done by hand.
**Action (~12 min):** `.claude/skills/release/SKILL.md` with `disable-model-invocation: true`
holding the exact steps (run suite → bump version → build → smoke-test the exe → tag → push).
Then it is `/release`. Skills load on demand, so this does not bloat every session.
**Source:** best-practices, "Create skills".

## 10. Ten lines of CI so the check runs even when you forget
**Evidence:** no `.github/workflows` in CanTraceSplitter. Local runs are the only gate, and
tip 1 shows local runs can lie.
**Action (~10 min):** ask Claude for a workflow that runs `python test_app.py` on push and PR.
`claude -p` also works in CI/pre-commit if you want Claude in the loop rather than just tests.
**Source:** best-practices, "Run non-interactive mode".

## 11. Writer / Reviewer across two sessions
**Action (~0 min setup):** session A implements, session B (fresh, or a cloud session) reviews
`@the/changed/file` for edge cases and consistency; paste B's findings into A. Works for tests
too: one session writes the tests, another makes them pass. Useful once a change is big enough
that `/code-review` isn't enough.
**Source:** best-practices, "Run multiple Claude sessions".

## 12. Measure before you believe a speed-up (the METR result)
**Why it matters for a 15-min budget:** in METR's 2025 randomised trial, experienced devs
predicted a 24% speed-up, *reported* 20% after the fact, and were measured **19% slower**.
The Feb-2026 follow-up (57 devs, 800+ tasks, late-2025 tools) found a central estimate of
about +18% for returning users and +4% for new ones, with confidence intervals that include
zero. Self-report is not evidence.
**Action (~5 min):** next time you adopt one of these tips, note the start and end time of two
comparable tasks — one with it, one without. Keep only what survives.
**Source:** METR RCT 2025 + Feb-2026 follow-up; see also arxiv 2607.01418 on Microsoft's
Claude Code / Copilot CLI rollout.

## 13. Right surface for the job
**Action (~3 min to internalise):** chat for thinking and advice (the retirement question in
`🟥Claude questions` belongs there, in a private window); CLI for repo work; a cloud routine
for anything unattended; mobile for capture. Mismatches are a quiet tax — doing repo work in
chat means copy-pasting, doing advisory work in the CLI means no memory of the conversation.

## 14. Fan out for mechanical, repetitive edits
**Action (~10 min when the moment comes):** `/batch <instruction>` splits a change across
5-30 subagents, each in its own worktree; or script it — `for f in $(cat files.txt); do
claude -p "..." --allowedTools "Edit" --permission-mode dontAsk; done`. Test on 2-3 files,
refine the prompt, then run the lot. Only worth it above ~10 near-identical edits.
**Source:** best-practices, "Fan out across files".

## 15. Worktrees when you want two things open at once
**Action (~8 min):** `git worktree` + a session per checkout so parallel work can't collide.
The honest prerequisite: you need two tasks that genuinely don't touch the same files.
**Source:** best-practices, "Run multiple Claude sessions" / /docs/en/worktrees.

## 16. The earning pipeline deserves a skill as much as the code does
**Evidence:** "apply for 1 upwork post", "buy upwork connects", "update CV",
"amend LinkedIn profile" — all open since 2025-10-14/15, all priority-3. Nothing has shipped.
**Action (~12 min):** a `/proposal` skill holding your CV, your CAN/embedded/Python niche and
your rate, which takes a pasted job post and drafts a tailored proposal plus the 3 questions to
ask the client. Turns a 40-minute psychological hurdle into a 5-minute review. This is the tip
with the most direct line to money, so it ranks higher the moment the profile confirms Upwork
is the chosen channel.

## 17. Batch the parked questions instead of asking ad hoc
**Evidence:** `🟥Claude questions` has exactly one task (retirement funds, parked 2026-09-28).
A parking lot that is never emptied is just guilt.
**Action (~0 min today):** one 15-min slot a week to burn through the parked questions —
and a habit of parking them there rather than context-switching mid-task.

## 18. Know what multi-agent actually costs before defaulting to it
**Why:** community measurements put a single agent at roughly 4x the tokens of a chat turn
and multi-agent setups at roughly 15x. Parallelism buys wall-clock, not correctness. Use it
when the work is genuinely independent; a single well-verified agent beats three unverified ones.
**Source:** community telemetry (unverified figures — treat as order-of-magnitude);
official framing in /docs/en/workflows.

## 19. CLI tools and `@file` beat MCP round-trips for context
**Action (~5 min):** install `gh` locally and tell Claude to use it; reference files with `@`
instead of describing where code lives; pipe data in (`cat error.log | claude -p "explain this"`).
CLI tools are the most context-efficient way to reach an external service.
**Source:** best-practices, "Use CLI tools" / "Provide rich content".

## 20. `/goal` for the unattended run
**Action (~5 min):** set the check as a `/goal` condition and a separate evaluator re-checks it
every turn, so a long run keeps working until the goal resolves rather than stopping at
"looks done". The natural next step after tips 1 and 2.
**Source:** best-practices, "Give Claude a way to verify its work".

---

## Research refresh log
- **2026-10-22:** official Claude Code best-practices page (read in full); METR 2025 RCT +
  Feb-2026 follow-up; arxiv 2607.01418 (Microsoft CLI-agent rollout), 2605.23135 (longitudinal),
  2602.03593 (developer perspectives); 2026 spec-driven-development write-ups (GitHub Spec Kit,
  Addy Osmani on specs); community multi-agent orchestration posts (treated as unverified).
  Next refresh: ~2026-11-05, or when the backlog drops below 7 entries.
