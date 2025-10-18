# backend/app/domain/value_objects/anthropometric_data.py
from dataclasses import dataclass

@dataclass(frozen=True)
class AnthropometricData:
    weight_kg: float
    height_cm: float
    age_months: int
    sex: str
