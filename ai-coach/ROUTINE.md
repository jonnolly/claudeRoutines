# How the daily AI-tip routine should run (protocol for future runs)

Target: **≤15 minutes of John's time**, and not much more of the routine's own effort.

1. Read `ai-coach/PROFILE.md`, `ai-coach/BACKLOG.md`, `ai-coach/TIPS.md`.
2. Pick up any answers John has given since the last run (session reply, email, or a note in
   this repo). Fold them into PROFILE.md and tick off the Tier 0 questions.
3. Re-rank the backlog if anything material changed. Otherwise don't churn it.
4. Pick **one** tip: the top unticked item that fits today (see alternation note in TIPS.md).
   It must be concrete, doable in ≤15 min, and something he isn't already doing.
5. Optionally attach **one or two** short questions — only ones answerable in a minute or two.
6. Send it with `PushNotification` wrapped in `<routine_summary>` tags. First sentence = the
   phone banner, so it must carry the actual action, not "here's today's tip".
7. Append to TIPS.md, commit, push to the designated branch.

## Hard rules

- Never create TickTick tasks, Jira issues, or scheduled routines on John's behalf. He
  schedules his own work. Suggest the task and let him add it.
- Never send email; drafts only, and only once he's authorised it.
- A quiet day is allowed. If there's genuinely nothing better than yesterday's tip, say
  nothing rather than manufacture a tip — but that should be rare while the backlog is full.
- Research is a means, not the output. Don't send a reading list; send one action.
