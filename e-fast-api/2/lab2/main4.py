import os

from dotenv import load_dotenv
from fastapi import FastAPI


load_dotenv()


APP_NAME = os.getenv(
    "APP_NAME",
    "Documents API"
)

MAX_UPLOAD_MB = int(
    os.getenv(
        "MAX_UPLOAD_MB",
        "5"
    )
)


app = FastAPI(
    title=APP_NAME
)


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


@app.get("/config")
def get_config():
    return {
        "app_name": APP_NAME,
        "max_upload_mb": MAX_UPLOAD_MB
    }