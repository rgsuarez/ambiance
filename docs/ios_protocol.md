# Ambiance iOS Client Protocol

## Overview
The iOS client communicates with the Ambiance Backend via a WebSocket connection. The protocol handles bidirectional audio streaming and control messages.

**Endpoint:** `wss://{gateway_url}/ws`

## Authentication
(To be defined: Zero Echelon ID integration. For now, open or API Key in headers).

## Message Structure
All text messages are JSON strings adhering to the `AmbianceMessage` schema.
Binary messages are treated as raw audio chunks (PCM 16-bit 16kHz mono).

### JSON Message Schema
```json
{
  "type": "string",
  "payload": "any",
  "timestamp": "float",
  "correlation_id": "string (optional)",
  "metadata": "object (optional)"
}
```

## Message Types

### Client -> Server

1. **Audio Chunk (Binary)**
   - Format: PCM 16-bit, 16kHz, Mono.
   - Transmission: Raw binary frames (e.g., 30ms = 960 bytes).
   - Response: None (to save bandwidth).

2. **Audio Chunk (JSON)**
   - Type: `audio`
   - Payload: Base64 encoded PCM string.
   - Use case: Debugging or non-streaming contexts.

3. **Status / Keepalive**
   - Type: `status`
   - Payload: `{"status": "ping"}`

### Server -> Client

1. **Response (Voice/Text)**
   - Type: `response`
   - Payload:
     ```json
     {
       "text": "Command output text",
       "spoken_text": "Text optimized for TTS",
       "original_command": "Transcribed user input"
     }
     ```

2. **Error**
   - Type: `error`
   - Payload: `{"error": "Description"}`

3. **Status**
   - Type: `status`
   - Payload: `{"status": "processing", "bytes": 1024}`

## Workflow

1. **Connect:** Client establishes WebSocket connection to `/ws`.
2. **Stream:** Client sends audio chunks (binary preferred).
3. **VAD:** Server detects speech activity.
4. **Transcribe:** Server transcribes speech segment.
5. **Execute:** Server routes command to Boardroom.
6. **Respond:** Server sends `response` message to Client.
7. **Display/Speak:** Client displays text and/or plays TTS (local or fetched).

## Error Handling
- WebSocket disconnect -> Client should auto-reconnect with exponential backoff.
- Server error message -> Client displays toast/alert.
