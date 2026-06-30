from fastapi import APIRouter, HTTPException
from app.schemas.request import IncidentRequest
from app.schemas.response import IncidentResponse
from app.services.incident_service import process_incident_text
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/extract", response_model=IncidentResponse, tags=["Incidents"])
async def extract_incident(request: IncidentRequest):
    try:
        return await process_incident_text(request.text)
    except Exception as e:
        logger.error(f"Error extracting incident: {e}")
        raise HTTPException(status_code=500, detail="Failed to process incident data via LLM.")