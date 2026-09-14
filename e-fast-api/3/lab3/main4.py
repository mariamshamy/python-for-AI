from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

app = FastAPI()
engine = create_engine("sqlite:///documents.db")

class Base(DeclarativeBase):
    pass

class Document(Base):
    __tablename__ = "documents"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120))
    content: Mapped[str] = mapped_column(Text)
    priority: Mapped[int] = mapped_column(default=1)

Base.metadata.create_all(engine)

class DocumentCreate(BaseModel):
    title: str
    content: str
    priority: int = 1

@app.get("/documents")
def list_documents():
    with Session(engine) as db:
        return db.query(Document).all()

@app.post("/documents")
def create_document(payload: DocumentCreate):
    with Session(engine) as db:
        doc = Document(title=payload.title, content=payload.content, priority=payload.priority)
        db.add(doc)
        db.commit()
        db.refresh(doc)
        return doc

@app.get("/documents/{document_id}")
def get_document(document_id: int):
    with Session(engine) as db:
        doc = db.get(Document, document_id)
        if doc is None:
            raise HTTPException(404, "Document not found")
        return doc
