# app/interfaces/api/v1/endpoints/children.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.infrastructure.database.connection import get_db_session
from app.infrastructure.database.models import Child

router = APIRouter(prefix="/children", tags=["Niños"])

@router.post("/")
def create_child(
    nombre: str,
    edad_meses: int,
    peso: float,
    talla: float,
    sexo: str,
    db: Session = Depends(get_db_session)
):
    new_child = Child(
        name=nombre,
        age_months=edad_meses,
        weight_kg=peso,
        height_cm=talla,
    )
    db.add(new_child)
    db.commit()
    db.refresh(new_child)

    return {
        "message": f"Niñ@ {nombre} registrado correctamente",
        "child": {
            "id": new_child.id,
            "nombre": nombre,
            "edad_meses": edad_meses,
            "peso": peso,
            "talla": talla,
            "sexo": sexo
        }
    }
