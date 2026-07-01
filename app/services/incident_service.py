from datetime import datetime
from app.preprocessing.cleaner import clean_text
from app.llm.prompts import INCIDENT_EXTRACTION_PROMPT
from app.llm.ollama_client import generate_extraction
from app.schemas.response import IncidentResponse


async def process_incident_text(text: str) -> IncidentResponse:
    # 1. Limpa o texto
    cleaned_text = clean_text(text)

    # 2. Captura a data/hora atual do sistema
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M")

    # 3. Injeta o texto e a data no prompt
    prompt = INCIDENT_EXTRACTION_PROMPT.format(
        text=cleaned_text,
        current_date=current_date
    )

    # 4. Envia para o LLM
    raw_response = await generate_extraction(prompt)

    # 5. Valida e retorna o Pydantic schema
    return IncidentResponse(**raw_response)