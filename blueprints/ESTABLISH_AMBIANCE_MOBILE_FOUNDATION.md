═══════════════════════════════════════════════════════════════
🚀 OUTPOST UNIFIED DISPATCH v1.5.0
═══════════════════════════════════════════════════════════════
Batch ID:   20260108-074811-batch-yb4i
Repo:       blueprint
Task:       Generate a Blueprint specification for: ESTABLISH_AMBIANCE_MOBILE_FOUNDATION_BACKEND_FIRST. Context:...
Executors:  claude
Context:    standard
Isolation:  ENABLED (each agent gets own workspace)
═══════════════════════════════════════════════════════════════

🔄 Syncing dispatch scripts from GitHub...
   Scripts synced from GitHub

📦 Pre-flight: Updating shared cache...
   Fetching latest...
HEAD is now at 979699b docs(journal): session 022 - v1.4.0 release
   Cache ready: 979699b4268d6594b7810be7a1576d4de1a43d6d

📋 Building context injection (level: standard)...
   ✅ Injection ID: INJ-20260108-074812-d6tf2b
   Tokens: ~575
   Sections: soul, profile, journal

📤 Dispatching to claude...

⏳ Waiting for all agents...
🚀 Claude Code dispatch starting...
Run ID: 20260108-074812-zrqdl1
Model: claude-opus-4-5-20251101
Repo: blueprint
Task: <zeos_context version="1.0" injection_id="INJ-20260108-074812-d6tf2b">

## SOUL

Project: blueprint
Purpose: See project documentation

## PROFILE

Operator: Richie Suarez
Style: Direct, military precision, BLUF

Standards:
- GitOps discipline mandatory
- Systems over tasks
- Production-grade code

## JOURNAL

# Session 015 - Fleet Consultation for Recursive Deepening
**Date:** 2026-01-07
**Agent:** Claude Opus 4.5
**Status:** CHECKPOINT - Blueprint Generated, Ready for Execution

## Session Objective
Design and spec the v1.4.0 Recursive Deepening feature with multi-agent fleet consultation.

## Session Accomplishments

### Fleet Consultation Completed
Dispatched query to 5 Outpost agents for architectural input:
- **Claude** (Architect): Weighted priority with ASK_USER threshold
- **Codex** (Code Gen): Numeric scoring, contract stability rule
- **Gemini** (Strategist): Mandates > Policy > Heuristics
- **Grok** (Contrarian): EXISTS & WORKS as veto, pattern-matched context
- **Aider** (Coder): Attempted implementation (useful reference code)

**Command ID:** `f107f698-3d44-4dba-8f2a-a11a7d23eca7`
**Output:** `s3://outpost-outputs/blueprint-fleet-consultation/`

### Fleet Consensus Synthesized

| Question | Consensus |
|----------|-----------|
| Rule Precedence | Weighted scoring with veto rules + confidence threshold |
| Codebase Context | Tiered injection (L0-L3) with 8K token cap |
| Output Format | Single file with `_layer`, `_parent`, `_rule_trace` |
| Doc-First Pass | Layer -1 generates `doc_manifest.yaml` |
| Additional Rules | security_audit, test_parity, schema_drift, testable?, reversible? |

### Official Blueprint Generated
**File:** `blueprints/v1.4.0-recursive-deepening.yaml`

**Structure:**
- **T0:** Foundation - Models & Schema (3 tasks)
- **T1:** Context Engine - Codebase Analysis (3 tasks)
- **T2:** Rule Engine - Evaluation System (4 tasks)
- **T3:** Doc Plan - Layer -1 Implementation (3 tasks)
- **T4:** Recursive Decomposer - Core Algorithm (4 tasks)
- **T5:** CLI & Output - User Interface (4 tasks)
- **T6:** Additional Rules - Fleet Recommendations (5 tasks)
- **T7:** Documentation & Testing - Final Polish (5 tasks)

**Total:** 7 Tiers, 27 Tasks, ~45 Sessions

### Critical Path
```
T0.1 -> T2.1 -> T2.4 -> T4.2 -> T5.3 -> T7.4
```

</zeos_context>

