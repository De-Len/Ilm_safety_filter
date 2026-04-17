from fastapi import FastAPI

from app.api.routes.moderation import moderation_router

app = FastAPI()

app.include_router(moderation_router, prefix="/v1")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}