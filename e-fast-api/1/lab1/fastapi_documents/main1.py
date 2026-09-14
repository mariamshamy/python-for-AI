from fastapi import FastAPI

app = FastAPI(title="Documents API")


@app.get("/health")
def health_check():
    return {"status": "ok"}