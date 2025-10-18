# backend/app/infrastructure/database/repositories/child_repository_impl.py
from typing import Optional, List
from sqlalchemy.orm import Session
from app.domain.entities.child import Child as ChildEntity
from app.domain.repositories.child_repository import ChildRepository
from app.infrastructure.database.models import Child as ChildModel

class ChildRepositoryImpl(ChildRepository):
    def __init__(self, db: Session):
        self.db = db

    def _to_entity(self, model: ChildModel) -> ChildEntity:
        return ChildEntity(
            id=model.id,
            first_name=model.first_name,
            last_name=model.last_name,
            birth_date=model.birth_date.isoformat(),
            sex=model.sex,
            weight_kg=model.weight_kg,
            height_cm=model.height_cm,
            socioeconomic_level=model.socioeconomic_level,
            residence_zone=model.residence_zone,
        )

    def create(self, child: ChildEntity) -> ChildEntity:
        model = ChildModel(
            first_name=child.first_name,
            last_name=child.last_name,
            birth_date=child.birth_date,
            sex=child.sex,
            weight_kg=child.weight_kg,
            height_cm=child.height_cm,
            socioeconomic_level=child.socioeconomic_level,
            residence_zone=child.residence_zone,
        )
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        return self._to_entity(model)

    def get_by_id(self, child_id: int) -> Optional[ChildEntity]:
        model = self.db.query(ChildModel).filter(ChildModel.id == child_id).first()
        return self._to_entity(model) if model else None

    def list(self, limit: int = 100, offset: int = 0) -> List[ChildEntity]:
        rows = self.db.query(ChildModel).offset(offset).limit(limit).all()
        return [self._to_entity(r) for r in rows]

    def update(self, child_id: int, data: dict) -> Optional[ChildEntity]:
        model = self.db.query(ChildModel).filter(ChildModel.id == child_id).first()
        if not model:
            return None
        for k, v in data.items():
            if hasattr(model, k):
                setattr(model, k, v)
        self.db.commit()
        self.db.refresh(model)
        return self._to_entity(model)
