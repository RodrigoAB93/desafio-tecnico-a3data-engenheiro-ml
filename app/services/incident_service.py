from app.preprocessing.cleaner import clean_text
from app.llm.prompts import INCIDENT_EXTRACTION_PROMPT
from app.llm.ollama_client import generate_extraction
from app.schemas.response import IncidentResponse

async def process_incident_text(text: str) -> IncidentResponse:
    cleaned_text = clean_text(text)
    prompt = INCIDENT_EXTRACTION_PROMPT.format(text=cleaned_text)
    
    raw_response = await generate_extraction(prompt)
    
    # Parse the LLM dictionary response into the Pydantic schema
    return IncidentResponse(**raw_response)