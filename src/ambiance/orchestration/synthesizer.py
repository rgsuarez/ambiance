import re
import logging
from typing import Dict, Any, AsyncGenerator

logger = logging.getLogger(__name__)

class ResponseSynthesizer:
    def __init__(self):
        pass

    def synthesize(self, text: str) -> str:
        """
        Convert raw LLM output to voice-friendly text.
        """
        # Remove code blocks
        # Replace ```...``` with "A code block."
        text = re.sub(r'```[\s\S]*?```', ' [Code Block] ', text)
        
        # Remove markdown headers
        text = re.sub(r'#+\s', '', text)
        
        # Remove bold/italic markers
        text = re.sub(r'\*\*|__', '', text)
        text = re.sub(r'\*|_', '', text)
        
        # Remove links [text](url) -> text
        text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
        
        # Collapse whitespace
        text = ' '.join(text.split())
        
        return text.strip()

    async def stream_synthesis(self, text_stream: AsyncGenerator[str, None]) -> AsyncGenerator[str, None]:
        """
        Synthesize a stream of text.
        (Simple implementation: buffer until sentence end?)
        For now, just pass through cleaned chunks.
        """
        async for chunk in text_stream:
            yield self.synthesize(chunk)
