# Profile — John Connolly

_Last updated: 2026-11-12. First build: inferred from connected accounts (Gmail, TickTick, GitHub), **not yet confirmed by John**. Items marked (?) are assumptions to verify._

## Work
- Developer at **New Electric** (newelectric.nl), embedded C on machine PLCs — battery packs, chargers, HVAC. Colleagues: Frank de Boer (lead, sets the workflow), Rogier van Rooijen (fellow dev), Shahbaz M. (invoices/admin).
- Domain: MRS CC27 hardware, CAN bus, firmware `.s19` images, bench testing on real machines, MISRA, Ceedling/Unity/CMock unit tests, `arm-none-eabi-gcc` 8.3.1.
- Self-hosted Forgejo at `git.newelectric.ovh`. 18 machine PLC repos.

## The big thing happening right now (started 31 Oct – 2 Nov 2026)
New Electric has just rolled out an entirely new dev environment and an **AI developer called "Alex"**:
- **DevDock** — one Ubuntu 26.04 Docker image (`ne-devdock`), identical on every PC. Standard dev PC is **Windows + Docker Desktop (WSL2) + VS Code**; code lives in a Windows folder (`C:\Code\projects`), built/tested inside the container. Known slow on mounted Windows folders.
- **nepkg** — in-house C package manager. No registry: a package is a git repo, a version is a git tag. `nepkg.json` + `nepkg.lock`. Commands: `install/configure/check/update/upgrade/revert/run test`.
- **Alex** = Claude Code with a name, a role and its own instruction repo **`NE_ALEX`**, imported by each repo's **`AGENTS.md`**. Has named **skills** (`new-package`, `release`, `upgrade-dependencies`, `rename-package`, `convert-plc-repo`) and scripts (`test.sh`, `repos.sh`, `elf-compare.sh`, `dependents.py`, `readme-examples.sh`).
- Alex's documented gate: it does nothing that **reaches the server, a machine or production** without John's explicit OK. So **John is the approver/bottleneck** on every push and release.
- Alex's six documented habits: start it in the repo; say the goal not the steps; say how far to go; answer its questions with a choice; interrupt and correct it; **read its summary**.
- Frank asked John and Rogier (2 Nov) to read both docs and write down questions/concerns — so the workflow is still being shaped and John has input into it.
- Pending migration pain: 11 PLCs pin different commits of the old shared `_ne_embedded_software_library`; 5 pin commits never merged anywhere; only 1 repo has a `nepkg.json` so far. A large, repetitive conversion job is coming.

## Side / personal projects
- **CanTraceSplitter** (GitHub, TeX+?) — matches TickTick project "✂Trace Trimmer". CAN trace splitting tool. Possible revenue line (?).
- **Gratitude_Journal** (GitHub, Python) — prompts for 3 gratitudes, saves to Google Drive. Has a matching TickTick project.
- SimpleSynthesizer (C#/WPF, 2023), renispace (C++, 2016) — dormant.

## Life / study
- Music is a major track: **first year at Zuyd** (conservatory), jazz trumpet + piano, theory homework, original music, recording ("Fingertips"), gigs ("Wake Up Gig", Ecstatic Dance Band, Key May duo with Kymé). Just moved / started school.
- Learning **Dutch** (TickTick vocabulary project).
- Deliberate personal-development practice: Goal Reviews, Career, Councilling, Gratitude Journal, Relationship, House.

## Tools & habits
- **TickTick** power user, GTD-shaped: paired "Work→Personal Inbox" / "Personal→Work Inbox" capture projects, "Admin Power Hours", "Someday/Reference", "Todo on the go", "At the piano", "Appointment Reminders". Uses both list and kanban views.
- **Obsidian** (TickTick project "♦Add to Obsidian" feeds it).
- Has a TickTick project **"🟥Claude questions"** (created 28 Sep 2026) used to stash things to ask Claude. Currently 1 item: a retirement-fund planning question.
- Reads **TLDR, TLDR Dev, TLDR AI** daily (arrive ~12:00–15:00 CET) and the **Claude Code newsletter**. So he already gets the headlines — tips must add *application*, not news.
- Runs Claude Code cloud sessions/routines (this one). Pays for Anthropic personally and forwards receipts to the company.
- Does a **morning email review** — this routine's tip rides along with it.

## How he wants this routine to behave
- One tip/day, tailored, highest-leverage-first. Must be something he is **not already doing**.
- Hard cap **15 min/day**. Shipping paid work beats polishing workflow.
- Interested in: multiple agents, assigned roles, agents working continuously.
- **He schedules his own follow-up work.** The routine suggests; it never creates tasks or routines for him.

## Known unknowns
See `questions.md`. Biggest: which advanced patterns he already uses, where his Claude hours actually go, what other routines he already runs, and whether he can change `NE_ALEX` himself.
