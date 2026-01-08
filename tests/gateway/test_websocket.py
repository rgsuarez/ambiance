from fastapi.testclient import TestClient
from ambiance.gateway.server import app
import pytest

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": "1.0.0"}

def test_websocket_connection():
    with client.websocket_connect("/ws") as websocket:
        data = {"type": "status", "payload": {"msg": "hello"}, "correlation_id": "test-123"}
        websocket.send_json(data)
        response = websocket.receive_json()
        assert response["type"] == "status"
        assert response["payload"]["status"] == "received"
        assert response["correlation_id"] == "test-123"

def test_invalid_json():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text("invalid json")
        response = websocket.receive_json()
        assert response["type"] == "error"

def test_binary_audio_chunk():
    with client.websocket_connect("/ws") as websocket:
        # 100 samples of zero (200 bytes)
        audio_chunk = bytes(200)
        websocket.send_bytes(audio_chunk)
        # Binary messages don't get a response to save bandwidth
        # We just ensure it doesn't crash

