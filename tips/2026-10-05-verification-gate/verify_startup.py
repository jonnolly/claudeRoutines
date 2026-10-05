#!/usr/bin/env python3
"""
Stop-hook gate: Trace Trimmer must cold-start in under BUDGET seconds.

Wire this up as a `Stop` hook and Claude physically cannot end its turn while the
app starts too slowly -- it gets the failure text back and has to keep working.
This replaces the instruction you were writing by hand in the task description.

Two knobs to set:  BUDGET  and  ENTRY.
"""
import json
import os
import pathlib
import subprocess
import sys
import time

BUDGET = 1.0                                        # seconds
ENTRY = ["python3", "-c", "import trace_trimmer"]   # <-- your real cold-start command
RUNS = 3                                            # take the fastest, to beat noise

ROOT = pathlib.Path(os.environ.get("CLAUDE_PROJECT_DIR", ".")).resolve()
STAMP = ROOT / ".claude" / ".startup-ok"
SKIP_DIRS = {".venv", "venv", ".git", "__pycache__", "build", "dist"}

# Loop guard: if we already blocked once this turn, don't block again.
try:
    payload = json.load(sys.stdin)
except Exception:
    payload = {}
if payload.get("stop_hook_active"):
    sys.exit(0)


def sources_changed() -> bool:
    """Only spend time measuring if Python source moved since the last green run."""
    if not STAMP.exists():
        return True
    ref = STAMP.stat().st_mtime
    for p in ROOT.rglob("*.py"):
        if SKIP_DIRS & set(p.parts):
            continue
        try:
            if p.stat().st_mtime > ref:
                return True
        except OSError:
            continue
    return False


if not sources_changed():
    sys.exit(0)

timings = []
for _ in range(RUNS):
    started = time.perf_counter()
    proc = subprocess.run(ENTRY, cwd=ROOT, capture_output=True)
    timings.append(time.perf_counter() - started)
    if proc.returncode != 0:
        sys.stderr.write(
            "Startup gate ERROR: the cold-start command failed, so startup time could "
            "not be measured. Fix this before finishing:\n"
            + proc.stderr.decode(errors="replace")[:1500]
        )
        sys.exit(2)

best = min(timings)

if best > BUDGET:
    sys.stderr.write(
        f"Startup gate FAILED: cold start is {best:.2f}s, over the {BUDGET:.1f}s budget.\n"
        f"Profile it with:  python3 -X importtime -c 'import trace_trimmer'  2>&1 | sort -k2 -rn | head -25\n"
        "Then cut the dominant costs -- usually by deferring heavy imports (GUI toolkit, "
        "pandas, matplotlib) out of module scope and into the function that needs them.\n"
        "Do not finish until this passes. If you genuinely cannot reach the budget, say so "
        "explicitly and report the best time you achieved and what is blocking it.\n"
    )
    sys.exit(2)

STAMP.parent.mkdir(parents=True, exist_ok=True)
STAMP.touch()
print(f"Startup gate passed: {best:.2f}s (budget {BUDGET:.1f}s)")
