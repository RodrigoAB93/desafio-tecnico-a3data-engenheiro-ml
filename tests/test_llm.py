import pytest
import json
from unittest.mock import patch, AsyncMock, MagicMock
from app.llm.ollama_client import generate_extraction


@pytest.mark.asyncio
@patch("httpx.AsyncClient.post", new_callable=AsyncMock)
async def test_generate_extraction(mock_post):
    # 1. Use MagicMock here because response.json() and response.raise_for_status() are synchronous
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None

    mock_response.json.return_value = {
        "response": json.dumps({
            "incident_type": "Falha",
            "severity": "Alta",
            "summary": "Servidor caiu",
            "entities": [
                {
                    "entity_type": "Server",
                    "value": "Servidor Principal"
                }
            ]
        })
    }

    # 2. The async post method returns the synchronous mock response
    mock_post.return_value = mock_response

    result = await generate_extraction("prompt")

    # 3. Assertions to verify it works
    assert result["incident_type"] == "Falha"
    assert result["severity"] == "Alta"
    assert len(result["entities"]) == 1
    assert result["entities"][0]["value"] == "Servidor Principal"