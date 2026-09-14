from fastapi import FastAPI, HTTPException

app = FastAPI(title="Documents API")


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


@app.put("/documents/{document_id}")
def update_document(document_id: int, payload: dict):

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