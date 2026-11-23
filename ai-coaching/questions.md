# Calibration question backlog (highest value at top)

Rules: every question must be answerable in **one or two sentences**, inside the 15-minute
window, with no prep. Max 1–2 surfaced per day. Answers go into `profile.md` and the
question is deleted from here.

Ranking = (how much it changes the advice) ÷ (seconds to answer).

---

### Tier 1 — these gate everything else

**Q1. Are you allowed to run Claude on New Electric's own repos** (`NEP_006_HX70_HVAC`,
`NEDCKR_MECH_bomBOM`, `NEDCKR_LOG_eShelf`), or is Claude effectively limited to personal
tooling like Trace Trimmer plus chat?
→ *Why:* this is the single biggest fork. If work repos are in scope, the money-making tips
are hooks/checks/reviews on firmware and the internal web tools. If not, every tip has to
route through Trace Trimmer, requirement writing, and email/admin instead.

**Q2. Which surfaces do you actually use?** Claude Code in the terminal / desktop app /
claude.ai web, plain claude.ai chat, the Jira+Confluence AI (Rovo), GitHub Copilot — and
roughly what split?
→ *Why:* hooks, skills, worktrees, `/effort` and routines only exist in Claude Code. If you
are mostly in chat, the whole tip series should be different.

**Q3. Where does your time actually go in a bad week?** Rank these: writing/grooming
requirement tickets · reviewing others' PRs · debugging CAN logs and field issues ·
meetings + notes + follow-ups · email/admin · firmware coding.
→ *Why:* I can only aim at the bottleneck if I know which one it is. The W150Fi review
volume suggests requirements, but that's a guess.

### Tier 2 — sharpen the aim

**Q4. Those AI-shaped PRs on `bomBOM` and `eShelf` ("Speed round 3…", "Lean stock…") —
yours, a colleague's, or Copilot's?**
→ *Why:* if a teammate is already running agents on those repos, the fastest win is copying
their setup, not inventing one. If they're yours, you're further along than I assumed.

**Q5. What's already set up?** Any `CLAUDE.md` files, `.claude/skills/`, hooks, custom
subagents, or other routines besides this one?
→ *Why:* stops me recommending what you already have.

**Q6. What is the money-making output right now** — shipping W150Fi/HX70 on time, the
internal tools, or something outside New Electric?
→ *Why:* your constraint was "meaningful output we can earn money with". I should point the
15 minutes at that thing specifically.

### Tier 3 — scheduling and scope

**Q7. When does "beginning of the day" start,** and should the tip land before or after the
email review? (This run fired ~08:45 CET.)

**Q8. Is Obsidian the knowledge store you'd want Claude reading/writing** (the "Add to
Obsidian" list), and is the vault on a machine Claude can reach?

**Q9. Do you want personal-development tips in the rotation** (jazz practice at Zuyd, goal
reviews, the retirement-fund question you parked), or keep this work-only?
→ *Why:* you said personal counts "if it is particularly useful". Default until you say
otherwise: ~1 personal tip a week, the rest work.

### Parked (useful later, not worth 15 min yet)
- Which model/effort you normally run, and whether you've hit usage limits mid-task.
- Whether New Electric has an Anthropic org plan or you're on a personal subscription.
- Whether you'd use a shared team skill (release/review procedure) if you wrote one.
