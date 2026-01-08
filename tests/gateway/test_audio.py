import numpy as np
import pytest
from ambiance.gateway.audio import AudioBuffer

def test_audio_buffer_add_and_get():
    buffer = AudioBuffer(sample_rate=16000, window_seconds=1.0)
    
    # 0.5 seconds of audio (8000 samples)
    chunk1 = np.zeros(8000, dtype=np.int16).tobytes()
    buffer.add_chunk(chunk1)
    
    assert buffer.current_samples == 8000
    assert len(buffer.get_audio()) == 8000

def test_audio_buffer_window_sliding():
    # 0.1 second window (1600 samples)
    buffer = AudioBuffer(sample_rate=16000, window_seconds=0.1)
    
    # Add 1000 samples
    buffer.add_chunk(np.zeros(1000, dtype=np.int16).tobytes())
    assert buffer.current_samples == 1000
    
    # Add another 1000 samples (total 2000 > 1600)
    buffer.add_chunk(np.ones(1000, dtype=np.int16).tobytes())
    
    # It should have popped the first chunk
    assert buffer.current_samples == 1000
    assert np.all(buffer.get_audio() == 1)

def test_audio_buffer_clear():
    buffer = AudioBuffer()
    buffer.add_chunk(np.zeros(100, dtype=np.int16).tobytes())
    buffer.clear()
    assert buffer.current_samples == 0
    assert len(buffer.get_audio()) == 0
