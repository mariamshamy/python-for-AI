from fastapi import FastAPI, HTTPException, status

from schemas import DocumentCreate, DocumentResponse


app = FastAPI(title="Documents API")


documents = {
    1: {
        "id": 1,
        "title": "FastAPI Notes",
        "content": "REST basics",
        "priority": 1
    }
}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/documents")
def list_documents():
    return {
        "items": list(documents.values())
    }


@app.get("/documents/{document_id}")
def get_document(document_id: int):

    item = documents.get(document_id)

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return item


@app.post(
    "/documents",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_document(payload: DocumentCreate):

    new_id = max(
        documents.keys(),
        default=0
    ) + 1

    item = {
        "id": new_id,
        **payload.model_dump()
    }

    documents[new_id] = item

    return item


@app.put(
    "/documents/{document_id}",
    response_model=DocumentResponse
)
def update_document(
    document_id: int,
    payload: DocumentCreate
):

    if document_id not in documents:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    documents[document_id] = {
        "id": document_id,
        **payload.model_dump()
    }

    return documents[document_id]