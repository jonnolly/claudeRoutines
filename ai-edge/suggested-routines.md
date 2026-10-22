# Routines worth scheduling — John schedules these himself

The routine never creates tasks, cron jobs or TickTick entries. These are proposals only.
Each entry: what it would do, when it should run, and what it needs first.

### A. `@claude` task sweeper
Pick up TickTick tasks tagged `@claude`, do the ones that are self-contained, and report back.
Several have sat untouched since mid-October, including two in "Remote Work".
**When:** mid-morning on a work day, after the email review, so its output lands while you can act on it.
**Needs first:** agreement on what it may do unattended (open a PR? only draft?) and which
repos it may touch. Worth answering Q5 before scheduling.

### B. Nightly green-keeper on CanTraceSplitter
Run the suite, and if it is red, diagnose and open a PR with the fix.
**When:** overnight — you review the PR with coffee, not with a session open.
**Needs first:** tips 1 and 2 (a test suite that cannot lie, and the startup-time check).
Pointless until then: a nightly run of a vacuously-green suite just reassures you.

### C. Weekly parked-question burner
Take everything in `🟥Claude questions`, research it properly, and come back with answers.
**When:** Sunday evening or any fixed 15-min slot.
**Needs first:** nothing. This one is ready now, and it is the cheapest of the three.

### D. Upwork / contract scanner
Watch the channels you choose for posts matching the CAN-bus / embedded-Python / instrumentation
niche, and draft a proposal for the best one or two.
**When:** daily, early. Applications are a volume game and they are currently at zero.
**Needs first:** Q4 (is Upwork actually the channel) and tip 16 (the `/proposal` skill).
