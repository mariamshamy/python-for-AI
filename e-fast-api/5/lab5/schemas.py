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

    model_config = {"from_attributes": True}