<task>
Generate a Blueprint specification for: ESTABLISH_AMBIANCE_MOBILE_FOUNDATION_BACKEND_FIRST. Context: Pivot from Meta Glasses to iOS/AirPods. Strategy: Backend-first validation on Linux. Architecture: iOS Client -> FastAPI Gateway (WebSockets) -> zeOS Boardroom -> Outpost CLI Agents. Stack: Python FastAPI, WebSockets, OpenAI Whisper. Constraint: Depth 2 (limit task granularity).. Keep task count between 5-10 tasks. Read docs/BLUEPRINT_SPEC.md for the exact format. CRITICAL: Include the BLUEPRINT METADATA comment block after the header. Output only the complete markdown document.
</task>
📦 Using pre-warmed cache
📂 Creating isolated workspace...
Workspace SHA: 979699b4268d6594b7810be7a1576d4de1a43d6d
🤖 Running Claude Code (Opus 4.5)...
Now I'll create the Blueprint specification for the Ambiance Mobile Foundation with Backend-First strategy.

```markdown
# Ambiance Mobile Foundation — Blueprint Specification

> **Document Status**: Active
> **Last Updated**: 2026-01-08
> **Owner**: Richie Suarez

<!-- BLUEPRINT METADATA (DO NOT REMOVE) -->
<!-- _blueprint_version: 2.0.1 -->
<!-- _generated_at: 2026-01-08T07:48:12Z -->
<!-- _generator: outpost.claude-opus -->
<!-- END METADATA -->

---

## Strategic Vision

Pivot Ambiance from Meta Glasses to iOS/AirPods platform. Backend-first validation strategy enables core orchestration development on Linux before iOS client integration. Architecture follows: **iOS Client → FastAPI Gateway (WebSockets) → zeOS Boardroom → Outpost CLI Agents**.

Key pivot rationale:
- AirPods ubiquity vs Meta Glasses early-adopter friction
- iOS ecosystem maturity for voice interfaces
- Backend-first de-risks mobile development timeline

---

## Success Metrics

| Metric | Target | Validation |
|--------|--------|------------|
| WebSocket latency | < 50ms p95 | Load test with k6 |
| Whisper transcription accuracy | > 95% WER | Test corpus evaluation |
| End-to-end voice command | < 2s response | Integration test |
| Linux backend fully functional | 100% features testable | pytest coverage |

---

## Execution Configuration

```yaml
execution:
  shell: bash
  shell_flags: ["-e", "-o", "pipefail"]
  max_parallel_tasks: 2
  
  preflight_checks:
    - command: "python3 --version | grep -E '3\\.(11|12)'"
      expected_exit_code: 0
      error_message: "Python 3.11+ required"
    - command: "which uvicorn"
      expected_exit_code: 0
      error_message: "uvicorn not installed"
      
  secret_resolution:
    on_missing: abort
    sources:
      - type: env
        prefix: ""
      - type: file
        path: ".env"
```

---

## Tier 0: Foundation — FastAPI Gateway

### T0.1: FastAPI WebSocket Server

```yaml
task_id: T0.1
name: "FastAPI WebSocket Server"
status: complete
dependencies: []

interface:
  input: "Project requirements and architecture spec"
  output: "Running FastAPI server with WebSocket endpoint"

input_bindings: {}

output:
  location: file
  path: "/tmp/blueprint/${task_id}/output.json"
  ports:
    server_module:
      type: file_path
    api_schema:
      type: json

required_capabilities:
  - python3.11
  - fastapi
  - uvicorn

acceptance_criteria:
  - "WebSocket endpoint at /ws accepts connections"
  - "Health check endpoint at /health returns 200"
  - "Structured message protocol defined (JSON schema)"
  - "Connection lifecycle: open, message, close, error"

verification:
  smoke:
    command: "python -c 'from ambiance.gateway import app; print(\"OK\")'"
    timeout: PT10S
  unit:
    command: "pytest tests/gateway/ -v --tb=short"
    timeout: PT2M

rollback: "git checkout HEAD -- src/ambiance/gateway/"

