from pydantic import BaseModel, Field
from typing import Optional

class IncidentResponse(BaseModel):
    data_ocorrencia: Optional[str] = Field(None, description="Date and time of the incident, if present")
    local: str = Field(description="Location of the incident")
    tipo_incidente: str = Field(description="Type or category of the incident")
    impacto: str = Field(description="Brief description of the generated impact")