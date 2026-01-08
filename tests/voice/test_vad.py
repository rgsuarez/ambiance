import pytest
from unittest.mock import MagicMock, patch
import numpy as np
from ambiance.voice.vad import VoiceActivityDetector

def test_vad_initialization():
    vad = VoiceActivityDetector(sample_rate=16000, sensitivity=2)
    assert vad.sample_rate == 16000
    assert vad.frame_duration_ms == 30

def test_process_frame_logic():
    vad = VoiceActivityDetector(min_speech_duration_ms=60, min_silence_duration_ms=60)
    # Mock webrtcvad.Vad
    vad.vad = MagicMock()
    
    # 30ms frame at 16kHz 16-bit = 16000 * 0.03 * 2 = 960 bytes
    frame = bytes(960)
    
    # 1. Feed silence (should buffer in ring buffer but not trigger)
    vad.vad.is_speech.return_value = False
    assert vad.process_frame(frame) is None
    assert vad.triggered is False
    
    # 2. Feed speech (enough to trigger)
    vad.vad.is_speech.return_value = True
    # Ring buffer length for 60ms min speech / 30ms frame = 2 frames
    # Need > 90% voiced. 
    vad.process_frame(frame) # 1
    vad.process_frame(frame) # 2
    vad.process_frame(frame) # 3 (Should trigger now)
    
    assert vad.triggered is True
    
    # 3. Feed silence (to end segment)
    vad.vad.is_speech.return_value = False
    # Min silence 60ms / 30ms = 2 frames
    assert vad.process_frame(frame) is None # Silence 1
    assert vad.process_frame(frame) is None # Silence 2
    
    # Silence 3 -> Should finish segment
    segment = vad.process_frame(frame) 
    assert segment is not None
    assert len(segment) > 0
    assert vad.triggered is False

def test_real_webrtcvad_silence():
    """Integration test ensuring webrtcvad actually processes zeros as silence."""
    vad = VoiceActivityDetector()
    frame = bytes(960) # Silence
    
    # Should never trigger on pure silence
    for _ in range(50):
        res = vad.process_frame(frame)
        assert res is None
    
    assert vad.triggered is False
