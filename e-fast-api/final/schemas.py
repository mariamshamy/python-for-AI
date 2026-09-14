from typing import Literal

from pydantic import BaseModel, Field


class DocumentCreate(BaseModel):
    title: str = Field(min_length=3, max_length=120)
    content: str = Field(min_length=1)
    priority: int = Field(default=1, ge=1, le=5)
    description: str | None = Field(default=None, max_length=250)


class DocumentResponse(BaseModel):
    id: int
    title: str
    content: str
    priority: int
    description: str | None = None
    ai_summary: str | None = None

    model_config = {"from_attributes": True}


class AIAnalysisResponse(BaseModel):
    summary: str
    key_points: list[str]
    category: Literal["technical", "business", "general"]
    suggested_priority: int = Field(ge=1, le=5)


class AgentAskRequest(BaseModel):
    message: str = Field(min_length=1, max_length=1000)


class AgentAskResponse(BaseModel):
    answer: str


class ListDocumentsArgs(BaseModel):
    pass


class GetDocumentArgs(BaseModel):
    document_id: int = Field(gt=0)


class SearchDocumentsArgs(BaseModel):
    query: str = Field(min_length=1, max_length=120)
