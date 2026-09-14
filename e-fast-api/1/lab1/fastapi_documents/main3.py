from fastapi import FastAPI, HTTPException, status


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
# List all documents
# -----------------------------

@app.get("/documents")
def list_documents():
    return {
        "items": list(documents.values())
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
# Create a document
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