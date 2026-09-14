from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from database import engine
from models import Document
from schemas import DocumentCreate, DocumentResponse


router = APIRouter(prefix="/documents", tags=["documents"])


@router.get(
    "",
    response_model=list[DocumentResponse],
    summary="List documents",
)
def list_documents():
    with Session(engine) as db:
        return db.query(Document).all()


@router.post(
    "",
    response_model=DocumentResponse,
    status_code=201,
    summary="Create a document",
)
def create_document(payload: DocumentCreate):
    with Session(engine) as db:
        doc = Document(
            title=payload.title,
            content=payload.content,
            priority=payload.priority,
            description=payload.description,
        )
        db.add(doc)
        db.commit()
        db.refresh(doc)
        return doc


@router.get(
    "/{document_id}",
    response_model=DocumentResponse,
    summary="Get one document",
    responses={404: {"description": "Document not found"}},
)
def get_document(document_id: int):
    with Session(engine) as db:
        doc = db.get(Document, document_id)
        if doc is None:
            raise HTTPException(404, "Document not found")
        return doc


@router.put(
    "/{document_id}",
    response_model=DocumentResponse,
    summary="Update a document",
    responses={404: {"description": "Document not found"}},
)
def update_document(document_id: int, payload: DocumentCreate):
    with Session(engine) as db:
        doc = db.get(Document, document_id)
        if doc is None:
            raise HTTPException(404, "Document not found")

        doc.title = payload.title
        doc.content = payload.content
        doc.priority = payload.priority
        doc.description = payload.description

        db.commit()
        db.refresh(doc)
        return doc


@router.delete(
    "/{document_id}",
    summary="Delete a document",
    responses={404: {"description": "Document not found"}},
)
def delete_document(document_id: int):
    with Session(engine) as db:
        doc = db.get(Document, document_id)
        if doc is None:
            raise HTTPException(404, "Document not found")

        db.delete(doc)
        db.commit()
        return {"message": "Document deleted"}