files_to_create:
  - src/ambiance/gateway/__init__.py
  - src/ambiance/gateway/server.py
  - src/ambiance/gateway/protocol.py
  - tests/gateway/test_websocket.py

notes: "Use FastAPI native WebSocket support. Message protocol: {type, payload, timestamp, correlation_id}"
```

### T0.2: Audio Stream Handler

```yaml
task_id: T0.2
name: "Audio Stream Handler"
status: complete
dependencies: [T0.1]

interface:
  input: "WebSocket connection and audio chunks"
  output: "Buffered audio ready for transcription"

input_bindings:
  server:
    source: T0.1
    output_port: server_module
    transfer: file
    required: true

output:
  location: file
  path: "/tmp/blueprint/${task_id}/output.json"
  ports:
    audio_handler:
      type: file_path
    buffer_config:
      type: json

required_capabilities:
  - python3.11
  - numpy

acceptance_criteria:
  - "Accepts chunked audio over WebSocket"
  - "Buffers audio with configurable window (default 3s)"
  - "Handles backpressure gracefully"
  - "Supports PCM 16-bit 16kHz mono format"

verification:
  smoke:
    command: "python -c 'from ambiance.gateway.audio import AudioBuffer; print(\"OK\")'"
    timeout: PT10S
  unit:
    command: "pytest tests/gateway/test_audio.py -v"
    timeout: PT2M

rollback: "git checkout HEAD -- src/ambiance/gateway/audio.py"

files_to_create:
  - src/ambiance/gateway/audio.py
  - tests/gateway/test_audio.py

notes: "Use ring buffer pattern. Chunk size aligned with Whisper expectations."
```

---

## Tier 1: Voice Processing — Whisper Integration

### T1.1: Whisper Transcription Service

```yaml
task_id: T1.1
name: "Whisper Transcription Service"
status: complete
dependencies: [T0.2]

interface:
  input: "Audio buffer (PCM 16-bit 16kHz)"
  output: "Transcribed text with confidence and timing"

input_bindings:
  audio_handler:
    source: T0.2
    output_port: audio_handler
    transfer: file
    required: true

output:
  location: file
  path: "/tmp/blueprint/${task_id}/output.json"
  ports:
    transcription_service:
      type: file_path
    model_config:
      type: json

required_capabilities:
  - python3.11
  - openai-whisper

acceptance_criteria:
  - "Integrates OpenAI Whisper (local or API)"
  - "Returns transcript with word-level timestamps"
  - "Configurable model size (tiny/base/small)"
  - "Async processing with timeout handling"

verification:
  smoke:
    command: "python -c 'from ambiance.voice.whisper import WhisperService; print(\"OK\")'"
    timeout: PT10S
  unit:
    command: "pytest tests/voice/test_whisper.py -v"
    timeout: PT3M

rollback: "git checkout HEAD -- src/ambiance/voice/"

files_to_create:
  - src/ambiance/voice/__init__.py
  - src/ambiance/voice/whisper.py
  - tests/voice/test_whisper.py

notes: "Start with 'base' model for balance of speed/accuracy. Support both local and API modes."
```

### T1.2: Voice Activity Detection

```yaml
task_id: T1.2
name: "Voice Activity Detection"
status: complete
dependencies: [T0.2]

interface:
  input: "Raw audio stream"
  output: "Speech segments with start/end timestamps"

input_bindings:
  audio_handler:
    source: T0.2
    output_port: audio_handler
    transfer: file
    required: true

output:
  location: file
  path: "/tmp/blueprint/${task_id}/output.json"
  ports:
    vad_module:
      type: file_path

required_capabilities:
  - python3.11
  - webrtcvad

acceptance_criteria:
  - "Detects speech onset and offset"
  - "Configurable sensitivity (0-3)"
  - "Filters background noise"
  - "Returns speech segments for transcription"

verification:
  smoke:
    command: "python -c 'from ambiance.voice.vad import VoiceActivityDetector; print(\"OK\")'"
    timeout: PT10S
  unit:
    command: "pytest tests/voice/test_vad.py -v"
    timeout: PT2M

rollback: "git checkout HEAD -- src/ambiance/voice/vad.py"

