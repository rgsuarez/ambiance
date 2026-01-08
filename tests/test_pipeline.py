import pytest
from unittest.mock import MagicMock, AsyncMock, patch
from ambiance.pipeline import AmbiancePipeline
from ambiance.protocol import MessageType

@pytest.fixture
def mock_components():
    whisper = MagicMock()
    whisper.transcribe = AsyncMock(return_value={"text": "hello world"})
    
    boardroom = MagicMock()
    boardroom.send_command = AsyncMock(return_value=MagicMock(content="Hi there"))
    
    return whisper, boardroom

@pytest.mark.asyncio
async def test_pipeline_process_audio_flow(mock_components):
    whisper, boardroom = mock_components
    pipeline = AmbiancePipeline(whisper, boardroom)
    
    # Mock VAD to return a segment
    pipeline.vad = MagicMock()
    pipeline.vad.process_stream.return_value = [b"speech_segment"]
    
    # Mock Synthesizer
    pipeline.synthesizer = MagicMock()
    pipeline.synthesizer.synthesize.return_value = "Spoken text"
    
    # Callback
    callback = AsyncMock()
    pipeline.set_response_callback(callback)
    
    await pipeline.process_audio(b"raw_audio", correlation_id="cid-1")
    
    # Verify flow
    pipeline.vad.process_stream.assert_called_with(b"raw_audio")
    whisper.transcribe.assert_called_once()
    boardroom.send_command.assert_called_once_with("default-session", "hello world")
    pipeline.synthesizer.synthesize.assert_called_with("Hi there")
    
    # Verify response message
    callback.assert_called_once()
    msg = callback.call_args[0][0]
    assert msg.type == MessageType.RESPONSE
    assert msg.payload["text"] == "Hi there"
    assert msg.payload["spoken_text"] == "Spoken text"
    assert msg.payload["original_command"] == "hello world"
    assert msg.correlation_id == "cid-1"

@pytest.mark.asyncio
async def test_pipeline_no_speech(mock_components):
    whisper, boardroom = mock_components
    pipeline = AmbiancePipeline(whisper, boardroom)
    
    # Mock VAD to return empty
    pipeline.vad = MagicMock()
    pipeline.vad.process_stream.return_value = []
    
    callback = AsyncMock()
    pipeline.set_response_callback(callback)
    
    await pipeline.process_audio(b"silence")
    
    whisper.transcribe.assert_not_called()
    boardroom.send_command.assert_not_called()
    callback.assert_not_called()
