# Question queue (highest value first)

Rules: only questions answerable inside the 15-minute window get surfaced. One or two per day max,
and only when the answer would change which tips come next. Answers get folded into `profile.md`.

## Asked — awaiting answer

### Q1 — the tick-box (asked 2026-11-26, ~2 min)
Which of these are you *already* using? Just tick.
`CLAUDE.md` · `.claude/rules/` · hooks · skills (`/slash` commands) · subagents · plan mode
(shift-tab) · git worktrees / parallel sessions · `/loop` · permission allowlist · MCP servers
beyond the ones in these routines.
*Why it's first: every tip below is ranked on a guess about this. Two minutes of ticking stops me
teaching you things you already do.*

### Q2 — verification (asked 2026-11-26, ~3 min)
For Trace Trimmer: is there a command that proves it still works — `pytest`, a lint, a build, a
start-up timer — that exits 0/1? Or is checking still "run the GUI and click"?
*Why: an executable pass/fail is the thing that makes unattended Claude work safe. Without one,
half the throughput tips are unusable.*

### Q3 — where the money is this quarter (asked 2026-11-26, ~2 min)
Which single track should tips bias toward until February: (a) Upwork/contracting, (b) teaching
(Codementor/Wyzant), (c) music income + AIM award, (d) none — just make the day job faster so
school fits?
*Why: decides whether tips lean dev-workflow or output/marketing.*

## Queued — not yet asked

- **Q4** Where does Claude Code run — work laptop terminal, desktop app, web? And is it allowed on
  New Electric's firmware repos, or personal tools only? (policy question, 3 min)
- **Q5** Besides Trace Trimmer, what other repos/folders do you point Claude at? (2 min)
- **Q6** What's the most repetitive 30+ minute task in a normal work week? (3 min — best single
  input for a high-value automation tip)
- **Q7** How many Claude sessions are you willing to run at once, and on what machine? (worktree /
  parallel-agent tips depend on it)
- **Q8** Does usage cost or rate-limiting shape your choices today? (model/effort tips)
- **Q9** Do you want music/personal-development tips in the rotation, or dev + PM only?
- **Q10** Is Obsidian the place written output should land, or TickTick?
- **Q11** Do you ever review Claude's diffs line by line, or mostly accept and test? (sets how hard
  to push review automation)
