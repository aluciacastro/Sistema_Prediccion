# backend/app/domain/repositories/prediction_repository.py
from abc import ABC, abstractmethod
from typing import Dict, Any
from app.domain.entities.prediction import PredictionResult

class PredictionRepository(ABC):
    @abstractmethod
    def save(self, prediction: PredictionResult) -> PredictionResult: ...
    @abstractmethod
    def get_by_child(self, child_id: int) -> list[PredictionResult]: ...
