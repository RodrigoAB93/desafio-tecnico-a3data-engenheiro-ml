from unittest.mock import AsyncMock, patch

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@patch("app.api.routes.process_incident_text", new_callable=AsyncMock)
def test_extract_endpoint(mock_process):

    mock_process.return_value = {
        "incident_type": "Falha de infraestrutura",
        "severity": "Alta",
        "summary": "Servidor caiu.",
        "entities": [
            {
                "entity_type": "Server",
                "value": "Servidor Principal"
            }
        ]
    }

    response = client.post(
        "/api/v1/extract",
        json={
            "text": "O servidor caiu às 14h em São Paulo."
        }
    )

    assert response.status_code == 200

    body = response.json()

    assert body["incident_type"] == "Falha de infraestrutura"
    assert body["severity"] == "Alta"
    assert body["summary"] == "Servidor caiu."

    assert len(body["entities"]) == 1
    assert body["entities"][0]["entity_type"] == "Server"
    assert body["entities"][0]["value"] == "Servidor Principal"