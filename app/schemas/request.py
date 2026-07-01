from pydantic import BaseModel, Field
from typing import Optional


class IncidentRequest(BaseModel):
    text: Optional[str] = Field(
        default=None,
        description="Raw text describing the incident"
    )

    @classmethod
    def from_raw(cls, data: str | dict):

        if isinstance(data, str):
            return cls(text=data)

        if isinstance(data, dict):
            return cls(**data)

        raise ValueError("Invalid input format")