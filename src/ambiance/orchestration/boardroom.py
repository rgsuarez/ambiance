import httpx
import logging
from typing import Dict, Any, Optional
from pydantic import BaseModel

logger = logging.getLogger(__name__)

class BoardroomResponse(BaseModel):
    session_id: str
    content: str
    metadata: Dict[str, Any] = {}

class BoardroomClient:
    def __init__(self, base_url: str = "http://localhost:8000/boardroom", api_key: Optional[str] = None):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
        self.client = httpx.AsyncClient(headers=self.headers, timeout=30.0)

    async def start_session(self, context: Dict[str, Any] = {}) -> str:
        """
        Start a new Boardroom session.
        Returns session_id.
        """
        try:
            response = await self.client.post(f"{self.base_url}/sessions", json={"context": context})
            response.raise_for_status()
            data = response.json()
            return data.get("session_id")
        except httpx.HTTPError as e:
            logger.error(f"Failed to start Boardroom session: {e}")
            raise

    async def send_command(self, session_id: str, command: str) -> BoardroomResponse:
        """
        Send a command to an active session.
        """
        try:
            payload = {
                "session_id": session_id,
                "command": command
            }
            response = await self.client.post(f"{self.base_url}/command", json=payload)
            response.raise_for_status()
            data = response.json()
            return BoardroomResponse(**data)
        except httpx.HTTPError as e:
            logger.error(f"Failed to send command to Boardroom: {e}")
            raise
    
    async def close(self):
        await self.client.aclose()
