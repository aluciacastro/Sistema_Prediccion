# app/interfaces/api/v1/router.py
from fastapi import APIRouter

router_v1 = APIRouter(
    prefix="/api/v1",
    tags=["v1 - Sistema de Predicción Nutricional"]
)

@router_v1.get("/health")
def health_check():
    return {"status": "ok", "message": "🩺 API funcionando correctamente"}

@router_v1.get("/children")
def get_children_info():
    return {"message": "Listado de niños registrados (endpoint de ejemplo)"}

@router_v1.post("/predictions")
def predict_nutrition():
    return {"message": "Predicción nutricional generada (ejemplo)"}
