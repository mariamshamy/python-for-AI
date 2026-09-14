from fastapi import FastAPI
from schemas import DocumentCreate, DocumentResponse


app = FastAPI(title="Documents API")


@app.get("/health")
def health_check():
    return {"status": "ok"}