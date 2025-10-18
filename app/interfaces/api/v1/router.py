# app/interfaces/api/v1/router.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import json
from pathlib import Path
from app.interfaces.api.v1.endpoints import children


router_v1 = APIRouter(
    prefix="/api/v1",
    tags=["v1 - Sistema de Predicción Nutricional"]
)

# 📂 Ruta donde se guardarán los registros
DATA_FILE = Path("app/data/children.json")
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

# 📘 Modelo de datos
class Child(BaseModel):
    id: int
    nombre: str
    edad_meses: int
    peso: float
    talla: float
    sexo: str  # "M" o "F"

# 🩺 Verificación del sistema
@router_v1.get("/health")
def health_check():
    return {"status": "ok", "message": "🩺 API funcionando correctamente"}

# 👶 Listar niños registrados
@router_v1.get("/children")
def get_children():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    return {"total": len(data), "children": data}

# 🧾 Registrar un nuevo niño
@router_v1.post("/children")
def add_child(child: Child):
    # Cargar registros existentes
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []

    # Validar duplicados
    if any(c["id"] == child.id for c in data):
        raise HTTPException(status_code=400, detail=f"Ya existe un niño con ID {child.id}")

    # Agregar nuevo registro
    data.append(child.dict())

    # Guardar
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return {"message": f"Niño {child.nombre} registrado correctamente", "child": child.dict()}
router_v1.include_router(children.router)
