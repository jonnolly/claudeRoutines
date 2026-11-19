# Profile — John Connolly (how AI gets used, and where the gaps are)

Last updated: 2026-11-19 (first build, from observable sources only — not yet confirmed by John)

## Work context (observed, high confidence)

- Engineer at **New Electric** (newelectric.nl, NL) — electrification of heavy machinery:
  battery packs, BMS, contactors/precharge, DC-link, motor controllers, HV safety.
- Current focus: **W150Fi design review** and **CAT 330Z battery** (Jira projects
  `NEP_007_W150Fi`, `NE_124_CAT_330Z_Battery`). Review tickets are requirement-anchored
  ("requirement 3.11", "requirements 4.24 to 4.31"): LOW_POWER_MODE limits, per-pack
  current limits, welded-contactor warnings, DC-link discharge timeouts, OBS bench test
  plans (OT1–OT11).
- So the day job is **safety-critical embedded + requirements/traceability + test planning**,
  not web app CRUD. This matters: published evidence says LLMs do well on text-level review
  (style, null checks, bounds) and badly on register behaviour, ISR safety and timing, while
  the *documented* weak spot is traceability between requirement and code — which is
  exactly the part that is also the most tedious for a human.
- Tooling in reach: **Jira + Confluence** (newelectric.atlassian.net), **Google Chat**,
  **Gmail**, GitHub (`jonnolly`). Colleagues: Rogier van Rooijen, Frank de Boer,
  Adarsha BN, Shahbaz M.
- A **"new workflow / new colleague"** rollout is in progress (Frank, 2 Nov): dev-env docs
  heading into a "devdock". Good moment to land conventions as skills/CLAUDE.md.

## Personal context (observed)

- Heavy, well-organised **TickTick** user: GTD-style projects plus Goal Reviews, Career,
  Councilling, Gratitude Journal, Admin Power Hours, Someday/Reference, and a
  **`🟥Claude questions`** project used to park things to ask Claude later.
- **Obsidian** user (`♦Add to Obsidian` project).
- Studying **jazz at Zuyd** (sax/piano, theory homework, recording projects), learning
  **Dutch**, moving house / starting school. Side project: **Trace Trimmer**.
- Reads **TLDR**, **TLDR AI**, **TLDR Dev** daily — many land unread. He is already
  exposed to headline-level AI news, so coaching must be about *practice*, not news.
- Does a morning **email review** — the chosen delivery slot for the daily tip.

## AI usage (observed, low confidence — needs confirmation)

- Pays Anthropic personally and forwards the receipt to Shahbaz → likely expensing a
  Claude subscription through New Electric.
- Runs **Claude cloud sessions / routines** (this session) against `jonnolly/claudeRoutines`,
  which contained only a README before this run → routine infrastructure is brand new.
- Connectors live on the account: Atlassian, Gmail, TickTick, GitHub.
- Stated interests (his own words): multiple agents, assigning roles, agents working
  continuously. Note: two of those three are partly **2025-era advice** that current docs
  have retired (see tip T16) — worth correcting early so effort goes where it pays.

## Known gaps (drive `questions-backlog.md`)

1. Where Claude actually runs: claude.ai chat / Claude Code terminal / cloud / desktop / mobile.
2. Whether the **firmware/BMS repos are reachable** by Claude at all (this session only has
   `jonnolly/claudeRoutines`; GitHub scope is limited to it).
3. Whether a CLAUDE.md and a **runnable check** (build / unit test / static analysis / sim)
   exist on the work repos. Without a check, nothing unattended is safe.
4. Plan tier and whether usage limits are ever hit — decides if parallel/continuous agents
   are affordable at all.
5. Which non-code work he most wants offloaded (Jira triage, requirement↔code traceability,
   meeting notes → Confluence, test-plan drafting, email triage).
6. Where AI is explicitly *unwelcome* (music practice? counselling? journaling?).

## Operational findings

- **2026-11-19 — Atlassian connector is failing.** Call to `getAccessibleAtlassianResources`
  returned: the deprecated HTTP+SSE transport at `https://mcp.atlassian.com/v1/sse` is being
  phased out; clients must point at `https://mcp.atlassian.com/v2/mcp` and re-authorise.
  Until reconnected, Claude cannot read Jira or Confluence — the single highest-value data
  source for his current work. Reported in day 1 notification.
