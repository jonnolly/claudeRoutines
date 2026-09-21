# Tip 001 — Stop being the runtime for your own prompts

**Delivered:** 2026-09-21
**Theme:** continuous / background agents
**Effort:** ~20 minutes to set up, once
**Applies to:** personal + life admin (and later, code)

## What your data shows

Your TickTick contains roughly fourteen tasks that *are* Claude prompts:

- "ask claude what the state of music therapy is in southern france and north-west spain"
- "ask claude which jazz albums have no chordal instruments"
- "Get Claude to create spreadsheet for long term savings" — created 4 June, still open
- "continue asking claude about maastricht mortgage" — recreated 18 Sep, still open
- "ask claude what options there are to plan habits according to your daily schedule"

The sangomas one is the tell. Its body is a **complete, well-written prompt** —
"Hi Claude, please give me a list of the top books about sangomas… preferably
under 350 pages…". You had already done the hard part. It then waited four days
for you to be free to paste it in.

That is the pattern: **you are the runtime.** The thinking is done, the prompt is
written, and the only missing ingredient is you, sitting down, with a free hour.
Meanwhile the savings-plan question — arguably the highest-value one in the list —
has been open for three and a half months.

## The change

Let the queue drain itself.

1. **Tag the prompts.** Add a TickTick tag, e.g. `@claude`. From now on, when you
   catch yourself writing "ask claude …", write the *actual prompt* in the task
   body (you already do this half the time) and tag it.
2. **Add a second scheduled routine** — same mechanism as this one, ~06:00, just
   before the email review. Its job:
   - find open tasks tagged `@claude`;
   - run **each one as its own subagent**, so six unrelated questions (mortgage,
     jazz albums, ADHD notes) never bleed into each other's context;
   - write each answer back as a **comment on the task**, leaving the task open;
   - notify once: *"3 answers waiting."*
3. **Keep the close.** Deliberately do not let it complete the tasks. You still
   decide what was useful — you just stop being the one who presses go.

Your morning review then changes shape: instead of a list of work you must
*start*, it's a list of answers you *read*.

## Why this one first

Of everything you could adopt — worktrees, agent teams, roles, hooks — this is
the one your own data is screaming for, and it's the cheapest. You already have
every piece: the TickTick MCP connector, working scheduled routines, and a habit
of writing the prompt down. Nothing new to learn; one routine to write.

It's also exactly the shape 2026 practice has converged on: one orchestrator
running agents while you sleep, you giving goals and reviewing finished output,
with subagents used for per-task context isolation rather than one long polluted
conversation.

## Caveats

- Several of these questions carry real personal and financial detail (mortgage,
  retirement, counselling). This all stays inside your own connected accounts —
  but keep those prompts in this private setup, not in anything shared with work.
- Start with the low-stakes half of the queue (books, jazz, habits) for a week.
  Once you trust the answers, let it take the mortgage and savings questions.
- If a prompt is genuinely a conversation rather than a question, tag it
  differently — this handles one-shot research well and dialogue badly.

## First action today

Tag three tasks `@claude` — the jazz-albums one, the habits-planning one, and the
savings spreadsheet — then ask Claude to write the routine. Twenty minutes, and
by tomorrow morning three things you've been carrying since June are answered.
