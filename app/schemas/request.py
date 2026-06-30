from pydantic import BaseModel, Field

class IncidentRequest(BaseModel):
    text: str = Field(..., description="Raw text describing the incident")