# Daily AI-practice tip — how the routine runs

Fires each morning, before/with the email review. One tip per day. No exceptions,
no doubling up, no "here are five things".

## Each run

1. **Read state.** `profile/claude-usage-profile.md`, `profile/QUESTIONS-FOR-JOHN.md`,
   `tips/INDEX.md`, `research/tip-backlog.md`.
2. **Refresh the picture** (cheaply — don't re-derive the whole profile daily).
   Look for what changed: new TickTick projects or tasks, whether the last tip was
   adopted, anything in the repo John edited. Fold new facts into the profile.
3. **Pick one tip.** Highest-ranked backlog item that:
   - he is *not already doing* (check the profile before anything else — he already
     has coding standards with a self-verification loop; don't sell that back);
   - is grounded in something concrete from *his* data, ideally quoted;
   - is achievable in one sitting.
4. **Top up the backlog** when it drops below ~10 items, or weekly, whichever is
   sooner. Search for current practice; prefer primary/Anthropic sources and
   well-cited research over listicles.
5. **Write the tip** to `tips/YYYY-MM-DD-NNN-slug.md`, add a row to `tips/INDEX.md`.
6. **Commit and push** to `claude/youthful-curie-8b7tq7`.
7. **Deliver twice:**
   - **Notify** — the notification *is* the primary delivery. Lead sentence = the
     tip in one line (that's the phone banner); the body carries enough that he can
     act without opening anything.
   - **Create a TickTick task** in `💼Personal to Work Inbox`
     (id `68ac8bcae2bebe00c8e800c2`), titled `AI tip NNN — <headline>`, with the
     actionable version in the body. He approved this on 2026-09-21. It survives the
     morning review; the notification doesn't.

## Tone

He is a working developer, a music student, and in the middle of a house move and
a career change. He does not need cheerleading or a listicle. One specific change,
why it's aimed at him, what it costs, what breaks. Quote his own data back at him
when it makes the case.

## Standing rules

- One tip. Per day. Even when three look good — the others go in the backlog.
- Tailored beats novel. A well-aimed basic beats an exotic technique he won't use.
- Writing the daily tip into `💼Personal to Work Inbox` is approved. Any *other*
  write to TickTick, Gmail, Jira or Confluence needs his say-so first.
- Never propose anything that writes into his Obsidian vault — he has ruled that out.
- Never propose destroying or bulk-moving the BookStack wiki; other teams depend on it.
- If there is genuinely nothing new and useful, say so in one line rather than
  padding — but that should be rare while the backlog is stocked.
