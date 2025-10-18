# backend/app/application/use_cases/predict_malnutrition.py
from app.domain.repositories.prediction_repository import PredictionRepository
from app.infrastructure.ml.predictor import PredictorService
from app.domain.entities.prediction import PredictionResult
from app.application.dto.prediction_request_dto import PredictionRequestDTO

class PredictMalnutritionUseCase:
    def __init__(self, predictor: PredictorService, prediction_repo: PredictionRepository):
        self._predictor = predictor
        self._prediction_repo = prediction_repo

    def execute(self, request: PredictionRequestDTO) -> PredictionResult:
        result = self._predictor.predict(request)
        saved = self._prediction_repo.save(result)
        return saved
