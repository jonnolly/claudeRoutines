# Tip library — ranked by (impact on John's output) ÷ (minutes to adopt)

Each tip: **what**, **why it fits John**, **the ≤15 min action**, **source**.
Re-rank whenever `ANSWERS.md` changes. Delivered tips are marked in `TIP-LOG.md`.
Tips marked `[blocked: Qn]` wait for that question to be answered.

---

## 1. Give Claude a check it can run — stop being the verification loop
**What:** Claude stops when work *looks* done. If you hand it a pass/fail check (test,
build exit code, a script that measures startup time), it iterates until the check passes
instead of handing you something plausible to inspect. Three escalating levels:
in-prompt ("run it and iterate"), `/goal <condition>` (a separate evaluator re-checks
after every turn and Claude keeps going until it resolves), and a **Stop hook** (a script
that blocks the turn from ending until it passes).
**Why John:** he already wrote this by hand into the Trace Trimmer startup-time task —
*"Make a rule… the start-time must always be under 1 second. Test this each time you make
a change… keep trying until you do fulfill this requirement."* That instruction is
advisory and gets lost; a hook is deterministic.
**15 min action:** in the Trace Trimmer folder, ask Claude: *"Write me a script that
launches the app, measures time-to-first-window, and exits non-zero if it's over 1.0 s.
Then add it as a Stop hook in .claude/settings.json."* Next startup-time session: start
with `/goal startup time under 1.0s measured by scripts/startup_time.py`.
**Source:** Claude Code best practices — "Give Claude a way to verify its work"; hooks docs.

## 2. Move repeated prompt text out of task descriptions into CLAUDE.md / a skill
**What:** `CLAUDE.md` loads every session (keep it short — bloat makes Claude ignore it);
skills load **on demand** and are the right home for domain knowledge like trace formats.
`/doctor` proposes cuts for anything Claude could derive from the code itself.
**Why John:** his TickTick tasks carry re-explained project rules each time (trace
formats, the `;` header lines, the `can_log_<ip>_<start>_<end>` filename convention, the
startup budget). That is per-task typing he pays for forever.
**15 min action:** *"Read my last few task descriptions and the trace parsing code. Write
a short CLAUDE.md with only the rules you can't infer from the code, and put the CAN/Insight
trace format knowledge in .claude/skills/can-traces/SKILL.md."* Then `/context` to confirm it loaded.
**Source:** best practices — "Write an effective CLAUDE.md", "Create skills".

## 3. Let Claude interview you, then implement from SPEC.md in a *fresh* session
**What:** For anything multi-file: *"I want to build X. Interview me in detail using the
AskUserQuestion tool. Ask about implementation, UX, edge cases and tradeoffs — dig into the
hard parts. Then write a complete spec to SPEC.md."* Start a **new** session to implement
it, so the implementation context is clean. Good specs name the files, state what's out of
scope, and end with an end-to-end verification step.
**Why John:** the GUI start/end-time selection task and the auto-update pop-up task are
exactly the shape that silently sprawls — and he's writing the spec himself, in a TickTick
box, before knowing the edge cases.
**15 min action:** run the interview prompt for the "only selectable start/end times"
GUI change. Stop at the spec. Implement tomorrow.
**Source:** best practices — "Let Claude interview you"; spec-driven development.

## 4. Set effort and model **per subagent**, inline in the prompt
**What:** Since v2.1.292 you can say which subagents think hard and which just grep:
*"Find every X with low effort subagents, then have a high effort one check the results."*
Haiku 5.5 (1M context, $0.10/M in) is the cheap one for lookups and summaries.
**Why John:** on a Team seat with usage limits, this is a direct speed-and-cost win for the
search-heavy work he does over trace code and logs — and it's two weeks old, so it's
genuinely ahead of the curve.
**15 min action:** next codebase question, phrase it as above. Also add the pacing sentence
Anthropic's own team uses: *"Time matters here: do not spend time that can be avoided, and
the earlier a correct result is obtained, the better."*
**Source:** This week in Claude Code, 17 Oct 2026; subagents docs.

## 5. Writer / reviewer split — never let the session that wrote the code grade it
**What:** A reviewer in a **fresh context** sees only the diff and your criteria, not the
reasoning that produced it. Either run the bundled `/code-review` skill, or:
*"Use a subagent to review this diff against SPEC.md. Report gaps that affect correctness
or the stated requirements — not style."* Tell it to flag only real gaps, or it will invent
findings and you'll over-engineer.
**Why John:** solo developer, no second pair of eyes, shipping a tool colleagues depend on.
This is the cheapest quality gate he can buy. Code Review is also now GA on Team plans with
Quick/Standard/Deep depth.
**15 min action:** run `/code-review` on the current Trace Trimmer diff before the next
build you hand to a colleague.
**Source:** best practices — "Add an adversarial review step"; Code Review GA announcement.

