from fastapi import (
    FastAPI,
    File,
    UploadFile,
    HTTPException
)


app = FastAPI(title="Documents API")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/documents/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    if file.content_type not in {
        "text/plain",
        "application/pdf"
    }:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type"
        )

    content = await file.read()

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(content)
    }