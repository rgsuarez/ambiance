---
type: session-journal
project: ambiance
status: complete
started: 2026-01-07T06:45:00Z
ended: 2026-01-08T07:55:00Z
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

## Work Since Pivot Checkpoint

### Blueprint Generation & Activation
- **Consultation:** Dispatched query to 5 Outpost agents.
  - **Consensus:** Approved "Backend-First (Linux)" strategy. Mac only for iOS build.
  - **Architecture:** Validated FastAPI + WebSockets for low-latency audio stream.
- **Blueprint Generated:** `ESTABLISH_AMBIANCE_MOBILE_FOUNDATION.md`
  - **Tiers:** 3 (Audio Pipeline, Gateway, zeOS Integration).
  - **Tasks:** 9 atomic tasks.
  - **Validation:** Includes CLI Test Client for Linux-only E2E validation.
- **Activation:** Set as active blueprint in `MASTER_ROADMAP.md`.

## Work Since Generation Checkpoint

### Tier 0: Foundation
- **T0.1 FastAPI WebSocket Server:** Implemented bidirectional WebSocket gateway with JSON/Binary support.
- **T0.2 Audio Stream Handler:** Implemented ring buffer for PCM audio chunks.
- **Tests:** Added `tests/gateway/` covering connection lifecycle and audio buffering.

### Tier 1: Voice Processing (Partial)
- **T1.1 Whisper Service:** Implemented `WhisperService` with `openai-whisper` integration.
- **T1.2 Voice Activity Detection:** Implemented `VoiceActivityDetector` using `webrtcvad` with stateful frame buffering.
- **Tests:** Added `tests/voice/` with mocked model loading and VAD logic verification.
- **Dependencies:** Installed `fastapi`, `uvicorn`, `websockets`, `numpy`, `openai-whisper`, `webrtcvad`.

### Tier 2: Orchestration
- **T2.1 Boardroom Client Adapter:** Implemented `BoardroomClient` with `httpx` for async communication.
- **T2.2 Response Synthesizer:** Implemented `ResponseSynthesizer` to clean markdown for TTS/Voice output.
- **Tests:** Verified client and synthesizer logic.

### Tier 3: Integration
- **T3.1 Pipeline Orchestrator:** Implemented `AmbiancePipeline` linking VAD -> Whisper -> Boardroom -> Synthesizer. Integrated into `server.py` WebSocket loop.
- **T3.2 iOS Client Protocol:** Documented WebSocket protocol in `docs/ios_protocol.md` and generated JSON schema.
- **Architecture Refactor:** Moved `protocol.py` to root `src/ambiance/protocol.py` to resolve circular imports.

### Current Focus
- **BLUEPRINT COMPLETE.**
- Backend foundation is established and tested (on Linux).
- Ready for iOS Client development (Phase 2).

