# Tip backlog — ranked, highest value first

Each tip: what it is, why it fits John, the ≤10-minute first step, and where it comes from.
`Blocked-by` means: don't deliver until that fact is known/true.
Re-rank every run as the profile fills in. One tip per day, max.

---

## T01 — Reconnect the Atlassian connector (dead tool = silent capability loss)
**Status:** delivered 2026-11-19
**Why John:** His whole W150Fi review lives in Jira + Confluence. The connector is returning
a hard error (v1 SSE transport retired), so every Claude session is blind to the one system
that holds his actual work. Also the general lesson: a connected tool that silently stops
working costs you more than a missing feature, because you stop asking.
**First step (5 min):** claude.ai → Settings → Connectors → remove and re-add Atlassian
(new endpoint `https://mcp.atlassian.com/v2/mcp`), complete OAuth. Then ask Claude
"list my open Jira issues" to confirm.
**Source:** observed tool error, 2026-11-19 + Atlassian v1→v2 migration notice.

---

## T02 — Give Claude a check it can run (the single highest-leverage setup step)
**Why John:** Claude stops when work *looks* done. On safety-critical firmware "looks done"
is worthless, and it makes him the test suite. One line in CLAUDE.md with the exact build /
unit-test / static-analysis command turns every session into a self-correcting loop, and is
the precondition for every unattended run later.
**First step (10 min):** add to the work repo's CLAUDE.md: build command, single-test command,
static-analysis command (cppcheck/clang-tidy or vendor equivalent). Then ask for a small
change and require the command output as evidence.
**Blocked-by:** Q02 (is a work repo reachable by Claude), Q04.
**Source:** code.claude.com/docs/en/best-practices — "Give Claude a check to run".

---

## T03 — A read-only reviewer that checks code against the requirement, not against taste
**Why John:** The documented failure mode of AI on firmware is *traceability*: generated or
reviewed code with no link back to the requirement it satisfies. That is also the most
tedious half of a W150Fi review. A reviewer subagent with `tools: Read, Grep, Glob` cannot
edit anything (enforced by the harness, not by a prompt) and hasn't seen the reasoning that
produced the code, so it argues with the diff instead of agreeing with it.
**First step (10 min):** create `.claude/agents/reviewer.md` with
`tools: Read, Grep, Glob` and a body like: "compare the changed files against the requirement
text you are given; report only gaps that affect correctness or that no test covers; skip style".
Run it on one review ticket (e.g. the 300 A per-pack / 700 A total limit) and judge the output.
**Note:** keep "skip style" in the prompt — a reviewer asked to find problems always finds some.
**Blocked-by:** Q02.
**Source:** best-practices "Know what subagents cost" / "Review against your spec";
firmware-review literature on the traceability gap.

---

## T04 — Deterministic vs non-deterministic: the distinction worth internalising
**Why John:** This is the mental model that makes everything else cheap. Prompts, CLAUDE.md
and skills are *suggestions* the model may override; hooks, deny rules and managed settings
are *enforced by the harness*. In safety-critical work the rules that genuinely cannot bend
("never finish with a failing build", "never touch the generated CAN DBC output") belong in
the second category. Corollary: if he keeps adding emphasis to a CLAUDE.md line, that line
wants to be a hook — and if he has hooks for mere preferences, they should be deleted.
**First step (10 min):** list his top 3 "must never / must always" rules, then convert exactly
one into a `PreToolUse` or `Stop` hook in `.claude/settings.json`. Asking Claude to
"write a hook that blocks edits to <path>" works as a prompt.
**Source:** best-practices — "Deterministic and non-deterministic instructions".

---

## T05 — Stop correcting; clear and re-prompt
**Why John:** Cheapest speed win available, zero setup. After two failed corrections a third
one just adds more failed attempts for Claude to re-read every turn. `/clear` plus one new
prompt that folds in what was learned beats it almost every time. Same for unrelated tasks:
`/clear` between them so task four isn't paying to re-read tasks one to three.
Also: `Esc` stops mid-action and keeps the work; `Esc Esc` / `/rewind` rolls code *and*
conversation back, which makes trying the bolder approach first low-risk.
**First step (2 min):** nothing to install — just adopt the "two strikes then /clear" rule
and try `/rewind` once on purpose so the menu isn't unfamiliar under pressure.
**Source:** best-practices — "Steer the session", "Keep cost and context down".

---

