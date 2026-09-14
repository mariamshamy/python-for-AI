from fastapi import (
    FastAPI,
    Request,
    status
)

from fastapi.responses import JSONResponse

from schemas import (
    DocumentCreate,
    DocumentResponse
)


app = FastAPI(
    title="Documents API"
)


documents = {
    1: {
        "id": 1,
        "title": "FastAPI Notes",
        "content": "REST basics",
        "priority": 1
    }
}


class AppError(Exception):

    def __init__(
        self,
        code: str,
        message: str,
        status_code: int = 400
    ):
        self.code = code
        self.message = message
        self.status_code = status_code


@app.exception_handler(AppError)
async def handle_app_error(
    request: Request,
    exc: AppError
):

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message
            }
        }
    )


@app.post(
    "/documents",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_document(
    payload: DocumentCreate
):

    for document in documents.values():

        if document["title"].lower() == payload.title.lower():

            raise AppError(
                code="duplicate_title",
                message="A document with this title already exists.",
                status_code=409
            )

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