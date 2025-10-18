# backend/app/infrastructure/database/repositories/prediction_repository_impl.py
from typing import List
from dataclasses import asdict
from app.domain.repositories.prediction_repository import PredictionRepository
from app.domain.entities.prediction import PredictionResult

# For simplicity we store predictions in memory or you can implement a DB model.
class PredictionRepositoryImpl(PredictionRepository):
    def __init__(self):
        self._store: List[PredictionResult] = []

    def save(self, prediction: PredictionResult) -> PredictionResult:
        self._store.append(prediction)
        return prediction

    def get_by_child(self, child_id: int) -> List[PredictionResult]:
        return [p for p in self._store if p.child_id == child_id]
