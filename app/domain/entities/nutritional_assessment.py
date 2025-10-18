# backend/app/domain/entities/nutritional_assessment.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class NutritionalAssessment:
    child_id: int
    age_months: int
    weight_kg: float
    height_cm: float
    bmi_z: Optional[float] = None
    classification: Optional[str] = None  # normal / moderate / severe
