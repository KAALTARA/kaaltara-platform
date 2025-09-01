from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()


origins = os.getenv("CORS_ORIGINS", "").split(",") if os.getenv("CORS_ORIGINS") else []

app.add_middleware(
CORSMiddleware,
allow_origins=origins or [""],
allow_credentials=True,
allow_methods=[""],
allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/api/hello")
def hello():
    return {"message": "Backend is live"}