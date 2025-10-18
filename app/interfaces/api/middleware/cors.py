# backend/app/interfaces/api/middleware/cors.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def add_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # restrict in prod
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
