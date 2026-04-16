from typing import Dict

from pydantic import BaseModel, Field


class Request(BaseModel):
    text: str = Field(min_length=1)

class Response(BaseModel):
    scores: Dict[str, float]
    decision: str | None = None