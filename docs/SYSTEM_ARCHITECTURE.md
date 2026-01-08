---
document: "SYSTEM_ARCHITECTURE"
version: "2.0.0"
status: "DRAFT"
created: "2026-01-06"
updated: "2026-01-07"
owner: "Technical Operations"
---

# Ambiance — System Architecture

> **Document Status**: Living Document  
> **Last Updated**: 2026-01-07  
> **Owner**: Technical Operations

---

## Overview

Ambiance is the mobile sensory layer for the autonomous AI entity. It utilizes an **iOS application** combined with **AirPods** to provide a "Voice-to-Action" cognitive prosthetic. It processes verbal commands and sensor data, routes them to the zeOS orchestration layer, and executes tasks via CLI agents on the Outpost infrastructure.

---

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    PHYSICAL WORLD / OPERATOR                    │
│  ┌──────────────┐    ┌──────────────┐                           │
│  │   iPhone     │    │   AirPods    │                           │
│  │ (Sensors/UI) │ ←→ │ (Mic/Audio)  │                           │
│  └──────┬───────┘    └──────────────┘                           │
└─────────┼───────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────┐
│               CLIENT LAYER (iOS App)                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │ Action      │  │ Audio       │  │ Context     │             │
│  │ Button      │  │ Manager     │  │ Manager     │             │
│  │ (Trigger)   │  │ (Stream)    │  │ (GPS/Health)│             │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘             │
└─────────┼───────────────────────────────────────────────────────┘
          │ HTTPS / WebSocket
          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    GATEWAY LAYER (Cloud API)                    │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ API Gateway / Load Balancer                                 ││
│  │ Auth (Zero Echelon ID)                                      ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────┼───────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    PROCESSING LAYER                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │ Whisper     │  │ Intent      │  │ Command     │             │
│  │ Transcribe  │  │ Classifier  │  │ Parser      │             │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘             │
└─────────┼───────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    zeOS ORCHESTRATION                           │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ AI Boardroom (Directors)                                    ││
│  │ zeOS Memory (Perception Journal)                            ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────┼───────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    EXECUTION LAYER (Outpost)                    │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │ CLI Agent   │  │ CLI Agent   │  │ CLI Agent   │             │
│  │ (Claude)    │  │ (Gemini)    │  │ (Bash)      │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
└─────────────────────────────────────────────────────────────────┘
```

---

## Infrastructure

| Resource | Value |
|----------|-------|
| Client Platform | iOS 17+ (SwiftUI) |
| Backend Hosting | AWS Lambda / API Gateway |
| Transcription | OpenAI Whisper API |
| Orchestration | zeOS (AI Boardroom) |
| Execution | Outpost (EC2/SSM) |

---

## Component Details

### iOS Client

**Purpose:** Primary interface for the Operator.
**Key Features:**
- **Push-to-Talk:** Action Button integration for instant command.
- **Background Mode:** Continuous listening/transcription (Meeting Mode).
- **Visual Feedback:** Cards for complex results (charts, code snippets).
- **Haptic Feedback:** Confirmation of command receipt/execution.

### Gateway Layer

**Purpose:** Secure entry point for voice/data streams.
**Stack:** AWS API Gateway + Lambda.

### Processing Layer

**Purpose:** Convert audio to structured intent.
**Workflow:**
1. **Receive** audio blob.
2. **Transcribe** via Whisper.
3. **Parse** text for zeOS commands (e.g., "!delegate", "!project").
4. **Inject** context (Location, Time, previous turns).

### zeOS Orchestration

**Purpose:** Decide HOW to execute the command.
- **Simple Command:** Direct CLI execution.
- **Complex Query:** Route to Boardroom Directors.
- **Strategic Decision:** Convene Directors for EDB.

---

## Privacy Architecture

### Mobile Sovereignty

| Layer | Protection |
|-------|------------|
| L1: On-Device | Local keyword detection (optional), Mute switch |
| L2: Transmission | E2E Encryption (TLS 1.3) |
| L3: Cloud | Ephemeral processing (transcripts stored, audio purged) |
| L4: Operator | Full audit log of all voice commands |

---

## Integration Points

| System | Integration |
|--------|-------------|
| zeOS Core | Memory persistence, Shell Protocol commands |
| Outpost | Worker fleet dispatch for CLI execution |
| AI Boardroom | High-level reasoning for vague queries |
| iOS HealthKit | Wellness context injection |

---

## Technology Stack (Planned)

| Component | Technology |
|-----------|------------|
| Mobile App | Swift / SwiftUI |
| API | Python (FastAPI) or Node.js |
| Database | DynamoDB (User settings/Logs) |
| Storage | S3 (Temp Audio Staging) |
| AI Models | GPT-4o / Claude 3.5 Sonnet |

---

*Last verified: 2026-01-07*
*Architecture Pivot: Mobile-First*