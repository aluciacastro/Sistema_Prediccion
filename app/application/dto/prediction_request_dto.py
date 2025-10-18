# backend/app/application/dto/prediction_request_dto.py
from pydantic import BaseModel, Field

class PredictionRequestDTO(BaseModel):
    child_id: int
    age_months: int
    weight_kg: float
    height_cm: float
    sex: str
    socioeconomic_level: int | None = None
    residence_zone: str | None = None
