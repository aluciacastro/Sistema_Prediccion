# backend/app/domain/entities/child.py
from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class Child:
    id: Optional[int]
    first_name: str
    last_name: str
    birth_date: str  # ISO date string
    sex: str  # 'M' or 'F'
    weight_kg: float
    height_cm: float
    socioeconomic_level: Optional[int] = None
    residence_zone: Optional[str] = None  # 'urban'/'rural' etc.
