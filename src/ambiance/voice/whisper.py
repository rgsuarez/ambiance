import whisper
import numpy as np
import torch
import logging
import asyncio
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

class WhisperService:
    def __init__(self, model_name: str = "base", device: Optional[str] = None):
        self.model_name = model_name
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model = None
        logger.info(f"Initializing WhisperService with model '{model_name}' on {self.device}")

    def load_model(self):
        """
        Load the Whisper model. This is blocking and heavy.
        """
        if self.model is None:
            logger.info(f"Loading Whisper model '{self.model_name}'...")
            self.model = whisper.load_model(self.model_name, device=self.device)
            logger.info("Model loaded successfully.")

    async def transcribe(self, audio: np.ndarray) -> Dict[str, Any]:
        """
        Transcribe audio numpy array.
        Audio must be 16kHz mono float32.
        """
        if self.model is None:
            self.load_model()

        if len(audio) == 0:
            return {"text": "", "segments": []}

        # Whisper expects float32
        if audio.dtype != np.float32:
            audio = audio.astype(np.float32) / 32768.0

        # Run in executor to avoid blocking event loop
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, self._run_transcription, audio)
        return result

    def _run_transcription(self, audio: np.ndarray) -> Dict[str, Any]:
        """
        Blocking transcription call.
        """
        return self.model.transcribe(audio, fp16=(self.device == "cuda"))
