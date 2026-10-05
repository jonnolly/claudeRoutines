# Tip 001 — 2026-10-05 (Mon)

## Stop *asking* Claude to keep checking. Make it structurally unable to stop.

**Time to apply: ~10 minutes. One-time. Pays back on every Trace Trimmer session forever.**

### Why this one, for you specifically

In your Trace Trimmer task "reduce start-up time" you wrote, by hand, in the description:

> "Make a rule that will **definitely** see whenever I start claude in this folder that the
> start-time must always be under 1 second. **Test this each time you make a change.** If it
> doesn't fulfill this requirement, **you must keep trying** until you do fulfill this
> requirement. If you can't you have to let me know and let me know the new start-time."

That is a precise, correct instinct — and it is the thing Anthropic's own guidance calls the
single most impactful practice: give Claude a check it can run, and the loop closes by itself.
But written as prose in a prompt, it's *advisory*. Claude reads it, means it, and then stops
when the work "looks done" — because looking done is the only signal prose provides. Rules in
prompts and in `CLAUDE.md` decay, especially as the file grows and the session gets long.

A **`Stop` hook** is not advisory. It is the one hook that can refuse to let Claude finish its
turn: exit code 2 blocks the stop and hands your stderr text back to Claude as the reason it
must continue. Your paragraph above becomes a thing the harness enforces, not a thing Claude
remembers. Same words, infinitely more reliable.

### Do this

1. Copy `verify_startup.py` into the Trace Trimmer repo at `.claude/hooks/verify_startup.py`.
2. Set the two knobs at the top:
   - `BUDGET = 1.0` — your 1-second target.
   - `ENTRY` — the real cold-start command. For a GUI app don't launch the window; measure the
     import, which is where nearly all of a 4-second Python GUI start actually goes:
     `["python3", "-c", "import trace_trimmer"]` (use your real module name).
3. Merge `settings-snippet.json` into the repo's `.claude/settings.json`.
4. Prove it works, in the repo: `echo '{}' | CLAUDE_PROJECT_DIR=$PWD python3 .claude/hooks/verify_startup.py`
   You should see either `Startup gate passed: 0.xxs` or a `FAILED` message with exit code 2.
5. Add `.claude/.startup-ok` to `.gitignore`.

Then just say "make startup faster" and stop supervising. Claude cannot hand the work back
to you while the app still starts in 4 seconds.

### What's already handled in the script

- **Only measures when Python sources actually changed** since the last green run — so it isn't
  paying 3 process launches on every single turn.
- **Takes the fastest of 3 runs**, so a noisy laptop doesn't produce a false failure.
- **Loop guard**: honours `stop_hook_active`, so if Claude truly can't hit the budget you get
  told, instead of an infinite retry loop burning tokens.
- **Fails loudly if the entry command errors**, rather than silently reporting a fast "startup".
- The failure message tells Claude *how* to fix it (`-X importtime`, defer heavy imports), not
  just that it failed. Failure text is a prompt — it's worth writing well.

### The generalisation (this is the real tip)

Any sentence you find yourself repeating to Claude in prose — "always run the tests", "never
commit without lint", "keep the GUI responsive" — is a candidate for a gate. Prose is a wish;
a check with an exit code is a guarantee. You already have one budget worth enforcing. The next
ones for Trace Trimmer are probably: the app launches without an exception, and a known trace
file trims to the byte-identical expected output (a fixture diff — cheap, and it's the thing
that will catch Claude silently breaking your `insight` file-format handling while fixing
something else).

### Sources
- Anthropic, *Building verification loops in Claude Code with skills* — https://claude.com/blog/building-verification-loops-in-claude-code-with-skills
- Claude Code docs, *Hooks* (Stop hook blocking semantics, exit code 2) — https://code.claude.com/docs/en/hooks
- Claude Code docs, *Best practices* — https://code.claude.com/docs/en/best-practices
