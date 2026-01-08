from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List, Dict
import json
import logging
import base64
from ..protocol import AmbianceMessage, MessageType
from ..voice.whisper import WhisperService
from ..orchestration.boardroom import BoardroomClient
from ..pipeline import AmbiancePipeline

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Ambiance Gateway")

# Shared services
whisper_service = WhisperService()
boardroom_client = BoardroomClient()

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[WebSocket, AmbiancePipeline] = {}

    async def self_connect(self, websocket: WebSocket):
        await websocket.accept()
        pipeline = AmbiancePipeline(whisper_service, boardroom_client)
        
        async def send_response(msg: AmbianceMessage):
             await websocket.send_text(msg.model_dump_json())
        
        pipeline.set_response_callback(send_response)
        self.active_connections[websocket] = pipeline
        logger.info(f"New connection. Total: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            del self.active_connections[websocket]
            logger.info(f"Connection closed. Total: {len(self.active_connections)}")

    async def send_message(self, message: AmbianceMessage, websocket: WebSocket):
        await websocket.send_text(message.model_dump_json())

manager = ConnectionManager()

@app.on_event("shutdown")
async def shutdown_event():
    await boardroom_client.close()

@app.get("/health")
async def health_check():
    return {"status": "ok", "version": "1.0.0"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.self_connect(websocket)
    try:
        while True:
            message = await websocket.receive()
            
            if message["type"] == "websocket.receive":
                if "text" in message:
                    data = message["text"]
                    try:
                        message_dict = json.loads(data)
                        ambiance_msg = AmbianceMessage(**message_dict)
                        
                        if ambiance_msg.type == MessageType.AUDIO:
                            audio_data = base64.b64decode(ambiance_msg.payload)
                            # Process through pipeline
                            await manager.active_connections[websocket].process_audio(
                                audio_data, 
                                correlation_id=ambiance_msg.correlation_id
                            )
                            
                            # Ack
                            response = AmbianceMessage(
                                type=MessageType.STATUS,
                                payload={"status": "processing", "bytes": len(audio_data)},
                                correlation_id=ambiance_msg.correlation_id
                            )
                            await manager.send_message(response, websocket)
                        else:
                            logger.info(f"Received message: {ambiance_msg.type}")
                            response = AmbianceMessage(
                                type=MessageType.STATUS,
                                payload={"status": "received", "original_type": ambiance_msg.type},
                                correlation_id=ambiance_msg.correlation_id
                            )
                            await manager.send_message(response, websocket)
                            
                    except Exception as e:
                        logger.error(f"Error parsing message: {e}")
                        error_response = AmbianceMessage(
                            type=MessageType.ERROR,
                            payload={"error": str(e)}
                        )
                        await manager.send_message(error_response, websocket)
                
                elif "bytes" in message:
                    audio_data = message["bytes"]
                    await manager.active_connections[websocket].process_audio(audio_data)
            
            elif message["type"] == "websocket.disconnect":
                break
                
    except Exception as e:
        logger.error(f"WebSocket error: {e}")
    finally:
        manager.disconnect(websocket)