---
document: "SYSTEM_ARCHITECTURE"
version: "1.0.0"
status: "DRAFT"
created: "2026-01-06"
updated: "2026-01-06"
owner: "Technical Operations"
---

# Ambiance — System Architecture

> **Document Status**: Living Document  
> **Last Updated**: 2026-01-06  
> **Owner**: Technical Operations

---

## Overview

Ambiance is the sensory layer that transforms the autonomous AI entity from purely digital to cyber-physical. It integrates Meta Ray-Ban glasses as sensory input, processes observations through a Perception Layer, and feeds structured events into the zeOS Director-Worker orchestration loop.

---

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    PHYSICAL WORLD                               │
│  ┌──────────────┐                                               │
│  │ Meta Ray-Ban │ ← Camera, Microphone, GPS, Accelerometer      │
│  └──────┬───────┘                                               │
└─────────┼───────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────┐
│               PERCEPTION LAYER (Edge Processing)                │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │ Vision      │  │ Audio       │  │ Context     │             │
│  │ Processor   │  │ Processor   │  │ Synthesizer │             │
│  │ (frame→text)│  │ (speech→text│  │ (multimodal)│             │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘             │
│         │ PII Redaction  │ Scrubbing      │ Compression        │
└─────────┼────────────────┼────────────────┼─────────────────────┘
          │                │                │
          ▼                ▼                ▼
┌─────────────────────────────────────────────────────────────────┐
│                    STAGING LAYER (S3)                           │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ s3://ambiance-staging-535471339422/                         ││
│  │   ├── audio/                                                ││
│  │   ├── images/                                               ││
│  │   └── events/                                               ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    PROCESSING LAYER                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │ Whisper     │  │ Vision      │  │ Event       │             │
│  │ Transcribe  │  │ Analysis    │  │ Classifier  │             │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘             │
└─────────┼────────────────┼────────────────┼─────────────────────┘
          │                │                │
          ▼                ▼                ▼
┌─────────────────────────────────────────────────────────────────┐
│                    zeOS MEMORY PERSISTENCE                      │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ Perception Journal: timestamped observations, entities,     ││
│  │ locations, conversations, environmental state               ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    DIRECTOR COUNCIL (AI Boardroom)              │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐           │
│  │ Claude   │ │ Gemini   │ │ ChatGPT  │ │ Grok     │           │
│  │ Architect│ │ Strategist│ │ Creative │ │Contrarian│           │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘           │
└─────────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    WORKER EXECUTION (Outpost)                   │
│  Tasks spawned based on physical-world triggers                 │
└─────────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    OUTPUT CHANNELS                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │ Glasses HUD │  │ Audio       │  │ Phone/Watch │             │
│  │ (visual)    │  │ (earpiece)  │  │ (haptic)    │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Infrastructure

| Resource | Value |
|----------|-------|
| Repository | https://github.com/rgsuarez/ambiance |
| AWS Account | 535471339422 (pending) |
| AWS Region | us-east-1 |
| Staging Bucket | TBD: ambiance-staging-535471339422 |

---

## Component Details

### Perception Layer

**Purpose:** Convert raw sensor data to structured observations before reaching Directors.

**Key Design Decisions:**
- Edge-first processing (on-device or phone app)
- PII redaction before anything leaves device
- Structured events, not raw streams
- Minimal bandwidth (90% reduction target)

**Technologies (Research):**
- YOLO for object detection
- Whisper for speech-to-text
- CLIP/Jina for embeddings

### Staging Layer

**Purpose:** Landing zone for processed glasses outputs.

**S3 Structure:**
```
s3://ambiance-staging-535471339422/
├── audio/{date}/{timestamp}.mp3
├── transcripts/{date}/{timestamp}.json
├── images/{date}/{timestamp}.jpg
├── events/{date}/{timestamp}.json
└── metadata/{date}/manifest.json
```

### Processing Layer

**Purpose:** Transform staged artifacts into actionable intelligence.

**Lambda Functions (Planned):**
- `ambiance-transcribe`: Audio → text via Whisper
- `ambiance-vision`: Image analysis via OpenAI Vision
- `ambiance-classify`: Event classification and trigger detection

### Output Channels

**HUD Overlays:** Director-generated insights surface via glasses display  
**Audio Feedback:** Critical alerts via earpiece  
**Haptic:** Phone/watch notifications for non-visual cues

---

## Privacy Architecture

### Layered Protection Model

| Layer | Protection |
|-------|------------|
| L1: Real-Time | Physical kill switch, "pause capture" voice command |
| L2: Contextual | Geofence blacklist, time-based rules |
| L3: Data Governance | Auto-purge TTLs, E2E encryption |
| L4: Legal | Jurisdiction-aware auto-disable |

### Data Flow Security

1. **Edge scrubbing:** Face blur, PII redaction on-device
2. **Minimal transmission:** Only structured events leave device by default
3. **Encrypted storage:** S3 server-side encryption + client-side for sensitive
4. **Audit trail:** Immutable log of all data access

---

## Integration Points

| System | Integration |
|--------|-------------|
| zeOS Core | Memory persistence, context injection |
| Outpost | Worker fleet dispatch |
| AI Boardroom | Director-level orchestration |
| Blueprint | Task planning and execution |

---

## Technology Stack (Planned)

| Component | Technology |
|-----------|------------|
| Edge Processing | Meta SDK + custom bridge |
| Staging | S3 |
| Transcription | Whisper API or Deepgram |
| Vision | OpenAI Vision API |
| Event Bus | EventBridge or SNS |
| Compute | Lambda |
| Memory | zeOS GitHub persistence |

---

*Last verified: 2026-01-06*
*Architecture based on Outpost Fleet synthesis*
