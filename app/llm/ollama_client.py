import httpx
import json
from app.config import settings

async def generate_extraction(prompt: str) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{settings.OLLAMA_BASE_URL}/api/generate",
            json={
                "model": settings.MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "format": "json" # Forces Ollama to output valid JSON
            },
            timeout=120.0
        )
        response.raise_for_status()
        data = response.json()
        return json.loads(data["response"])