files_to_create:
  - src/ambiance/voice/vad.py
  - tests/voice/test_vad.py

notes: "Use webrtcvad for lightweight VAD. Mode 3 (most aggressive) for noisy environments."
```

---

## Tier 2: Orchestration — zeOS Boardroom Bridge

### T2.1: Boardroom Client Adapter

```yaml
task_id: T2.1
name: "Boardroom Client Adapter"
status: complete
dependencies: [T1.1]

interface:
  input: "Transcribed user command"
  output: "Boardroom session with command dispatch"

input_bindings:
  transcription:
    source: T1.1
    output_port: transcription_service
    transfer: file
    required: true

output:
  location: file
  path: "/tmp/blueprint/${task_id}/output.json"
  ports:
    boardroom_client:
      type: file_path
    session_manager:
      type: file_path

required_capabilities:
  - python3.11

acceptance_criteria:
  - "Establishes session with zeOS Boardroom"
  - "Translates voice commands to Boardroom format"
  - "Maintains conversation context"
  - "Handles Boardroom responses async"

verification:
  smoke:
    command: "python -c 'from ambiance.orchestration.boardroom import BoardroomClient; print(\"OK\")'"
    timeout: PT10S
  unit:
    command: "pytest tests/orchestration/test_boardroom.py -v"
    timeout: PT2M

rollback: "git checkout HEAD -- src/ambiance/orchestration/"

files_to_create:
  - src/ambiance/orchestration/__init__.py
  - src/ambiance/orchestration/boardroom.py
  - tests/orchestration/test_boardroom.py

notes: "Boardroom interface via existing zeOS SDK. Session persistence for multi-turn conversations."
```

### T2.2: Response Synthesizer

```yaml
task_id: T2.2
name: "Response Synthesizer"
status: complete
dependencies: [T2.1]

interface:
  input: "Boardroom agent response"
  output: "Formatted response for client delivery"

input_bindings:
  boardroom:
    source: T2.1
    output_port: boardroom_client
    transfer: file
    required: true

output:
  location: file
  path: "/tmp/blueprint/${task_id}/output.json"
  ports:
    synthesizer:
      type: file_path

required_capabilities:
  - python3.11

acceptance_criteria:
  - "Formats Boardroom responses for voice output"
  - "Handles structured data (lists, code) gracefully"
  - "Supports response streaming"
  - "Manages response queue for async delivery"

verification:
  smoke:
    command: "python -c 'from ambiance.orchestration.synthesizer import ResponseSynthesizer; print(\"OK\")'"
    timeout: PT10S
  unit:
    command: "pytest tests/orchestration/test_synthesizer.py -v"
    timeout: PT2M

rollback: "git checkout HEAD -- src/ambiance/orchestration/synthesizer.py"

files_to_create:
  - src/ambiance/orchestration/synthesizer.py
  - tests/orchestration/test_synthesizer.py

notes: "Future: integrate TTS. Current scope: text response formatting only."
```

---

## Tier 3: Integration — End-to-End Pipeline

### T3.1: Pipeline Orchestrator

```yaml
task_id: T3.1
name: "Pipeline Orchestrator"
status: complete
dependencies: [T1.1, T1.2, T2.2]

interface:
  input: "WebSocket audio stream"
  output: "Complete voice command pipeline"

input_bindings:
  whisper:
    source: T1.1
    output_port: transcription_service
    transfer: file
    required: true
  vad:
    source: T1.2
    output_port: vad_module
    transfer: file
    required: true
  synthesizer:
    source: T2.2
    output_port: synthesizer
    transfer: file
    required: true

output:
  location: file
  path: "/tmp/blueprint/${task_id}/output.json"
  ports:
    pipeline:
      type: file_path

required_capabilities:
  - python3.11

acceptance_criteria:
  - "Integrates VAD → Whisper → Boardroom → Response"
  - "End-to-end latency < 2s for typical commands"
  - "Graceful degradation on component failure"
  - "CLI test harness for Linux validation"

