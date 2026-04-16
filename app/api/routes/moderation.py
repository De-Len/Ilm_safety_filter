from fastapi import APIRouter

from app.api.schemas.schemas import Response, Request
from app.application.handler import handle_request

moderation_router = APIRouter()

@moderation_router.post("/moderate")
async def moderate(request: Request) -> Response:
    result = await handle_request(request.text)

    return Response(scores=result.scores, decision=result.decision)
