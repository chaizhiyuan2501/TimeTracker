from fastapi import FastAPI
from app.api import api_router

app = FastAPI(title="Time Tracker API", version="1.0.0")

app.include_router(api_router, prefix="/api", tags=["api"])

@app.get("/")
def health_check():
    return {"status": "ok", "message": "Time Tracker API is running"}
