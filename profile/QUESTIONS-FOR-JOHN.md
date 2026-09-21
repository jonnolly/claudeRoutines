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

## Round 2 — open

1. **How much time does the daily TickTick tidy actually cost you?** You called it
   low priority "unless I'm wasting a lot of time every day". A rough number
   decides whether the two-account problem gets solved or stays parked.
2. **Which Confluence spaces matter?** For the doc-freshness work: which spaces or
   page trees are the ones that hurt when they go stale, and does the software team
   own them?
3. **Does the BookStack wiki have an API token you could give a script?** It changes
   whether consolidation is "an agent does it" or "an agent makes you a plan".
4. **Do your work repos live on GitHub too**, and would you want Claude to have
   access to them — or should everything work-side stay on the Jira/Confluence
   connectors only?
5. **What does a typical week actually look like** — which days are New Electric,
   which are conservatoire, where do the 1.5 free days land? Timing tips to your
   real calendar matters more than the tips themselves.

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
