import webrtcvad
import collections
import logging
from typing import List, Tuple, Optional

logger = logging.getLogger(__name__)

class VoiceActivityDetector:
    def __init__(self, sample_rate: int = 16000, sensitivity: int = 3, min_speech_duration_ms: int = 300, min_silence_duration_ms: int = 400):
        """
        Initialize VAD.
        
        Args:
            sample_rate: Audio sample rate (must be 8000, 16000, 32000, or 48000)
            sensitivity: 0 (least aggressive) to 3 (most aggressive)
            min_speech_duration_ms: Minimum duration of speech to trigger a segment
            min_silence_duration_ms: Silence duration to consider speech ended
        """
        self.vad = webrtcvad.Vad(sensitivity)
        self.sample_rate = sample_rate
        self.frame_duration_ms = 30
        self.frame_size = int(sample_rate * self.frame_duration_ms / 1000) * 2 # 16-bit
        
        # State
        self.triggered = False
        self.speech_buffer = collections.deque()
        self.ring_buffer = collections.deque(maxlen=int(min_speech_duration_ms / self.frame_duration_ms))
        self.silence_counter = 0
        self.min_silence_frames = int(min_silence_duration_ms / self.frame_duration_ms)
        
    def process_frame(self, frame: bytes) -> Optional[bytes]:
        """
        Process a single 30ms frame of audio.
        Returns a bytes object containing a complete speech segment if one just finished, else None.
        """
        if len(frame) != self.frame_size:
            logger.warning(f"Invalid frame size: {len(frame)}. Expected {self.frame_size}")
            return None

        is_speech = self.vad.is_speech(frame, self.sample_rate)

        if not self.triggered:
            self.ring_buffer.append((frame, is_speech))
            num_voiced = len([f for f, speech in self.ring_buffer if speech])
            
            # If 90% of the ring buffer is voiced, trigger speech start
            if num_voiced > 0.9 * self.ring_buffer.maxlen:
                self.triggered = True
                # Start speech buffer with the ring buffer content
                for f, _ in self.ring_buffer:
                    self.speech_buffer.append(f)
                self.ring_buffer.clear()
        else:
            self.speech_buffer.append(frame)
            if not is_speech:
                self.silence_counter += 1
            else:
                self.silence_counter = 0
                
            # If enough silence, end speech segment
            if self.silence_counter > self.min_silence_frames:
                self.triggered = False
                self.silence_counter = 0
                
                # Combine buffer
                segment = b"".join(self.speech_buffer)
                self.speech_buffer.clear()
                return segment
                
        return None

    def process_stream(self, audio_stream: bytes) -> List[bytes]:
        """
        Process a stream of bytes, chunking into frames and returning any completed segments.
        Remaining bytes that don't fit a frame are buffered? 
        (Simplified: assumes audio_stream is multiple of frame_size for now, or drops remainder)
        """
        segments = []
        offset = 0
        while offset + self.frame_size <= len(audio_stream):
            frame = audio_stream[offset:offset + self.frame_size]
            offset += self.frame_size
            result = self.process_frame(frame)
            if result:
                segments.append(result)
        return segments
