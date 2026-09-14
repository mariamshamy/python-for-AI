import logging

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from errors import AppError
from routes.ai import router as ai_router
from routes.documents import router as documents_router


logging.basicConfig(level=logging.INFO)


app = FastAPI(
    title="SmartDoc AI",
    description=(
        "SQLite-backed Documents API with Gemini analysis "
        "and a controlled read-only document agent."
    ),
    version="1.0.0",
)


@app.exception_handler(AppError)
async def handle_app_error(
    request: Request,
    exc: AppError,
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
            }
        },
    )


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}


app.include_router(documents_router)
app.include_router(ai_router)
