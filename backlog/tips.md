# Tip backlog — ranked by (impact on revenue-producing output) ÷ (minutes to adopt)

Rules: one tip per day, delivered with the email review. Each tip must be adoptable in **≤10 min**
(leaving ~5 min for the day's questions). Must be something John is *not* already doing.
Re-rank every run — new evidence beats old ordering. Mark delivered tips with the date.

| # | Tip | Why it's high value for John | Min | Status |
|---|-----|------------------------------|-----|--------|
| 1 | **Enforce standing rules with a hook, not with prose in every prompt** | Directly fixes the observed pattern in his "reduce start-up time" task. Converts a re-typed instruction into a permanent, deterministic guardrail + gives Claude a verification signal to iterate against — the most-cited reliability lever in agentic coding. | 10 | **DELIVERED 2026-10-12** |
| 2 | **Give Trace Trimmer a `CLAUDE.md` + a `/trim-feature` slash command** | His TickTick prompts repeat the same CAN-trace domain context (`;` headers, epoch times, insight-converter filenames) every time. Hoisting it once cuts prompt-writing time and stops Claude re-learning the format. | 10 | pending |
| 3 | **Plan mode as a gate on the two multi-part tasks already in the backlog** | The "insight can converter" task has two stacked requirements and was edited 3× over 3 weeks — classic spec-drift. Read-only plan → approve → implement catches the misread before it costs a rewrite. | 5 | pending |
| 4 | **Run the Trace Trimmer backlog in parallel with git worktrees** | He has 7 independent queued features. `--worktree` gives each agent its own branch+dir; he keeps working in main checkout. This is the concrete version of the "multiple agents" he asked about. Needs a git repo + a merge habit. | 10 | pending (gated on Q3) |
| 5 | **Turn the repeated prompt shape into a Skill, not a longer prompt** | Skills load only when invoked, so they don't burn context like a fat CLAUDE.md. Good fit for "add a new trace-file format" which he'll clearly do again. | 10 | pending |
| 6 | **Subagents per *feature area*, not per *role*** | Counter to the obvious "assign roles" instinct he mentioned — current guidance favours feature-specific subagents over generic `qa`/`architect` roles, because the fresh context window is the real benefit, not the persona. Saves him from building the wrong thing. | 5 | pending |
| 7 | **Stop re-typing prompts: TickTick task → Claude Code via the MCP he already has** | He already has TickTick MCP connected. A routine could pull the next ✂Trace Trimmer task and run it, instead of him copy-pasting. This is his "continuously working agents" ask, scoped safely. | 10 | pending |
| 8 | **Ship his team the setup, not just himself** | He's on a Team plan with colleagues. Shared skills/plugins/CLAUDE.md in a repo multiplies one evening of setup across the team — highest-leverage item on the list *if* colleagues write code. | 10 | pending (gated on Q6) |
| 9 | **Spec-anchored tasks: keep the spec in-repo and diff it against code** | Addresses silent spec/code drift, the named failure mode of exactly his workflow (specs live in TickTick, code lives in git, nothing reconciles them). | 10 | pending |
| 10 | **A verification subagent that only tries to break the change** | Cheap reliability win: one adversarial pass over his own diff before he looks at it. Pairs with #1. | 5 | pending |
| 11 | *(personal)* **Claude as a structured-decision partner for the retirement-fund question already parked in 🟥Claude questions** | He parked it and hasn't run it. A 10-min framing (constraints → options → monthly number → FI date) unblocks a real life-goal decision. | 10 | pending |

## Source notes (for credibility when challenged)
- CLAUDE.md is advisory and loads at session start; hooks in `settings.json` are deterministic shell commands the harness runs regardless of model choice. Community guides put CLAUDE.md adherence around 80% and recommend keeping it under ~200 lines.
- Claude Code auto-ends a turn after 8 consecutive **Stop**-hook firings → prefer `PostToolUse` for self-correcting loops and always give a real exit condition.
- Explore → Plan → Implement → Commit, with a testable exit condition ("iterate until this passes"), is the consensus loop.
- Spec-driven development consensus flow: constitution → specify → clarify → plan → tasks → implement → analyze, with human gates at phase boundaries. Named failure modes: context explosion and silent spec-code drift.
- Worktrees isolate files but not *intent* — parallel agents can each be locally correct and still collide at integration. Keep parallel work to genuinely independent features.
