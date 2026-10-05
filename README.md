# claudeRoutines

State for John's scheduled Claude routines.

## Daily AI tip routine

Runs each weekday morning alongside the email review. One tip per day, tailored, ≤15 min to act on.

| File | Purpose |
|---|---|
| `profile.md` | What's known about how John works and uses Claude. Updated as answers come in. |
| `questions-backlog.md` | Ranked questions for tailoring. Top ≤3 asked per morning, then retired to "Answered". |
| `tip-pipeline.md` | Researched tip backlog, ranked by gain ÷ adoption time. Prevents repeats. |
| `tips/<date>-<slug>/` | Each delivered tip, with any ready-to-copy scripts. |

### Operating rules
- **≤15 min/day total**, tip + questions combined. Money-generating output beats workflow polish.
- **John creates and schedules his own follow-up tasks and routines.** The routine suggests; it
  does not create TickTick tasks, crons, or routines on his behalf.
- Each tip must be *specific to his actual setup*, cite why it applies to him, and be verifiable.
  Scripts handed over get tested before they're recommended.
- Delivery is by push notification — nobody reads the session transcript.
