from fastapi import FastAPI
from routes.documents import router as documents_router


app = FastAPI(
    title="Documents API",
    description="SQLite-backed JSON API for documents.",
    version="1.0.0",
)

app.include_router(documents_router)
