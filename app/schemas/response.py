from pydantic import BaseModel, Field
from typing import List, Optional

class ExtractedEntity(BaseModel):
    entity_type: str = Field(description="E.g., Server, IP Address, Username, Service")
    value: str = Field(description="The extracted value")

class IncidentResponse(BaseModel):
    incident_type: str = Field(description="Categorization of the incident (e.g., Outage, Security, Performance)")
    severity: str = Field(description="Low, Medium, High, or Critical")
    summary: str = Field(description="A concise 1-2 sentence summary of the event")
    entities: List[ExtractedEntity] = Field(default_factory=list)