# AI Coach — one tip per day, under 15 minutes

Purpose: keep John ahead of the curve on effective AI/agent use **without** eating into
money-earning work. Hard budget: **15 minutes/day, including reading the tip.**

Guiding rule (John's words): *"It is good to keep improving workflow, but it is more
important to generate meaningful output that we can earn money with."*
So: one tip, one action, one question batch at most. If a tip can't pay for itself within
roughly a week of use, it goes to the bottom of the library.

## Files

| File | What it is |
|---|---|
| `PROFILE.md` | What we know about how John actually works + what is still assumption |
| `QUESTIONS.md` | Prioritised question backlog. Highest-value, fastest-to-answer at the top |
| `ANSWERS.md` | Answers as they come in. Feeds back into `PROFILE.md` and re-ranks the library |
| `TIP-LIBRARY.md` | Ranked, tailored tips. Each has a ≤15 min action |
| `TIP-LOG.md` | What was delivered when, and what John did with it |
| `SOURCES.md` | Where the advice comes from, so claims can be checked |

## Daily protocol (for whichever routine delivers the tip)

1. Read `TIP-LOG.md` → find the first tip in `TIP-LIBRARY.md` not yet delivered and not
   blocked by an unanswered question.
2. Send **one** tip: what it is, why it fits John specifically, the ≤15 min action, and
   the source. No menus, no alternatives, no survey of options.
3. Attach **at most one** question batch from `QUESTIONS.md` (top batch only, ~3 questions,
   answerable in under 5 minutes). Skip the batch entirely on days when the tip itself
   needs the full 15 minutes.
4. Append to `TIP-LOG.md`, move answered questions into `ANSWERS.md`, commit, push.
5. Never create TickTick tasks, routines or cron schedules on John's behalf. Propose the
   task text; **John adds and schedules it himself** so it never collides with
   value-adding work.

## Wiring it into the morning email review

This routine currently fires mid-morning, which is after the email review. Two options —
John's call:

- **Option A (preferred):** paste this into the existing email-review routine prompt:
  > After the email summary, open the repo `jonnolly/clauderoutines`, branch
  > `claude/blissful-galileo-h3h446`, read `ai-coach/TIP-LIBRARY.md` and `ai-coach/TIP-LOG.md`,
  > and deliver the next undelivered tip following `ai-coach/README.md`. Keep it under
  > 15 minutes of my time. Then append to `ai-coach/TIP-LOG.md` and push.
- **Option B:** re-schedule this routine to fire ~15 minutes before the email review.

Do not run both — that would double-deliver tips.
