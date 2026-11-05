# Tip 1 — 2026-11-05: stop asking Claude to remember; make the repo enforce it

## Why you specifically
Your Trace Trimmer task "reduce start-up time" says:

> *"Make a rule that will definitely see whenever I start claude in this folder that the start-time
> must always be under 1 second. Test this each time you make a change. If it doesn't fulfill this
> requirement, you must keep trying until you do fulfill this requirement."*

You've correctly identified that you want a *persistent, self-verifying invariant*. But asking for it
in a prompt is the one delivery mechanism that can't provide it. Anthropic's own steering guidance
calls this out directly: instructions are **advisory**, they fail "in a long session or an ambiguous
situation", and *"Every time X, always do Y" belongs in a hook, not CLAUDE.md*. Hooks run every time,
as actual shell commands.

## The 12-minute version
1. Write a script that measures cold-start and exits non-zero over budget —
   `scripts/check-startup.ps1` (or `.sh`), printing the measured time either way.
2. Wire it as a `PostToolUse` hook in `.claude/settings.json` so it fires after every code edit:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "pwsh -File scripts/check-startup.ps1" }
        ]
      }
    ]
  }
}
```

3. Exit code **2** feeds stderr back to Claude as something it must fix — which is exactly the
   "keep trying until you fulfil this requirement" loop you were asking for by hand, except it can't
   be forgotten or talked out of.
4. Put the single line `Startup must stay under 1s — enforced by the PostToolUse hook.` in CLAUDE.md
   so Claude knows *why* it's being blocked.

**Fastest path:** open Claude Code in the Trace Trimmer folder and ask it to set this up — the
`update-config` skill handles settings.json and hook wiring for you. Verify by making a deliberately
slow change and checking that it blocks.

## What you get
The requirement outlives the session, the conversation, and your memory of having asked for it. And
it's a template: every future hard requirement becomes a script plus four lines of JSON.

⚠️ One caveat worth knowing: don't attach this to a `Stop` hook — Claude Code overrides and ends the
turn after ~8 consecutive Stop-hook blocks, so a genuinely slow build would just stall. `PostToolUse`
is the right place. (Hook limits come from community guides; check the official docs if it misbehaves.)
