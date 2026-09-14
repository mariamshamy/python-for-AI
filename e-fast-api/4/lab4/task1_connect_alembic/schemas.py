from pydantic import BaseModel


class DocumentCreate(BaseModel):
    title: str
    content: str
    priority: int = 1


class DocumentResponse(BaseModel):
    id: int
    title: str
    content: str
    priority: int

    model_config = {"from_attributes": True}
