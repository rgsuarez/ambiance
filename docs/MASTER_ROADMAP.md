---
document: "MASTER_ROADMAP"
version: "2.0.0"
status: "ACTIVE"
created: "2026-01-06"
updated: "2026-01-07"
owner: "Richie Suarez"
active_blueprint: null
---

# Ambiance — Master Roadmap

> **Document Status**: Living Document  
> **Last Updated**: 2026-01-07  
> **Owner**: Richie Suarez

---

## Strategic Vision

**North Star:** Build a universal cognitive prosthetic powered by an autonomous AI entity with persistent awareness across all life domains. **iOS devices and AirPods** provide the sensory layer that extends this awareness beyond digital into physical reality.

**Success Metric:** The AI entity makes autonomous decisions based on voice commands and context — it hears a request, understands the implications, and acts appropriately via CLI agents.

---

## Phase 1: Foundation (Current)

**Goal**: Establish iOS Voice-to-Action Pipeline

| Task | Status | Notes |
|------|--------|-------|
| Scaffold iOS App (SwiftUI) | 🔲 | Basic shell with push-to-talk UI |
| Implement Audio Capture | 🔲 | Record audio from AirPods/Mic |
| Build API Gateway | 🔲 | Endpoint to receive audio/text |
| Connect to zeOS | 🔲 | Route inputs to Boardroom/Outpost |
| Action Button Integration | 🔲 | Map iPhone Action Button to "Listen" |

### Phase 1 Complete When:
- [ ] iOS App deployed to TestFlight
- [ ] Audio successfully streaming to API
- [ ] CLI agents executing commands from voice input

---

## Phase 2: Orchestration & Feedback

**Goal**: Intelligent routing and bidirectional communication

| Task | Status | Notes |
|------|--------|-------|
| Director Routing | 🔲 | Classify intent -> Route to Director |
| Text-to-Speech Output | 🔲 | AI speaks back via AirPods |
| Visual Cards | 🔲 | App displays complex outputs (code/charts) |
| Meeting Mode | 🔲 | Long-form background recording/transcription |

### Phase 2 Complete When:
- [ ] Full conversational loop (Talk -> Action -> Speak Back)
- [ ] Meeting context auto-persisted to zeOS
- [ ] Complex results displayed on phone screen

---

## Phase 3: Context Awareness

**Goal**: Leverage iOS sensors for rich context

| Task | Status | Notes |
|------|--------|-------|
| Location Context | 🔲 | "I'm at home" vs "I'm at office" behavior |
| Health Integration | 🔲 | HealthKit data feeding wellness Director |
| Photo/Camera Input | 🔲 | "Look at this" visual analysis |
| Background Refresh | 🔲 | Periodic state sync |

---

## Phase 4: Recursive Capability Discovery

**Goal**: AI learns new capabilities from physical world input

| Task | Status | Notes |
|------|--------|-------|
| Classification engine | 🔲 | Categorize observations against known domains |
| Gap analysis workflow | 🔲 | Detect when workers cannot handle domain |
| Capability spawning | 🔲 | Director consensus → new worker type |
| Integration to zeOS registry | 🔲 | New capabilities registered |

---

## Phase 5: Full Autonomous Loop

**Goal**: AI independently decides when to observe, analyze, act

| Task | Status | Notes |
|------|--------|-------|
| Predictive suggestion | 🔲 | AI speaks proactive suggestion via AirPods |
| Federated perception | 🔲 | Multiple inputs feed shared intelligence |

---

## Research & Integration Points

| External Solution | Status | Integration Point |
|-------------------|--------|-------------------|
| OpenAI Whisper | 🔲 Research | Transcription |
| Apple Speech | 🔲 Research | On-device transcription fallback |
| FastAPI | 🔲 Research | Backend API |
| zeOS Shell Protocol | 🔲 Standard | Command format |

---

## Dependencies

- **Outpost**: Fleet dispatch for worker tasks
- **AI Boardroom**: Director-level orchestration
- **Blueprint**: Task planning and execution
- **zeOS Core**: Memory persistence and context injection

---

*"The phone is the edge processor; AirPods are the interface."*
*— Ambiance Pivot, 2026-01-07*