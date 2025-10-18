# backend/app/application/dto/prediction_response_dto.py
from pydantic import BaseModel
from typing import Dict, Any

class PredictionResponseDTO(BaseModel):
    child_id: int
    predicted_label: str
    probabilities: Dict[str, float]
    metadata: Dict[str, Any]