## T06 — Effort is the dial, not prompt wording
**Why John:** "think hard" / "be thorough" are ordinary prompt text now; they nudge within
the current effort setting but cannot lift it. `/effort high` or `xhigh` is for exactly his
kind of problem — a bug in code someone else wrote, a timing-dependent fault, a change where
every reader of an old shape must be found. `/effort low` for sketching and renames. `max`
only for a hard problem to be worked through unattended. `ultrathink` in a single prompt when
only that one turn needs depth. Separately, `be ambitious` *does* still work: it tells Claude
about scope (edge cases, error states, the natural follow-on) which only he knows.
**First step (3 min):** run the next genuinely tricky diagnosis at `/effort high` and compare.
**Source:** best-practices — "Change the model and effort", "Write a specific prompt".

---

## T07 — Parallelism that actually works: one checkout per agent
**Why John:** He named "multiple agents" as a goal. The thing that makes multi-agent work
*fail* is two agents writing the same file. `claude -w <name>` starts a session in its own
git worktree; the desktop app runs several side by side; cloud sessions run them off his
machine entirely. Read-only research agents can share; writers need isolation. Add a
`.worktreeinclude` listing the gitignored files a build needs (`.env`, dev credentials) and
each new worktree gets them copied in — otherwise worktree sessions fail on missing config.
**First step (10 min):** `claude -w spike-<something>` for one independent piece of work;
add `.worktreeinclude` if the build needs gitignored files.
**Source:** best-practices — "Run sessions in parallel".

---

## T08 — One mechanical change across many files: `/batch`
**Why John:** Firmware repos accumulate exactly this shape of work — rename a CAN signal
everywhere, migrate every handler to a new API, add a guard to every ISR entry. `/batch`
splits it into 5–30 units, shows the plan for approval, then gives each unit its own worktree
and reports back or opens a PR. This is the right tool where he might otherwise hand-roll
parallel agents.
**First step (10 min):** find one pending repo-wide mechanical change and run `/batch` on it;
approve the plan, review the diffs.
**Source:** best-practices — "Run sessions in parallel" (`/batch`).

---

## T09 — Spec-first: make Claude interview him
**Why John:** Review tickets and test plans (OT1–OT11) are specs in disguise. Rather than
pre-writing a brief, "I want X but haven't thought it through — interview me until you could
write the spec, then write it to SPEC.md" turns a vague intent into a written definition of
done in a few multiple-choice rounds. Then build from it in a **fresh** session, and point
the reviewer (T03) at the same file. The spec is what makes the review objective later.
**First step (10 min):** do the interview once for a single review ticket or test plan.
**Source:** best-practices — "Brainstorm with Claude first".

---

## T10 — Turn the devdock / new-workflow docs into skills, not CLAUDE.md
**Why John:** New Electric is rolling out a new workflow and dev-env docs right now, which is
the cheapest possible moment to encode them. Team procedure (release steps, bench-test
protocol, how a review ticket gets closed) goes in `.claude/skills/<name>/SKILL.md`: Claude
sees only the name and description every session and reads the body only when relevant, so a
long procedure doesn't tax unrelated work the way a long CLAUDE.md does. For anything with
side effects, add `disable-model-invocation: true` so it only runs when he types `/name`.
**First step (10 min):** convert one procedure from Frank's docs into a skill.
**Blocked-by:** Q02.
**Source:** best-practices — "Put team procedures in skills".

---

## T11 — Keep CLAUDE.md short (and audit it)
**Why John:** The instinct is to document architecture and conventions. Claude reads the repo
faster than he can describe it; every line in CLAUDE.md spends attention on *every* task.
Write down only what isn't in the repo (decisions made in meetings, the deploy process in
someone's head, the env var the integration tests need) or what Claude would otherwise
re-discover each session. Under 200 lines. `/init` drafts it, `/doctor` suggests cuts, and
`/doctor prompt-audit` flags instructions written for older models or contradicting each other.
Personal preferences go in `CLAUDE.local.md` (gitignored). Rules that matter only in one
directory go in `.claude/rules/*.md` with a `paths:` filter so they load only there.
**First step (5 min):** run `/doctor prompt-audit` on the repo he uses most.
**Source:** best-practices — "Keep CLAUDE.md short", "Scope rules to one part of the codebase".

---

## T12 — Demand evidence, not claims
**Why John:** "All tests pass" tells him nothing; the command plus its output tells him
everything, and reading it is faster than re-running it. For a session he wasn't watching,
that output is the *only* evidence. `/code-review` gets a fresh subagent that never saw the
conversation; `/verify` has Claude actually build and run the thing and look at the result,
which catches what tests and typechecks miss.
**First step (2 min):** make "show me the command and its output" the default ending of his
prompts for a week.
**Source:** best-practices — "Give Claude a check to run".

---

