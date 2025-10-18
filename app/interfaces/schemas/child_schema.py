# backend/app/interfaces/schemas/child_schema.py
from pydantic import BaseModel, Field, conint
from datetime import date
from typing import Optional

class ChildSchema(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    birth_date: date
    sex: str
    weight_kg: float
    height_cm: float
    socioeconomic_level: Optional[conint(ge=0, le=6)]
    residence_zone: Optional[str]
