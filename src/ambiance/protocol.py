from enum import Enum
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field
import time

class MessageType(str, Enum):
    AUDIO = "audio"
    TEXT = "text"
    COMMAND = "command"
    RESPONSE = "response"
    STATUS = "status"
    ERROR = "error"

class AmbianceMessage(BaseModel):
    type: MessageType
    payload: Any
    timestamp: float = Field(default_factory=time.time)
    correlation_id: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
