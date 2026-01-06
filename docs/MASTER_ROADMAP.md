---
document: "MASTER_ROADMAP"
version: "1.0.0"
status: "ACTIVE"
created: "2026-01-06"
updated: "2026-01-06"
owner: "Richie Suarez"
active_blueprint: null
---

# Ambiance — Master Roadmap

> **Document Status**: Living Document  
> **Last Updated**: 2026-01-06  
> **Owner**: Richie Suarez

---

## Strategic Vision

**North Star:** Build a universal cognitive prosthetic powered by an autonomous AI entity with persistent awareness across all life domains. Meta glasses provide the sensory layer that extends this awareness beyond digital into physical reality.

**Success Metric:** The AI entity makes autonomous decisions based on real-world observations that were never explicitly provided — it sees something, understands the implications, and acts appropriately.

---

## Phase 1: Foundation (Current)

**Goal**: Establish data pipeline from glasses to zeOS

| Task | Status | Notes |
|------|--------|-------|
| Acquire Meta Ray-Ban glasses | 🔲 | Demo scheduled 2026-01-06 |
| Test data export mechanisms | 🔲 | How to get audio/photos/video out of Meta ecosystem |
| Create S3 staging bucket | 🔲 | Landing zone for glasses outputs |
| Prototype voice note pipeline | 🔲 | Audio → S3 → Whisper transcription → zeOS journal |
| Test privacy controls | 🔲 | Geofence, pause, face blurring capabilities |

### Phase 1 Complete When:
- [ ] Glasses acquired and operational
- [ ] Basic data pipeline working (glasses → S3 → processing)
- [ ] Privacy boundaries understood and documented

---

## Phase 2: Meeting Mode MVP

**Goal**: Highest-value, lowest-risk use case

| Task | Status | Notes |
|------|--------|-------|
| Implement meeting detection | 🔲 | 3+ voices for 60+ seconds |
| Auto-transcription pipeline | 🔲 | Silent capture → Whisper processing |
| Action item extraction | 🔲 | AI Director processes transcripts |
| Session journal integration | 🔲 | Meeting notes feed into zeOS |

### Phase 2 Complete When:
- [ ] Meeting mode operational end-to-end
- [ ] Action items auto-extracted and surfaced
- [ ] Meeting context persists in zeOS memory

---

## Phase 3: Perception Layer Architecture

**Goal**: Formalize glasses as AI sensory organ

| Task | Status | Notes |
|------|--------|-------|
| Define Perception API | 🔲 | Standard format for glasses → zeOS |
| Build edge preprocessing | 🔲 | On-device redaction, compression |
| Implement perception bus | 🔲 | MQTT/WebSocket structured events |
| Create Perception Journal | 🔲 | Timestamped observations in zeOS |

---

## Phase 4: Autonomous Triggers

**Goal**: Real-world scenarios auto-initiate AI workflows

| Trigger Type | Status | Notes |
|--------------|--------|-------|
| Location-based context loading | 🔲 | Enter known location → load project |
| Meeting mode auto-start | 🔲 | Voice detection triggers |
| Technical reconnaissance | 🔲 | "Analyze this" command |
| Anomaly detection | 🔲 | Grok flags inconsistencies |

---

## Phase 5: Recursive Capability Discovery

**Goal**: AI learns new capabilities from physical world input

| Task | Status | Notes |
|------|--------|-------|
| Classification engine | 🔲 | Categorize observations against known domains |
| Gap analysis workflow | 🔲 | Detect when workers cannot handle domain |
| Capability spawning | 🔲 | Director consensus → new worker type |
| Integration to zeOS registry | 🔲 | New capabilities registered |

---

## Phase 6: Full Autonomous Loop

**Goal**: AI independently decides when to observe, analyze, act

| Task | Status | Notes |
|------|--------|-------|
| Predictive observation | 🔲 | AI requests observations before operator knows needed |
| Cross-Director perception routing | 🔲 | Right Director analyzes right input |
| Federated perception | 🔲 | Multiple operators feed shared intelligence |

---

## Research & Integration Points

| External Solution | Status | Integration Point |
|-------------------|--------|-------------------|
| Deepgram (transcription) | 🔲 Research | Alternative to Whisper |
| AssemblyAI | 🔲 Research | Real-time transcription |
| OpenAI Vision | 🔲 Research | Image understanding |
| Privacy-preserving edge AI | 🔲 Research | On-device processing |

---

## Dependencies

- **Outpost**: Fleet dispatch for worker tasks
- **AI Boardroom**: Director-level orchestration
- **Blueprint**: Task planning and execution
- **zeOS Core**: Memory persistence and context injection

---

*"The glasses are not a peripheral — they are a sensory organ."*
*— Outpost Fleet Consensus, 2026-01-06*
