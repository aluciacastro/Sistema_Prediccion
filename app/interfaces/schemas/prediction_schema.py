# backend/app/interfaces/schemas/prediction_schema.py
from pydantic import BaseModel

class PredictionSchema(BaseModel):
    child_id: int
    age_months: int
    weight_kg: float
    height_cm: float
    sex: str
    socioeconomic_level: int | None
    residence_zone: str | None
