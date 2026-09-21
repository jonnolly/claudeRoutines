# John's Claude / AI usage profile

Last updated: 2026-09-21 (round 1 answers folded in)

**[confirmed]** = stated by John. **[inferred]** = derived from his connected
accounts (TickTick, Gmail metadata, GitHub) during a routine run.

## Who / context

- John Connolly, `john@newelectric.nl`, GitHub `jonnolly`. Europe/Amsterdam–Berlin. **[inferred]**
- Works at New Electric on a **3.5-day contract**, keeping ~1.5 days free and
  actively hunting remote work. **[inferred]**
- Also a **music student** — Zuyd conservatoire first year (jazz, trumpet, piano),
  plus gigs, recording, theory homework. **[inferred]**
- Mid-life reorganisation: house move, mortgage decisions (Maastricht vs. a
  2-day-a-week Utrecht commute), retirement modelling, counselling, gratitude
  journal, goal reviews. **[inferred]**
- **Time is the scarce resource, not ideas.** Tips should buy back hours.

## Environment **[confirmed]**

- **Editor: VS Code.** Uses Claude via *both* the **desktop app** and the **VS Code
  extension**, switching between them, unsure which is better.
- Values the VS Code extension for one specific reason: he can **open a single
  folder containing multiple git repos** and work across them. Wants to know
  whether the desktop app can do the same. → Answered 2026-09-21: yes, via
  `/add-dir` (see `tips/` and the answer log below).
- Obsidian vault **is on the same machine** as Claude Code, but he **does not want
  an agent writing into it**. Read-only at most. Do not propose vault-writing tips.

## Tooling

- Claude paid plan, partly expensed to New Electric. **[inferred]**
- Scheduled routines, including a daily **email review** and this tip routine. **[confirmed]**
- MCP connectors: **TickTick, Gmail, Atlassian (Jira/Confluence), GitHub**. **[inferred]**
- **Two TickTick accounts** — personal and work. Claude currently tidies the
  **personal** backlog only; he has found it awkward to get Claude to handle both.
  He has considered moving work to **Todoist** to solve it, but that would risk
  breaking the cross-account inboxes he relies on. **Low priority for now**, rising
  only if the daily tidy-up starts costing real time. **[confirmed]**
- **BookStack** wiki at `https://wiki.newelectric.ovh/shelves` — largely abandoned
  by the software team, **still used by other teams**, so it must not be destroyed.
  **[confirmed]**

## The two inbox projects **[confirmed]**

These are the bridge between his two TickTick accounts, and he uses them heavily.

- `💼Personal to Work Inbox` — things he thinks of **outside** work that he must do
  **at** work. **Work-relevant.** (id `68ac8bcae2bebe00c8e800c2`)
- `🧔Work to Personal Inbox` — things he thinks of **at** work that are **personal**
  and belong outside work. **Not work-relevant.** (id `67a1dca8ebbf3b00000005c3`)

Note this is where most of the "ask claude …" tasks live — i.e. personal questions
captured while at work.

## Coding projects

- `✂Trace Trimmer` (task: "reduce start-up time") **[inferred]**
- `❤Gratitude Journal` — an app he is building **[inferred]**
- `claudeRoutines` (this repo) **[confirmed]**

## How he uses Claude today

1. **Queued one-off conversations — the dominant pattern.** ~14 TickTick tasks that
   *are* Claude prompts, several with the prompt fully drafted in the body, some
   open for months. He is the runtime. → Tip 001. **[inferred]**
2. **Claude as adviser across life domains** — jazz practice plans, ADHD notes,
   ethics reading, mortgages, retirement maths, a CBT-therapist profile. **[inferred]**
3. **`claudeCodingStandards.md` exists but its status is unknown to him.** Written
   Sept 2025, specifying reproduce → test → fix → verify, and intended to apply
   across projects. He confirms he **does not know whether anything loads it**, and
   what he actually wants is *"a standardised way to use claude across all projects,
   using the same standards by default unless otherwise specified."* **[confirmed]**
   → This is now a top-priority tip, not a check.
4. **He has never run more than one Claude at once** — no subagents, no parallel
   sessions, no worktrees. Asked whether he should. **[confirmed]**
5. **Claude tidies his personal TickTick backlog** already. **[confirmed]**

## Live pain points **[confirmed]**

- **Documentation rot at work.** Confluence pages go stale because nobody
  remembers to update them after a change. He wants **documentation updated as
  changes are made**. He has Atlassian MCP already — this is achievable.
- **Documentation sprawl.** Docs spread across Confluence *and* BookStack. He wants
  **consolidation**, without removing BookStack for the other teams still using it.
- **Most annoying repeated chore:** cleaning the TickTick backlog — and the fact
  that it only works on one of his two accounts.

## Delivery preference **[confirmed]**

Tips arrive by notification (phone + email) at email-review time. He has approved
**also** dropping each tip into TickTick as a task, in `💼Personal to Work Inbox`
(the only work-relevant project Claude can reach).

## Working hypotheses about the biggest remaining gaps

- **He is the runtime** (Tip 001 addresses this).
- **Nothing standardises his Claude behaviour across projects** — every project
  starts from scratch. Highest-value structural fix.
- **Never parallelised.** The right first step for him is *asynchronous* work
  (agents running while he's at a lesson or a gig), not *concurrent* worktrees —
  his bottleneck is his own review time, and he has very little of it.
- **Work documentation is decaying on a schedule** and he knows it.
