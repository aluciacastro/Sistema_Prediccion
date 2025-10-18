# backend/app/domain/entities/prediction.py
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class PredictionResult:
    child_id: int
    predicted_label: str
    probabilities: Dict[str, float]
    metadata: Dict[str, Any]
