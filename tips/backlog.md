# Daily AI-workflow tip backlog

Ranked by **(money or reliability impact) ÷ (minutes to adopt)** for John's specific situation.
One per day, delivered in the morning email-review window. Mark `DELIVERED yyyy-mm-dd` when sent.

Sources for the underlying practice are cited per tip so claims stay checkable.

---

## DELIVERED 2026-10-29 — #1 Make "must always" rules enforced, not hoped for
**Why him:** His Trace Trimmer task literally asks for a rule that will "definitely" apply every
session and be tested on every change. Anthropic's own memory docs say CLAUDE.md is *context, not
enforced configuration* — to guarantee behaviour you need a hook. So his request is currently
unsatisfiable as written, and he probably doesn't know why Claude keeps drifting.
**Do:** `CLAUDE.md` for the intent + a `Stop` hook that runs the startup benchmark and `exit 2`s
with the measured time when it exceeds 1s. Exit 2 on `Stop` feeds stderr back and stops Claude
from finishing, so it must fix it or tell him the real number.
**Minutes:** ~10. **Payback:** every future Trace Trimmer session.

---

## NEXT UP

### #2 Plan mode before any change touching more than one file
Plan review is the cheapest intervention point there is — fixing a wrong plan costs a fraction of
fixing a wrong implementation. His tasks are already written as specs, so he's 80% there; the
missing step is making Claude restate the plan before it edits.
**Minutes:** ~2 to adopt, saves a whole wrong implementation.

### #3 Turn the `@claude` tag into something that actually runs
He already tags TickTick tasks `@claude` — nothing consumes them. A routine that reads
`@claude`-tagged tasks each morning, does the self-contained ones, and reports back converts a
dead convention into throughput. (He schedules it himself.)
**Minutes:** ~15 to specify. **Payback:** compounding.

### #4 Batch the Upwork/freelance output instead of hand-writing it — MONEY
The freelance backlog has been stale two weeks because each application is a cold-start writing
task. Headless/scripted Claude (`claude -p`) over a file of saved job posts produces N tailored
proposals in one pass, with his CV + Trace Trimmer case study as fixed context. Turns "apply for
1 post" from a 40-minute chore into a review-and-send.
**Minutes:** ~15 to set up once. **Payback:** direct revenue.

### #5 A reviewer subagent that didn't write the code
A subagent starts with a fresh context window, so it isn't anchored on the reasoning that produced
the code — which is exactly why it catches what the author missed. Give it read-only tools
(Read/Grep/Glob). Highest-value single subagent role for a solo developer.
**Minutes:** ~10.

### #6 Promote task descriptions to `.spec.md` files in the repo
His CAN-format task description is already a better spec than most tickets. Living in TickTick, it
dies after one use; living in the repo, it's reusable context and a regression record.
**Minutes:** ~5 per feature.

### #7 Custom slash commands for the workflows he repeats
Trace Trimmer feature work and freelance proposals are both repeated shapes. A `/feature` and a
`/proposal` command removes the re-prompting tax.
**Minutes:** ~10.

### #8 Auto memory on, per repository
Claude writes its own learnings from corrections, loaded every session (first 200 lines / 25KB).
Stops him re-teaching the same CAN-trace conventions.
**Minutes:** ~2.

### #9 Verification loop: hand the agent its own test/lint output
Once an agent can see a failing test or lint warning it works hard to fix it. He asks for this in
prose ("test this each time") — a `PostToolUse` hook on `Edit|Write` makes it automatic.
**Minutes:** ~10.

### #10 Git worktrees for parallel Trace Trimmer features
Two agents editing the same file race. Worktree isolation is the standard fix, and lets GUI work
and the format-parser work run at once.
**Minutes:** ~10. Only worth it once #2 and #5 are habits.

### #11 Measure before believing — the METR caveat
A METR study found experienced developers took **19% longer** with AI tools once review and
debugging were counted. Worth him timing two comparable Trace Trimmer tasks rather than assuming
a speedup. Protects against exactly the trap this routine could create.
**Minutes:** ~0 extra (just note the times).

### #12 Right-size parallelism
Community consensus: the documented subagent cap is a limit, not a target; 5–7 specialists is
where merging summaries starts costing more than parallelism saves. Relevant before he scales up.
**Minutes:** ~5 reading.

---

## Sources
- Claude Code memory docs (CLAUDE.md is context, not enforced config): https://code.claude.com/docs/en/memory
- Claude Code hooks reference (events, exit-2 semantics): https://code.claude.com/docs/en/hooks
- [Claude Code Subagents: A 2026 Practical Guide](https://www.tembo.io/blog/claude-code-subagents)
- [Claude Code Subagents Best Practices](https://crystl.dev/blog/claude-code-subagents-best-practices/)
- [Claude Code subagents: the 2026 production playbook](https://www.totalum.app/blog/claude-code-subagents-totalum)
- [My LLM coding workflow going into 2026 — Addy Osmani](https://medium.com/@addyosmani/my-llm-coding-workflow-going-into-2026-52fe1681325e)
- [Agentic Coding Workflow 2026: The End-to-End Loop](https://www.futureproofing.dev/resources/ai-native-team/agentic-coding-workflow-2026)
- [AI Coding Workflow Best Practices 2026: 12 Patterns From Senior Engineers](https://baeseokjae.github.io/posts/ai-coding-workflow-best-practices-2026/)
