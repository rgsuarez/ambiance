# Session Journals

This directory contains session journals for Ambiance.

**IMPORTANT:** All session journals for this app are stored HERE, not in zeOS Core.

## Format

Journals follow the zeOS session journaling standard:
- Filename: `YYYY-MM-DD-NNN.md` (e.g., `2026-01-06-001.md`)
- Status: CHECKPOINT or COMPLETE
- Required fields: session_id, date, status, agent, next_action_primer

## Usage

- `!checkpoint` — Save progress mid-session (writes HERE)
- `!end` — Generate final journal and commit (writes HERE)

See zeOS Shell Protocol for full documentation.

---

## Project Context

Ambiance is the sensory layer for the autonomous AI entity. Session journals capture:
- Glasses integration progress
- Perception layer development
- Privacy architecture decisions
- Autonomous trigger implementations

---

*zeOS Venture Factory - Ambiance*
