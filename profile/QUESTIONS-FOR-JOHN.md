# Open questions

Answer however is easiest — reply to the routine session, edit this file, or tell
Claude next time. Answers get folded into `profile/claude-usage-profile.md`.

## Round 1 — asked 2026-09-21, ANSWERED 2026-09-21 ✅

All seven answered. Folded into the profile. Summary of what changed:

1. **Where coding happens** → VS Code, and Claude via *both* desktop app and the
   VS Code extension. Keeps the extension partly because it opens one folder
   containing several git repos. → `/add-dir` answers this; see answer log.
2. **`claudeCodingStandards`** → status unknown; wants standards applied by default
   across every project. → Promoted to the next tip.
3. **Multiple Claudes at once** → never done it; asked whether he should. → Yes,
   but asynchronously rather than concurrently. Tip queued.
4. **Obsidian vault** → same machine, but **no agent writes**. Read-only at most.
   Instead he raised **Confluence doc rot** and **BookStack/Confluence sprawl**.
5. **Worst repeated chore** → TickTick backlog cleanup, made worse by having two
   accounts (personal tidied by Claude, work not). Low priority unless it starts
   eating real time.
6. **Work vs personal** → `💼Personal to Work Inbox` is work-relevant;
   `🧔Work to Personal Inbox` is personal.
7. **Delivery** → yes, also drop the tip into TickTick, in `💼Personal to Work Inbox`.

## Round 2 — asked 2026-09-21, ANSWERED 2026-09-21 ✅

1. **TickTick tidy cost** → 5 min to 1.5 hours a day, mostly rescheduling
   out-of-date tasks; ~15 min if partly automated. → Promoted to tier 1.
2. **Confluence** → `Software Development`, `CAT_330z_Battery`, `NEP_006_HX70`
   active but poorly structured; `NE_EMBEDDED_SOFTWARE_LIBRARY` unused and
   promising. Plus: the NESL Jira board is dead, and the weekly software meeting is
   his own pick for highest-value area to improve.
3. **BookStack API** → pending; colleague on holiday, he'll ask next week.
4. **Work repos on GitHub** → yes, and he wants them connected so Confluence pages
   update when code changes make them stale.
5. **Week shape** → 2.5 days: Mon & Thu in office, 2 remote hours Tue & Wed. He
   already plans tasks, hands them to Claude, reviews next office day — and it
   works. This reshaped the whole backlog.

## Round 3 — open

1. **The vision board (tier 2, item 9).** You asked for something visually pretty to
   replace the dry Google doc. I can build it — but the content has to be yours.
   Paste the Google doc, or spend twenty minutes telling me what the long-term
   goals actually are, and say go.
2. **Who else is in the weekly software meeting**, and how long is it? The ball
   ritual only works if the weekly slice is sized to the room.
3. **Which CI improvements** are the long-term goals you'd start the ball with?
   Naming two or three makes item 8 concrete instead of theoretical.
4. **Work GitHub access.** Which org/repos, and are you able to grant Claude access
   to them? Item 12 is blocked without it.
5. **How much of your Monday/Thursday actually goes on reviewing Claude's work**
   from the remote days? If it's already heavy, hardening (tips 2, 3, 5) comes
   before widening (tip 4).

## Answer log

**2026-09-21 — desktop app vs. VS Code extension, multi-repo folders.**
You don't have to choose for that reason. Claude Code works across multiple
directories in one session: `/add-dir <path>` during a session, or `--add-dir` with
several paths at launch. So a parent folder containing several repos works in
either surface, and you can also start in one repo and pull in a second. Caveats
worth knowing: sources disagree on whether added directories are read-only or fully
writable, so verify on your own setup before relying on cross-repo edits; and
loading `CLAUDE.md` files *from* added directories needs
`CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` (v2.1.20+). Pick the surface on
the things that actually differ — the extension gives inline diffs and editor
context; the desktop app is better for running work in the background while you do
something else.
