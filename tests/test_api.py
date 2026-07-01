from unittest.mock import AsyncMock, patch
from fastapi.testclient import TestClient

from app.main import app
from app.schemas.response import IncidentResponse

client = TestClient(app)

@patch("app.api.routes.process_incident_text", new_callable=AsyncMock)
def test_extract_endpoint(mock_process):
    # The mock returns the exact Pydantic model expected by your route
    mock_process.return_value = IncidentResponse(
        data_ocorrencia="2025-08-12 14:00",
        local="São Paulo",
        tipo_incidente="Falha no servidor",
        impacto="Sistema de faturamento indisponível por 2 horas"
    )

    response = client.post(
        "/api/v1/extract",
        json={
            "text": "Ontem às 14h, no escritório de São Paulo, houve uma falha no servidor principal que afetou o sistema de faturamento por 2 horas."
        }
    )

    # Assert the request was successful
    assert response.status_code == 200

    body = response.json()

    # Assert the response matches our mock and the required challenge fields
    assert body["data_ocorrencia"] == "2025-08-12 14:00"
    assert body["local"] == "São Paulo"
    assert body["tipo_incidente"] == "Falha no servidor"
    assert body["impacto"] == "Sistema de faturamento indisponível por 2 horas"