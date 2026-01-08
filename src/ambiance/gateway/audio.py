import numpy as np
from collections import deque
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class AudioBuffer:
    def __init__(self, sample_rate: int = 16000, window_seconds: float = 3.0):
        self.sample_rate = sample_rate
        self.window_seconds = window_seconds
        self.max_samples = int(sample_rate * window_seconds)
        # Deque of numpy arrays (chunks)
        self.chunks = deque()
        self.current_samples = 0

    def add_chunk(self, chunk: bytes):
        """
        Add a chunk of raw PCM 16-bit 16kHz mono audio.
        """
        # Convert bytes to numpy array (int16)
        data = np.frombuffer(chunk, dtype=np.int16)
        self.chunks.append(data)
        self.current_samples += len(data)
        
        # Maintain window size
        while self.current_samples > self.max_samples:
            removed = self.chunks.popleft()
            self.current_samples -= len(removed)

    def get_audio(self) -> np.ndarray:
        """
        Get the full buffered audio as a single numpy array.
        """
        if not self.chunks:
            return np.array([], dtype=np.int16)
        return np.concatenate(list(self.chunks))

    def clear(self):
        self.chunks.clear()
        self.current_samples = 0
