from fastapi import FastAPI
from app.api.routes import router
from app.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(router, prefix="/api/v1")

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}