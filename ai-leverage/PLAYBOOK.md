# Playbook — ranked pool of practices to trickle out

Ranked by (impact for John x cheapness to adopt). One is served per day; served items get logged in TIPS-LOG.md.
Re-rank whenever QUESTIONS.md gets new answers.

Primary sources (prefer these over blog listicles):
- Claude Code best practices — https://code.claude.com/docs/en/best-practices
- How Claude Code is used in practice (Anthropic, ~400k sessions) — https://www.anthropic.com/research/claude-code-expertise
- Running an AI-native engineering org (Anthropic) — https://claude.com/resources/articles/running-an-ai-native-engineering-org
- Large codebases guide — https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start

## Queue

| # | Practice | Why it fits John | Cost | Status |
|---|---|---|---|---|
| 1 | **Move "must always" rules from prose into a `Stop` hook.** `.claude/settings.json` -> `"Stop": [{"hooks":[{"type":"command","command":"<check> 1>&2 \|\| exit 2"}]}]`. Exit 2 sends Claude back to work. | His own Trace Trimmer task asks for exactly this in prose ("make a rule that will definitely..."). Prose = model's call; hook = enforced. | 10 min | **served 2026-11-16** |
| 2 | **Reviewer subagent that cannot edit.** `.claude/agents/reviewer.md` with `tools: Read, Grep, Glob` — reviews the diff against a spec, "report only gaps that affect correctness, skip style". | He has no independent check; the writer grades its own work. The tool limit is enforced by the harness, not requested. | 10 min | queued |
| 3 | **Interview-me-into-a-spec, then build in a fresh session.** *"I want X but haven't thought it through. Interview me until you could write the spec, then write it to SPEC.md."* Then `/clear` and build from SPEC.md. | The unblocking move for Trace Trimmer and the Upwork profile — both stalled with no written "done". | 15 min | queued |
| 4 | **Drain the `@claude` tag with a scheduled cloud routine.** A routine that reads TickTick tasks tagged `@claude`, does the ones that are self-contained research, and reports back. | He already has the intake habit; the loop never closes. Turns a dead tag into throughput. | 15 min (he schedules) | queued |
| 5 | **Give every repo one pass/fail command in CLAUDE.md.** The single most useful line is the command that runs the check (test/build/lint/screenshot-diff). Then ask for *evidence*: the command and its output. | Reliability, unattended runs, and it is the prerequisite for #1 and for anything backgrounded. | 5 min | queued |
| 6 | **`/clear` between unrelated tasks, and name sessions.** `/clear oauth-migration`, `/rename`, `claude --resume <name>`. Every request re-sends the whole conversation. | Train-commute working style = many short, unrelated bursts in one session. Cheap and immediate. | 2 min | queued |
| 7 | **Effort as the real dial.** `/effort high|xhigh` for bugs in code you didn't write, flaky tests, schema changes; `/effort low` for sketching; `ultrathink` for one hard turn. "think harder" in the prompt is *not* a keyword. | Likely still using folk prompt-magic. Directly affects reliability on the hard cases. | 2 min | queued |
| 8 | **Parallel worktrees.** `claude -w feature-x` per piece of work; `.worktreeinclude` to carry `.env` in. | Two stalled projects + a day job; parallelism is how one evening covers two fronts. | 10 min | queued |
| 9 | **`/batch` for one mechanical change across many files** — splits into 5-30 worktree units, each opening a PR, after you approve the plan. | Trace Trimmer-style refactors; a single approval buys a lot of work. | 10 min | queued |
| 10 | **Deny rules + sandbox for the things that must never happen.** `"deny": ["Read(./.env)", ...]` holds in *every* permission mode, auto included. `/sandbox` for OS-level limits. | Precondition for trusting unattended/scheduled runs with work credentials. | 10 min | queued |
| 11 | **Team procedures -> skills, not CLAUDE.md.** `.claude/skills/<name>/SKILL.md`; add `disable-model-invocation: true` for anything with side effects (releases, deploys). Lighter on context than CLAUDE.md. | The work "New Workflow"/devdock rollout is a procedure-shaped thing he could own and look good doing. | 15 min | queued |
| 12 | **Shrink CLAUDE.md.** `/init`, then `/doctor` and `/doctor prompt-audit` to cut what Claude can read from the repo anyway. Target <200 lines. Personal prefs -> `CLAUDE.local.md` (gitignored). | Every line costs attention on every task. Likely bloated with architecture description. | 10 min | queued |
| 13 | **Path-scoped rules.** `.claude/rules/<area>.md` with a `paths:` filter so a rule loads only where it applies. | Cheap once CLAUDE.md is trimmed; good fit for a repo with legacy + new areas. | 10 min | queued |
| 14 | **Ask Claude first for "why is it like this" questions** instead of a colleague or a doc hunt; then ask whether the recurring question should become a routine. | Anthropic's own org practice. Fits his routine habit and the new-workflow onboarding. | 0 min (habit) | queued |
| 15 | **Pre-flight for unattended runs** (the five questions): does it know what done looks like; can it check itself; what may it touch; what stops it (`--max-turns`, `--max-budget-usd`); where does the result go and who signs off. | He already runs scheduled routines — this is the ahead-of-the-curve hardening most people skip. | 10 min | queued |
| 16 | **Steering reflexes:** `Esc` the moment it drifts; `/rewind` to roll back code+conversation; after two failed corrections `/clear` and write a better prompt rather than a third correction. | Anthropic's session study: experts differ mainly by *steering precision* and by not abandoning stuck sessions. Free, pure skill. | 0 min (habit) | queued |
| 17 | **Headless loops from a script** for repetitive migrations: `claude --bare -p "..." --allowedTools ... --permission-mode dontAsk --max-turns 20`, tested on 3 files first. | Turns an evening of grind into a loop; also a sellable skill on Upwork. | 15 min | queued |

## Deliberately NOT recommending

- **"Use subagents to protect your context window"** — obsolete. 1M-token windows + automatic compaction; subagents are for parallelism, noise isolation and *fresh* review, each costing extra tokens.
- **`IMPORTANT`/ALL CAPS emphasis** — current models follow plain wording; piling on emphasis makes rules over-apply. If a line keeps getting missed, the file is too long or the rule belongs in a hook.
- **"think hard / don't be lazy / keep going"** — effort level is the control; those lines tend to cause over-work.
- **Describing architecture and file layout in CLAUDE.md** — Claude reads the repo faster than you can describe it.
- **Delegating to a subagent to get a *better* answer** — same model, same task, no gain. A fresh *reviewer* is a different thing and does help.
- **Chasing the productivity-study numbers.** Self-reported gains (~3x median) dwarf measured ones; METR's 2025 trial found experienced devs 19% *slower* while believing they were 20% faster, and its 2026 update swung positive with intervals including zero. Takeaway for John: don't trust the felt speedup — the per-project pass/fail check (#5) is the only honest signal.
