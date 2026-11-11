# Inbox triage routine: state between runs

Each run reads this file first, applies pending answers, then updates it.

## Checklist page
- Artifact: https://claude.ai/artifact/3LwrpYz3yzr3T2zB5QmG42 (db collections: `checks` = ticked items, `answers` = backlog answers).
- Next run: read `checks`; for ticked automated items -> archive; for ticked items from people -> mark read (keep in inbox).

## Pending backlog question
- id: `q1-celso-can-sensors` (asked 2026-11-11)
- Thread: "CAN BUS sensors" from Celso, 2025-09-10, thread id 1993278858b2361a
- Options: archive | read | keep

## Kept on purpose (don't re-archive)
- TLDR Dev 2026-10-27 (thread 1a17d295ed700b76): Claude Code code review + ESP32-S3 SIMD.

## Run log
- 2026-11-11: first run. Archived 1,305 automated threads >14d (834 Jenkins, 192 calendar, 108 Zoho, 54 Odos, 49 Nmbrs, 22 NS, 21 Atlassian, misc) + TLDR AI 2026-11-03. Skipped (kept): 19d06a243df0e63b, 19b9da24eadb0e2e (Suncar support convos), 1934e268b10af7a9 (company party invite), 188567031778b34e, 180feb49360d834d (self-forwarded payslips).
