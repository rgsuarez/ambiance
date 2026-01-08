import pytest
from unittest.mock import MagicMock, patch
import numpy as np
from ambiance.voice.whisper import WhisperService

@pytest.fixture
def mock_whisper():
    with patch("ambiance.voice.whisper.whisper") as mock:
        model_mock = MagicMock()
        model_mock.transcribe.return_value = {"text": "Hello world", "segments": []}
        mock.load_model.return_value = model_mock
        yield mock

@pytest.mark.asyncio
async def test_whisper_service_initialization(mock_whisper):
    service = WhisperService(model_name="tiny")
    assert service.model_name == "tiny"
    assert service.model is None

@pytest.mark.asyncio
async def test_whisper_transcription_flow(mock_whisper):
    service = WhisperService()
    
    # Create dummy audio (1 second of silence)
    audio = np.zeros(16000, dtype=np.int16)
    
    result = await service.transcribe(audio)
    
    assert result["text"] == "Hello world"
    mock_whisper.load_model.assert_called_once()
    service.model.transcribe.assert_called_once()

@pytest.mark.asyncio
async def test_empty_audio_handling(mock_whisper):
    service = WhisperService()
    service.model = MagicMock() # Pre-load mock
    
    audio = np.array([], dtype=np.int16)
    result = await service.transcribe(audio)
    
    assert result["text"] == ""
    service.model.transcribe.assert_not_called()
