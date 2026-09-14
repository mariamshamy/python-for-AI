from fastapi import APIRouter, File, HTTPException, UploadFile
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
        return db.query(Document).order_by(Document.id).all()


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
            raise HTTPException(
                status_code=404,
                detail="Document not found",
            )

        return doc


@router.put(
    "/{document_id}",
    response_model=DocumentResponse,
    summary="Update a document",
    responses={404: {"description": "Document not found"}},
)
def update_document(
    document_id: int,
    payload: DocumentCreate,
):
    with Session(engine) as db:
        doc = db.get(Document, document_id)

        if doc is None:
            raise HTTPException(
                status_code=404,
                detail="Document not found",
            )

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
            raise HTTPException(
                status_code=404,
                detail="Document not found",
            )

        db.delete(doc)
        db.commit()

        return {"message": "Document deleted"}


@router.post(
    "/upload",
    response_model=DocumentResponse,
    status_code=201,
    summary="Upload a text document",
    responses={400: {"description": "Unsupported or unreadable file"}},
)
async def upload_document(
    file: UploadFile = File(...),
):
    if file.content_type != "text/plain":
        raise HTTPException(
            status_code=400,
            detail="Only text/plain uploads are supported",
        )

    raw = await file.read()

    try:
        content = raw.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400,
            detail="Uploaded text must be UTF-8",
        )

    if not content.strip():
        raise HTTPException(
            status_code=400,
            detail="Uploaded document is empty",
        )

    title = (file.filename or "Uploaded document").rsplit(".", 1)[0]
    title = title[:120]

    if len(title) < 3:
        title = "Uploaded document"

    with Session(engine) as db:
        doc = Document(
            title=title,
            content=content,
            priority=1,
            description=f"Uploaded from {file.filename or 'text file'}",
        )
        db.add(doc)
        db.commit()
        db.refresh(doc)

        return doc
