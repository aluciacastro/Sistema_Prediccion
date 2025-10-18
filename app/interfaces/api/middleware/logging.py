# backend/app/interfaces/api/middleware/logging.py
from fastapi import FastAPI
import logging

def setup_logging(app: FastAPI):
    logger = logging.getLogger("uvicorn.error")
    # configure formatters/handlers as needed
    app.logger = logger