## T13 — The five questions before any unattended run
**Why John:** He wants agents "working continuously". That is safe exactly when five things
are true: (1) it knows what done looks like — a goal condition, a spec, a failing test to turn
green; (2) it can check its own work; (3) its reach is limited — permission rules, sandbox,
a worktree, one pushable branch; (4) something stops it — `--max-turns`, `--max-budget-usd`,
a spend limit; (5) a person signs off on anything irreversible. `/goal "<condition>"` is the
piece most people miss: a separate model checks the condition after every turn and sends
Claude back if it ended a turn with a progress summary while items were still open.
**First step (10 min):** take one routine he already wants and write down the five answers
before scheduling it.
**Source:** best-practices — "Let Claude run without you".

---

## T14 — `/usage`: find out what the tokens are buying
**Why John:** He has four connectors loaded (Atlassian, Gmail, TickTick, GitHub). Connected
MCP servers add their tool names and instructions to context in *every* session, used or not.
`/usage` breaks usage down by skill, subagent, plugin and MCP server, and flags patterns like
long context or frequent cache misses once one passes 10%. Turning off the servers a given
project doesn't need is free speed. Prefer a CLI over an MCP server where one exists (`gh`
over a GitHub server) — fewer tokens, same reach.
**First step (3 min):** run `/usage`, then disable unused servers in `/mcp`.
**Source:** best-practices — "Keep cost and context down", "Connect the tools Claude needs".

---

## T15 — Hand over the artefact instead of describing it
**Why John:** Debugging hardware means logs, scope traces, CAN dumps, requirement PDFs,
screenshots of a failing HMI. `@path` inlines a file, a pasted image goes straight into the
prompt, and `cat error.log | claude -p "what's going on here"` pipes shell output in. Every
minute spent paraphrasing an artefact he already has is wasted, and the paraphrase loses the
detail that mattered.
**First step (2 min):** next failure, paste the raw log/screenshot instead of summarising it.
**Source:** best-practices — "Write a specific prompt".

---

## T16 — Stop doing the 2025 things (directly relevant to his stated plan)
**Why John:** Three of his own instincts are retired advice. (a) *Subagents to protect the
context window* — windows are ~1M tokens with automatic compaction; subagents are for
parallelism, noisy output and fresh-eyes review, each costing extra tokens. (b) *Delegate to a
subagent for a better answer* — same model, same task, no smarter; only a reviewer that hasn't
seen the reasoning genuinely helps. (c) *"keep going, don't be lazy, loop until done"* — more
likely to cause over-work than to fix a stall; use `/goal` or a Stop hook for runs nobody
watches. Also drop IMPORTANT/ALL-CAPS (makes rules over-apply) and architecture dumps in
CLAUDE.md. Keeping the habit that still pays: `/clear` between tasks, and `ultrathink`.
**First step (5 min):** read the "What you can stop doing" table once and drop the two habits
he recognises.
**Source:** best-practices — "What you can stop doing".

---

## T17 — Headless Claude in a shell loop, tested on three files first
**Why John:** For a repetitive migration across many files, `claude --bare -p "<prompt>"` with
`--allowedTools`, `--permission-mode dontAsk` and `--max-turns 20` in a `for` loop is simpler
and cheaper than orchestrating agents. `--bare` skips hooks, skills, plugins, MCP and every
CLAUDE.md so the run behaves identically wherever it runs. Have it reply `OK` or `FAIL`.
Run three files, see what breaks, fix the prompt, then run the rest.
**First step (10 min):** pick a 10+ file repetitive edit and script it for three files.
**Source:** best-practices — "Run Claude from a script".

---

## T18 — Spec-driven development is the pattern the field converged on
**Why John:** Independent of Anthropic's docs, the 2026 consensus across practitioner and
preprint literature is a staged flow — spec → plan → tasks → implement, with a human gate at
each phase (GitHub Spec Kit, AWS Kiro, OpenSpec). The argument in the research is one he will
recognise from safety-critical work: agentic speed does not remove engineering discipline, it
*relocates* it upstream into specification precision, explicit gates and auditable provenance.
That is V-model thinking, so his domain is unusually well set up to exploit it.
**First step (10 min):** run one review item through spec → plan → tasks → implement with an
explicit approval between each, and judge whether the gates earn their time.
**Source:** SDAD (arXiv 2608.20341), Spec Kit Agents (arXiv 2604.05278), Agentic Agile-V
(alphaxiv 2605.20456), practitioner surveys — see `sources.md`.

---

## Candidate ideas not yet worked up
- Requirement-coverage routine: nightly cross-check of firmware against the requirement list,
  reporting only *newly* uncovered requirements. (High value, needs Q02 + T02 first.)
- Jira review-ticket triage digest in the morning email slot.
- Meeting notes → Confluence page, as a skill with his house style.
- Personal: Dutch vocabulary drilling from his own TickTick list; jazz transcription support
  (ask first — he may want music kept AI-free).
- `claude agents` / agent view for watching background work from one screen (research preview).
