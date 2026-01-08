---
type: session-journal
project: ambiance
status: active
started: 2026-01-07T06:45:00Z
ended: null
---

## Work Since Last Save

### Strategic Pivot: Ambiance Mobile
- **Decision:** Shifted North Star from Meta Ray-Ban glasses to **iOS + AirPods** architecture.
- **Rationale:**
  - Removed "walled garden" risk (Meta SDK limitations).
  - Leveraging existing hardware (iPhone/AirPods/MacBook Air).
  - Zero latency (direct API access vs. Meta Cloud hop).
  - Superior sensor access (HealthKit, Location, Files).
  - Action Button integration for instant "Push-to-Talk".

### Artifacts Updated
- **docs/MASTER_ROADMAP.md:** Complete rewrite. Removed "Acquire Glasses". Added "Scaffold iOS App".
- **docs/SYSTEM_ARCHITECTURE.md:** Updated diagram to "Voice-to-Action" pipeline. Replaced Edge/Meta layers with iOS Client/Gateway.

### Constraints & Notes
- **Hardware:** MacBook Air confirmed sufficient for iOS dev.
- **Privacy:** Shifted to on-device processing + E2E encryption.
- **Integration:** zeOS Core integration remains standard (API Gateway -> Boardroom).

### Current Focus
- Initializing Phase 1: iOS App Scaffolding.
