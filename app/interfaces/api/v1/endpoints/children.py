# backend/app/interfaces/api/v1/endpoints/children.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.infrastructure.database.repositories.child_repository_impl import ChildRepositoryImpl
from app.application.dto.child_dto import ChildDTO
from app.domain.entities.child import Child as ChildEntity
from app.application.use_cases.register_child import RegisterChildUseCase

router = APIRouter()

@router.post("/", response_model=ChildDTO, status_code=status.HTTP_201_CREATED)
def create_child(payload: ChildDTO, db: Session = Depends(get_db)):
    repo = ChildRepositoryImpl(db)
    use_case = RegisterChildUseCase(repo)
    child_entity = ChildEntity(
        id=None,
        first_name=payload.first_name,
        last_name=payload.last_name,
        birth_date=payload.birth_date.isoformat(),
        sex=payload.sex,
        weight_kg=payload.weight_kg,
        height_cm=payload.height_cm,
        socioeconomic_level=payload.socioeconomic_level,
        residence_zone=payload.residence_zone,
    )
    created = use_case.execute(child_entity)
    return ChildDTO.from_orm(created)
