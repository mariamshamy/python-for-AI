from pydantic import BaseModel


class DocumentCreate(BaseModel):
    title: str
    content: str
    priority: int = 1
    description: str | None = None


class DocumentResponse(BaseModel):
    id: int
    title: str
    content: str
    priority: int
    description: str | None = None

    model_config = {"from_attributes": True}
