# backend/app/interfaces/api/v1/endpoints/predictions.py
from fastapi import APIRouter, Depends, HTTPException
from app.core.dependencies import get_db, get_current_user
from app.infrastructure.ml.predictor import PredictorService
from app.infrastructure.database.repositories.prediction_repository_impl import PredictionRepositoryImpl
from app.application.use_cases.predict_malnutrition import PredictMalnutritionUseCase
from app.application.dto.prediction_request_dto import PredictionRequestDTO
from app.application.dto.prediction_response_dto import PredictionResponseDTO

router = APIRouter()

# instantiate repositories/services - in a fuller project these come from a DI container
predictor_service = PredictorService()
prediction_repo = PredictionRepositoryImpl()
use_case = PredictMalnutritionUseCase(predictor_service, prediction_repo)

@router.post("/", response_model=PredictionResponseDTO)
def predict(request: PredictionRequestDTO, _user=Depends(get_current_user)):
    result = use_case.execute(request)
    return PredictionResponseDTO(
        child_id=result.child_id,
        predicted_label=result.predicted_label,
        probabilities=result.probabilities,
        metadata=result.metadata,
    )
