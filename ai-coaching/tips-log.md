# Tip log

---

## Tip 001 — 2026-11-23 — Turn your hardest prose requirement into a check Claude can run
**Theme:** verification loops · **Est. time:** 12 min · **Target:** Trace Trimmer

**What I noticed in your own words.** Your Trace Trimmer ticket says:

> "Reduce the start-time to under 1 second. Make a rule that will definitely see whenever I
> start claude in this folder that the start-time must always be under 1 second. Test this
> each time you make a change. If it doesn't fulfill this requirement, you must keep trying
> until you do fulfill this requirement."

You knew exactly what you wanted and asked for it in the one form that cannot guarantee it.
A line in `CLAUDE.md` or a prompt is *non-deterministic*: Claude reads it and decides. A hook
is *deterministic*: the harness runs it every time, whatever the model decided. Anthropic's
current best-practices page is blunt about this: "If you keep adding emphasis to a CLAUDE.md
line and Claude still misses it, that's a sign the line belongs in a hook."

**Today's 15 minutes** (your own repo, nothing at stake):
1. In Trace Trimmer, prompt: *"write a test that measures cold start time and fails if it's
   over 1.0 s, then add a Stop hook in .claude/settings.json that runs it and exits 2 on
   failure."* (~6 min)
2. Ask Claude to deliberately slow start-up, and watch the turn refuse to end. (~4 min)
3. Delete the prose version of the rule from the ticket and from any `CLAUDE.md`. (~2 min)

**Why this one first.** You write requirements for a living — the W150Fi tickets (300 A per
pack, 60 V DC-link timeout, 170 kW in LOW_POWER_MODE) are the same skill. "Prose requirement →
runnable check" is the move that makes every later automation trustworthy, and it's the first
two of Anthropic's five pre-flight questions for a run nobody is watching: does it know what
done looks like, and can it check its own work? Everything else is worth less until that
exists, because a check is what lets a run finish without you and be believed afterwards.

**Heads-up on your own list.** You suggested multiple agents, assigned roles, continuous
running. Two of those are now explicitly on Anthropic's "what you can stop doing" table:
*"use subagents to protect your context window"* (1 M context + automatic compaction made it
moot) and *"delegate to a subagent for a better answer"* (same model, same task — you get
parallelism, not intelligence). What still pays: genuinely parallel independent work, keeping
noisy output out of your main session, and above all an **independent reviewer that never saw
your reasoning** (`/code-review`, or a `.claude/agents/reviewer.md` given only
`tools: Read, Grep, Glob` so it physically cannot edit). That's the version of your instinct
worth a slot later this week — not a cast of named roles.

**Questions surfaced:** Q1 (are work repos in scope for Claude), Q2 (which surfaces you use).
