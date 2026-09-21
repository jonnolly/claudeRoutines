# John's Claude / AI usage profile

Last updated: 2026-09-21 (rounds 1 and 2 folded in)

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

## Work rhythm **[confirmed]**

- **2.5-day week**, not 3.5 — updated 2026-09-21.
  - **Monday & Thursday** — in the office, full days.
  - **Tuesday & Wednesday** — 2 hours remote each, deliberately, to support a
    colleague who is new to the company and to keep correspondence and work moving
    through the week.
- **He has already found the async delegation loop, and it works.** In his own
  words: on the remote days he plans tasks, gives them to Claude to implement, and
  checks the result when he is next in the office. He calls it effective.
  → This is the single most important fact in this file. He is not a beginner at
  delegation; he has a *proven* pattern running on a two-hour budget. Tips should
  **scale and harden that loop**, not introduce it.
- Implication for tip design: his scarce resource is **review capacity on Monday
  and Thursday**, not agent capacity. Anything that increases output without
  increasing his review burden wins; anything that produces more diffs for him to
  read loses.
- He is also **mentoring** — a standing, recurring load worth designing for.

## Tooling

- Claude paid plan, partly expensed to New Electric. **[inferred]**
- Scheduled routines, including a daily **email review** and this tip routine. **[confirmed]**
- MCP connectors: **TickTick, Gmail, Atlassian (Jira/Confluence), GitHub**. **[inferred]**
- **Two TickTick accounts** — personal and work. Claude currently tidies the
  **personal** backlog only; awkward to get it to handle both. He has considered
  moving work to **Todoist**, but that would risk breaking the cross-account inbox
  bridge he relies on. **[confirmed]**
- **Cost of the daily tidy: 5 minutes to 1.5 hours per day**, mostly spent
  rescheduling out-of-date tasks. He estimates partial automation would bring it to
  **~15 minutes**. **[confirmed]** → No longer low priority. At the top of the
  range this is the largest single block of time any tip can return to him.
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

### 1. The weekly software meeting — his own pick for highest-value area

His words: *"The weekly software meeting is one of the most high value areas we can
improve. We have not historically been good at carrying forward long-term
improvement plans around anything."*

What he wants:
- Long-term goals (CI improvements especially) **broken into tiny, achievable
  weekly tasks**, one assigned per person per week.
- A physical ritual: **"who has the ball this week?"** — a literal ball placed on
  someone's desk representing that week's long-term task; their job is to get it to
  the middle table by the next meeting.
- A **visually attractive vision** of where this is heading, looked at every week,
  to sustain motivation. Today this is *"a google doc… which is very dry."*
  → He has explicitly asked for something visually pretty here. Strong candidate
  for a built artefact, but the *content* (their actual goals) must come from him —
  do not invent New Electric's roadmap.

### 2. The NESL Jira board is dead

`https://newelectric.atlassian.net/jira/software/projects/NESL/boards/10` — the
board for the embedded software library. Tasks get added when someone remembers it
exists; nobody ever reviews or works it. He wants it organised and **reviewed every
software meeting**. Pairs directly with pain point 1: the board becomes the source
of the weekly ball.

### 3. Confluence: actively used but badly organised

- `Software Development`, `CAT_330z_Battery`, `NEP_006_HX70` — in active use, but
  *"the file structure isn't so well organised."*
- `NE_EMBEDDED_SOFTWARE_LIBRARY` — **completely unused**, and he thinks it could be
  really useful. A greenfield space is the safest possible place to demonstrate a
  documentation structure before touching the live ones.

### 4. Documentation rot

Pages go stale because nobody updates them after a change. **Work repos are on
GitHub**, and he wants them **connected to Confluence** so that when code changes
make a page out of date, the page gets updated. → Note: this session's GitHub
access is scoped to `jonnolly/claudeRoutines` only; the work repos would need
access granted before any of this is buildable.

### 5. BookStack consolidation

`https://wiki.newelectric.ovh/shelves`. API access **pending** — the colleague
responsible is on holiday; John has a task to ask him next week. Blocked, not dead.

### 6. The TickTick tidy

Up to 1.5 hours a day. See Tooling above.

## Delivery preference **[confirmed]**

Tips arrive by notification (phone + email) at email-review time. He has approved
**also** dropping each tip into TickTick as a task, in `💼Personal to Work Inbox`
(the only work-relevant project Claude can reach).

## Working hypotheses about the biggest remaining gaps

- **He is the runtime** for personal questions (Tip 001 addresses this).
- **Nothing standardises his Claude behaviour across projects** — every project
  starts cold. Highest-value structural fix; next tip.
- **His proven async loop is running on one lane.** He plans tasks on a remote day,
  hands them to Claude, reviews next office day — and it works. The gap is not
  *whether* to delegate but **how many lanes, how well specified, and how much
  self-verification** happens before it reaches his review queue on Thursday.
- **Review capacity is the true bottleneck.** Two office days. Every tip should be
  tested against: does this add to Monday/Thursday reading, or subtract from it?
- **Nothing at New Electric carries long-term work forward between weeks** — and he
  has already designed the fix himself (the ball ritual). He needs the scaffolding,
  not the idea.
