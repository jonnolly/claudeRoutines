# Tip 2026-10-29 — Your "must always" rules aren't rules yet

**Time to adopt: ~10 minutes. Pays back every Trace Trimmer session after that.**

## Why you're getting this one first

In your Trace Trimmer backlog you wrote:

> "Reduce the start-time to under 1 second. **Make a rule that will definitely see whenever I
> start claude in this folder** that the start-time must always be under 1 second. **Test this
> each time you make a change.** If it doesn't fulfill this requirement, you must keep trying
> until you do fulfill this requirement. If you can't you have to let me know and let me know
> the new start-time."

That's a precise, well-specified ask — and as written it can't be satisfied, which is probably
why Claude keeps drifting off it. Anthropic's own memory documentation is blunt about the reason:

> CLAUDE.md and auto memory are **context, not enforced configuration**. To block an action
> regardless of what Claude decides, use a hook instead.

So a rule in `CLAUDE.md` is a strong suggestion that competes with everything else in the context
window. The word you used — *definitely* — needs a hook. Hooks are shell commands the harness
runs; they don't depend on Claude deciding to cooperate.

## The 10-minute version

**1. Keep the intent in `CLAUDE.md`** (so Claude knows *why*, and usually complies unprompted):

```markdown
## Hard constraint: start-up time
App start-up must stay under 1000ms. It was 4s; this is a headline requirement, not a nice-to-have.
Measure with `./scripts/measure-startup.sh` (prints integer ms). Never regress this to buy a feature.
```

**2. Add the enforcement** in the Trace Trimmer repo at `.claude/settings.json`:

```json
{
  "hooks": {
    "Stop": [
      { "hooks": [ { "type": "command", "command": ".claude/check-startup.sh", "timeout": 120 } ] }
    ]
  }
}
```

**3. `.claude/check-startup.sh`** (`chmod +x` it):

```bash
#!/usr/bin/env bash
# Blocks Claude from finishing its turn while start-up exceeds the budget.
set -uo pipefail
cat >/dev/null                      # drain the hook's JSON on stdin

BUDGET_MS=1000
MS=$(./scripts/measure-startup.sh)  # must print integer milliseconds

if [ "$MS" -gt "$BUDGET_MS" ]; then
  echo "Start-up is ${MS}ms, over the ${BUDGET_MS}ms budget. Profile it and reduce it. \
If it genuinely cannot be met, say so explicitly and report the measured number." >&2
  exit 2
fi
exit 0
```

## Why this shape

- `Stop` fires when Claude tries to finish responding. **Exit code 2 prevents it from stopping**
  and feeds your stderr text back to it — so the check runs on *every* turn, automatically, with
  no reliance on it remembering to test. That is your "test this each time you make a change".
- The escape hatch in the message ("if it genuinely cannot be met, say so and report the number")
  is deliberate — it's your own last sentence, and without it a blocking hook can trap Claude in
  a loop on an impossible target.
- `Stop` takes no `matcher` field; that's expected, not an omission.

## What you need to check first

You need `./scripts/measure-startup.sh` to exist and print milliseconds — I don't know Trace
Trimmer's stack, so I can't write it for you yet. If it doesn't exist, that script *is* the
10 minutes, and it's worth it regardless: an unmeasurable requirement can't be enforced by you
or by Claude.

## The general move

This generalises past start-up time. Any constraint you've ever repeated to Claude more than
twice — "don't touch the parser", "always run the tests", "keep the GUI responsive" — is a
candidate. Prose asks it; a hook guarantees it.

Sources: [Claude Code memory](https://code.claude.com/docs/en/memory) ·
[Claude Code hooks reference](https://code.claude.com/docs/en/hooks)