verification:
  smoke:
    command: "python -c 'from ambiance.pipeline import AmbiancePipeline; print(\"OK\")'"
    timeout: PT10S
  unit:
    command: "pytest tests/test_pipeline.py -v"
    timeout: PT3M
  integration:
    command: "pytest tests/integration/ -v --tb=short"
    timeout: PT5M

rollback: "git checkout HEAD -- src/ambiance/pipeline.py"

files_to_create:
  - src/ambiance/pipeline.py
  - tests/test_pipeline.py
  - tests/integration/test_e2e.py

notes: "CLI harness: `python -m ambiance.cli --audio test.wav` for local testing without iOS."
```

### T3.2: iOS Client Protocol Spec

```yaml
task_id: T3.2
name: "iOS Client Protocol Spec"
status: complete
dependencies: [T0.1, T3.1]

interface:
  input: "Backend API contract"
  output: "iOS client integration specification"

input_bindings:
  api_schema:
    source: T0.1
    output_port: api_schema
    transfer: file
    required: true
  pipeline:
    source: T3.1
    output_port: pipeline
    transfer: file
    required: true

output:
  location: file
  path: "/tmp/blueprint/${task_id}/output.json"
  ports:
    protocol_spec:
      type: file_path

required_capabilities:
  - python3.11

acceptance_criteria:
  - "WebSocket message schema documented"
  - "Audio format requirements specified"
  - "Authentication flow defined"
  - "Error handling protocol documented"

verification:
  smoke:
    command: "test -f docs/ios_protocol.md"
    timeout: PT5S
  unit:
    command: "python -m json.tool docs/api_schema.json > /dev/null"
    timeout: PT10S

rollback: "git checkout HEAD -- docs/"

files_to_create:
  - docs/ios_protocol.md
  - docs/api_schema.json

notes: "Spec-first approach. iOS client development can proceed independently once spec locked."
```

---

## Dependency Graph

```yaml
dependency_graph:
  T0.1:
    depends_on: []
    
  T0.2:
    depends_on: [T0.1]
    input_bindings:
      server: T0.1.output.server_module
      
  T1.1:
    depends_on: [T0.2]
    input_bindings:
      audio_handler: T0.2.output.audio_handler
      
  T1.2:
    depends_on: [T0.2]
    parallel_group: "voice_processing"
    input_bindings:
      audio_handler: T0.2.output.audio_handler
      
  T2.1:
    depends_on: [T1.1]
    input_bindings:
      transcription: T1.1.output.transcription_service
      
  T2.2:
    depends_on: [T2.1]
    input_bindings:
      boardroom: T2.1.output.boardroom_client
      
  T3.1:
    depends_on: [T1.1, T1.2, T2.2]
    input_bindings:
      whisper: T1.1.output.transcription_service
      vad: T1.2.output.vad_module
      synthesizer: T2.2.output.synthesizer
      
  T3.2:
    depends_on: [T0.1, T3.1]
    input_bindings:
      api_schema: T0.1.output.api_schema
      pipeline: T3.1.output.pipeline
```

**Visual Representation:**

```
T0.1 ──► T0.2 ──┬──► T1.1 ──► T2.1 ──► T2.2 ──┐
                │                              │
                └──► T1.2 ─────────────────────┼──► T3.1 ──► T3.2
                                               │
                                               └─────────────────►
```

**Critical Path:** T0.1 → T0.2 → T1.1 → T2.1 → T2.2 → T3.1 → T3.2

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-01-08 | Claude Opus | Initial specification |

---

*Blueprint Standard Format v2.0.1*
*"Backend-First Mobile Foundation"*
```

✅ Claude Code dispatch complete
Run ID: 20260108-074812-zrqdl1
Status: success
Changes: none
Workspace: /home/ubuntu/claude-executor/runs/20260108-074812-zrqdl1/workspace

═══════════════════════════════════════════════════════════════
✅ UNIFIED DISPATCH COMPLETE
═══════════════════════════════════════════════════════════════
Batch: 20260108-074811-batch-yb4i
Context: INJ-20260108-074812-d6tf2b
Use 'list-runs.sh' to see results
Use 'promote-workspace.sh <run-id>' to push changes
