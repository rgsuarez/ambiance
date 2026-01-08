import pytest
from unittest.mock import MagicMock, AsyncMock, patch
from ambiance.orchestration.boardroom import BoardroomClient

@pytest.fixture
async def client():
    client = BoardroomClient(base_url="http://test")
    yield client
    await client.close()

@pytest.mark.asyncio
async def test_start_session():
    with patch("httpx.AsyncClient.post", new_callable=AsyncMock) as mock_post:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"session_id": "sess-123"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        client = BoardroomClient()
        session_id = await client.start_session({"user": "richie"})
        
        assert session_id == "sess-123"
        mock_post.assert_called_with(
            "http://localhost:8000/boardroom/sessions",
            json={"context": {"user": "richie"}}
        )

@pytest.mark.asyncio
async def test_send_command():
    with patch("httpx.AsyncClient.post", new_callable=AsyncMock) as mock_post:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "session_id": "sess-123",
            "content": "Command executed",
            "metadata": {"tokens": 10}
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        client = BoardroomClient()
        response = await client.send_command("sess-123", "!status")
        
        assert response.content == "Command executed"
        assert response.metadata["tokens"] == 10
        mock_post.assert_called_with(
            "http://localhost:8000/boardroom/command",
            json={"session_id": "sess-123", "command": "!status"}
        )
