from fastapi import APIRouter, HTTPException, Request
from app.schemas.request import IncidentRequest
from app.schemas.response import IncidentResponse
from app.services.incident_service import process_incident_text
import logging
import json

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post(
    "/extract",
    response_model=IncidentResponse,
    tags=["Incidents"],
    openapi_extra={
        "requestBody": {
            "content": {
                "application/json": {
                    "schema": {
                        "type": "object",
                        "properties": {
                            "text": {
                                "type": "string",
                                "description": "Raw text describing the incident"
                            }
                        }
                    },
                    "example": {"text": "A collision occurred on Main St. causing traffic."}
                },
                "text/plain": {
                    "schema": {
                        "type": "string",
                        "description": "Raw text describing the incident"
                    },
                    "example": "A collision occurred on Main St. causing traffic."
                }
            },
            "required": True,
            "description": "Provide the incident details as a JSON object or raw text."
        }
    }
)
async def extract_incident(request: Request):
    try:
        content_type = request.headers.get("content-type", "")
        body = await request.body()

        # -------------------------
        # JSON input
        # -------------------------
        if "application/json" in content_type:
            try:
                data = json.loads(body)
                incident = IncidentRequest(**data)
                text = incident.text
            except Exception:
                raise HTTPException(status_code=400, detail="Invalid JSON payload")

        # -------------------------
        # Raw text input
        # -------------------------
        else:
            text = body.decode("utf-8").strip()

            if not text:
                raise HTTPException(status_code=400, detail="Empty request body")

        # chama service normalmente
        result = await process_incident_text(text)
        return result

    except HTTPException:
        raise

    except Exception as e:
        logger.error(f"Error extracting incident: {e}")
        raise HTTPException(
            status_code=500,
            detail="Failed to process incident data via LLM."
        )