from fastapi import FastAPI, HTTPException

app = FastAPI(title="Documents API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


documents = {
    1: {
        "id": 1,
        "title": "FastAPI Notes",
        "content": "REST basics"
    }
}


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