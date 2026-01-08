import logging
import asyncio
from typing import Optional, Callable, Awaitable
from ambiance.voice.vad import VoiceActivityDetector
from ambiance.voice.whisper import WhisperService
from ambiance.orchestration.boardroom import BoardroomClient
from ambiance.orchestration.synthesizer import ResponseSynthesizer
from ambiance.protocol import AmbianceMessage, MessageType

logger = logging.getLogger(__name__)

class AmbiancePipeline:
    def __init__(self, whisper_service: WhisperService, boardroom_client: BoardroomClient):
        self.vad = VoiceActivityDetector()
        self.whisper = whisper_service
        self.boardroom = boardroom_client
        self.synthesizer = ResponseSynthesizer()
        self.send_response: Optional[Callable[[AmbianceMessage], Awaitable[None]]] = None

    def set_response_callback(self, callback: Callable[[AmbianceMessage], Awaitable[None]]):
        self.send_response = callback

    async def process_audio(self, audio_chunk: bytes, correlation_id: Optional[str] = None):
        """
        Process a raw audio chunk (PCM 16kHz 16-bit mono).
        """
        # 1. VAD Processing (handle stream of arbitrary chunks)
        segments = self.vad.process_stream(audio_chunk)
        
        for segment in segments:
            logger.info("Speech segment detected. Transcribing...")
            
            # 2. Whisper Transcription (convert bytes to numpy float32)
            # numpy frombuffer int16
            import numpy as np
            audio_np = np.frombuffer(segment, dtype=np.int16)
            
            transcription = await self.whisper.transcribe(audio_np)
            text = transcription.get("text", "").strip()
            
            if text:
                logger.info(f"Transcribed: {text}")
                
                # 3. Boardroom Dispatch
                # Start session if needed (mock session ID for now)
                session_id = "default-session" 
                
                # In real flow, we might start session on connect
                
                try:
                    response = await self.boardroom.send_command(session_id, text)
                    
                    # 4. Synthesis
                    spoken_text = self.synthesizer.synthesize(response.content)
                    
                    # 5. Send Response
                    if self.send_response:
                        msg = AmbianceMessage(
                            type=MessageType.RESPONSE,
                            payload={
                                "text": response.content,
                                "spoken_text": spoken_text,
                                "original_command": text
                            },
                            correlation_id=correlation_id
                        )
                        await self.send_response(msg)
                except Exception as e:
                    logger.error(f"Boardroom error: {e}")
                    if self.send_response:
                        msg = AmbianceMessage(
                            type=MessageType.ERROR,
                            payload={"error": f"Processing failed: {str(e)}"},
                            correlation_id=correlation_id
                        )
                        await self.send_response(msg)