## 6. Hand the boring backlog to cloud sessions and close the laptop  `[blocked: Q10, Q12]`
**What:** Cloud sessions run on Anthropic infrastructure; continuing a local session in the
cloud now carries your **uncommitted changes and unpushed commits**, so there's no
commit-first dance. Kick off, walk away, review the pushed branch later.
**Why John:** his evenings go to the conservatory and his `@claude` TickTick backlog is
full of self-contained chores (LinkedIn/CV updates, platform comparisons, small GUI tasks).
Those are exactly the "bounded, repeatable, reviewable" tasks agents are reliable on.
**15 min action:** pick one `@claude` task, start it as a cloud session, let it push a
branch, review in the morning.
**Source:** cloud sessions update, 17 Oct 2026; founder-workflow guidance ("agent drafts,
human sends").

## 7. Parallel sessions instead of one long session
**What:** Nested sessions in the desktop app (ask Claude to run tasks in parallel; each
gets its own session and reports back), `/batch <instruction>` to fan a change across 5–30
subagents each in its own worktree, or git worktrees for manual parallelism. The sidebar
shows which sessions are working and which need you.
**Why John:** he explicitly flagged "using multiple agents, assigning roles, having them
continuously working" as something he suspects he's missing. This is the concrete version —
but it only pays off when file boundaries are clean, so it ranks below the quality tips.
**15 min action:** update the desktop app, then run two sessions on Trace Trimmer: one on
the Insight-format parsing, one on the update pop-up (different files, no collision).
**Source:** best practices — "Run multiple Claude sessions"; desktop app update, 17 Oct 2026.

## 8. A TickTick → agent intake loop  `[blocked: Q10, Q15]`
**What:** A routine that reads `@claude`-tagged tasks each morning, picks the ones with
enough detail, does them, and reports back — turning his tag into an actual work queue.
**Why John:** he already tags tasks `@claude` by hand and then has to re-open each one and
re-prompt it. The tag is a queue that nothing currently consumes.
**15 min action:** none yet — this needs a routine, and **John schedules his own routines.**
Proposed task text will be supplied when Q10/Q15 are answered, so it lands at a time that
doesn't collide with value-adding work.
**Source:** own observation; Managed Agents / scheduled-automation pattern.

## 9. Spend the Team API credits on one Managed Agent  `[blocked: Q7, Q13]`
**What:** Team plans include pooled monthly API credits (up to $500). Managed Agents (beta)
run on Anthropic infrastructure — nothing stays running on your machine. There's a
one-shot onboarding: `/claude-api managed-agents-onboard https://claude.dev/blog/building-effective-agent-automations/`
and Claude sets up the agent, its sources, schedule and memory.
**Why John:** this is the bridge between "improve my workflow" and "earn money" — a working
Managed Agent is both an internal time-saver and a demonstrable, sellable deliverable for
Upwork/Codementor clients. Credits that aren't spent are gone.
**15 min action:** run the onboarding command once and see what it proposes.
**Source:** This week in Claude Code, 17 Oct 2026; Managed Agents docs; API credits for subscribers.

## 10. Plan mode, but only where it pays
**What:** `Shift+Tab` to plan mode (or `claude --permission-mode plan`); `Ctrl+G` opens the
plan in your editor to edit before Claude proceeds. Plans persist to `~/.claude/plans/`, so
they survive compaction. **Skip it** when you could describe the diff in one sentence.
**Why John:** half his tasks are one-sentence diffs (parse a filename, update a timestamp)
where planning is pure overhead; the other half (GUI state constraints, auto-updater) are
multi-file and unfamiliar, where skipping it costs a rewrite.
**15 min action:** adopt the one-sentence test as the rule for which mode to open in.
**Source:** best practices — "Explore first, then plan, then code".

## 11. Context hygiene: `/clear`, two-correction rule, `/btw`
**What:** `/clear` between unrelated tasks. **If you've corrected Claude twice on the same
thing, stop** — the context is now polluted with failed approaches; `/clear` and rewrite the
prompt with what you learned. `/btw` answers a side question without putting it in history.
`Esc`/`/rewind` restores earlier conversation or code state.
**Why John:** one long session per topic is the default habit, and performance degrades as
context fills. The two-correction rule is the single highest-yield habit change on this list.
**15 min action:** nothing to install — just the rule: *second correction = `/clear` and restate.*
**Source:** best practices — "Manage your session", "Avoid common failure patterns".

## 12. Fan out over files with `claude -p` for repetitive trace work  `[blocked: Q12]`
**What:** `claude -p "…" --allowedTools "…" --permission-mode dontAsk` in a shell loop, or
`--output-format json | your_command` to pipe results into a pipeline. Refine the prompt on
2–3 items, then run the whole set.
**Why John:** batch-analysing a directory of CAN logs ("which of these 200 traces contain
fault X, output CSV") is a loop, not a conversation. This is where an hour becomes a minute.
**15 min action:** one-liner over a folder of traces producing a summary CSV.
**Source:** best practices — "Fan out across files", "Run non-interactive mode".

## 13. Make permission prompts stop costing attention
**What:** auto mode is the default starting mode on Team (a classifier reviews actions
instead of you, blocking scope escalation and hostile-content-driven actions);
plus `/permissions` allowlists for the commands you always approve, and `/sandbox` for
OS-level isolation. The bundled `/fewer-permission-prompts` skill scans your transcripts and
proposes an allowlist.
**Why John:** after the tenth approval nobody is reviewing, they're clicking — that's the
worst of both worlds, cost without safety.
**15 min action:** run `/fewer-permission-prompts` once and accept what it finds.
**Source:** best practices — "Configure permissions"; bundled skill.

## 14. Hooks that actually block, not just advise
**What:** Since v2.1.295, `"onFailure": "block"` makes a hook that times out, can't start,
or exits unexpectedly **block the action** rather than silently letting it through. Hooks are
the only way to guarantee something happens every time; `CLAUDE.md` is advisory.
**Why John:** he writes rules as prose ("you must keep trying"); the enforcement version is
a hook. Natural follow-on once tip #1 is in place.
**15 min action:** add `onFailure: block` to the startup-time Stop hook from tip #1.
**Source:** Claude Code changelog 2.1.295.

## 15. Let the agent build the income assets, not just the code  `[blocked: Q7]`
**What:** The reliable pattern for outward-facing work is **agent drafts, human sends**:
agents are good at bounded, repeatable, internal-facing work and bad at unsupervised
customer messaging. So: Claude drafts the Upwork profile, the proposal templates, the
LinkedIn rewrite and the CV from evidence in your actual repos; you edit and send.
**Why John:** 💻Remote Work has sat with "create upwork profile", "buy connects",
"apply for 1 upwork post" and "amend LinkedIn profile" open since mid-October. The blocker
is drafting effort, which is the cheapest thing to delegate.
**15 min action:** *"Read my Trace Trimmer repo and CV. Draft an Upwork profile and two
proposal templates positioning me as a CAN/embedded-data tooling engineer. Flag anything you
had to invent."*
**Source:** founder/freelance agent guidance; own TickTick backlog.

## 16. Productise one thing you already built  `[blocked: Q7, Q12]`
**What:** The highest-margin AI output is usually a tool you built once for yourself, cleaned
up and sold or taught. Trace Trimmer is a real tool solving a real industrial problem.
**Why John:** aligns the workflow work with the money goal instead of competing with it.
**15 min action:** *"Interview me about Trace Trimmer as a product: who else has this problem,
what would they pay, what's the smallest sellable version. Write it to IDEA.md."* Decide after.
**Source:** own observation; "workflows win" / bounded-scope agent guidance.

## 17. Name and resume sessions like branches
**What:** `/rename` a session, `claude --continue` / `--resume` to pick it back up. Each
workstream keeps its own persistent context, so you stop re-explaining. Long idle sessions
now auto-compact before the 1-hour cache expires (saves usage); `"idleCompaction": false`
turns it off.
**Why John:** work is interrupted by lessons, gigs and travel ("🚆Todo on the go") — resumable
named sessions are the fix for re-explaining after every interruption.
**15 min action:** `/rename` the current session to e.g. `trace-trimmer-insight-parsing`.
**Source:** best practices — "Resume conversations"; changelog 2.1.299.

## 18. Ask the codebase questions you'd ask a senior engineer
**What:** "How does logging work?", "What edge cases does X handle?", "Why does this call
foo() instead of bar() on line 333?" — no special prompting needed. Best onboarding tool
there is.
**Why John:** he inherits formats and conventions from other people's tooling (the Insight
CAN converter). Reading those by hand is the slow path.
**15 min action:** one such question against the trace-parsing module.
**Source:** best practices — "Ask codebase questions".

## 19. Watch the meters: `/context`, `/usage`, a context status line
**What:** `/context` shows what actually loaded; `/usage` now warns about max effort,
workflows, always-on context and large tool results; a custom status line tracks context
continuously.
**Why John:** on a Team seat, limits are shared; knowing which habit is expensive is how you
stop guessing. Low effort, modest payoff — hence the low rank.
**15 min action:** run `/usage` once and read the warnings.
**Source:** best practices — context window; changelog 2.1.299.

## 20. Free security scans if anything goes open source  `[blocked: Q16]`
**What:** Anthropic's OSS Scanner runs regular scans with their strongest models at no cost
for established open-source projects; you apply with a PR.
**Why John:** only relevant if Trace Trimmer (or a spin-off) is ever published. Parked.
**Source:** This week in Claude Code, 17 Oct 2026.
