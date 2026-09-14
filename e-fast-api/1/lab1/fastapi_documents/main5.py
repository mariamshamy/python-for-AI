from fastapi import FastAPI, HTTPException, status, Query


app = FastAPI(title="Documents API")


# -----------------------------
# Health endpoint
# -----------------------------

@app.get("/health")
def health_check():
    return {"status": "ok"}


# -----------------------------
# In-memory documents
# -----------------------------

documents = {
    1: {
        "id": 1,
        "title": "FastAPI Notes",
        "content": "REST basics"
    },
    2: {
        "id": 2,
        "title": "Python Notes",
        "content": "Functions and dictionaries"
    }
}


# -----------------------------
# List / search documents
# -----------------------------

@app.get("/documents")
def list_documents(
    q: str | None = Query(default=None),
    limit: int = Query(default=20, ge=1, le=100)
):

    items = list(documents.values())

    if q:
        q_lower = q.lower()

        items = [
            item
            for item in items
            if q_lower in item["title"].lower()
            or q_lower in item["content"].lower()
        ]

    items = items[:limit]

    return {
        "items": items
    }


# -----------------------------
# Get one document
# -----------------------------

@app.get("/documents/{document_id}")
def get_document(document_id: int):

    item = documents.get(document_id)

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return item


# -----------------------------
# Create document
# -----------------------------

@app.post(
    "/documents",
    status_code=status.HTTP_201_CREATED
)
def create_document(payload: dict):

    new_id = max(
        documents.keys(),
        default=0
    ) + 1

    item = {
        "id": new_id,
        **payload
    }

    documents[new_id] = item

    return item


# -----------------------------
# Update document
# -----------------------------

@app.put("/documents/{document_id}")
def update_document(
    document_id: int,
    payload: dict
):

    if document_id not in documents:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    documents[document_id] = {
        "id": document_id,
        **payload
    }

    return documents[document_id]


# -----------------------------
# Delete document
# -----------------------------

@app.delete("/documents/{document_id}")
def delete_document(document_id: int):

    if documents.pop(document_id, None) is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return {
        "deleted": document_id
    }