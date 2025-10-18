# backend/app/application/dto/child_dto.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class ChildDTO(BaseModel):
    id: Optional[int]
    first_name: str = Field(..., example="Adriana")
    last_name: str = Field(..., example="Castro")
    birth_date: date
    sex: str
    weight_kg: float
    height_cm: float
    socioeconomic_level: Optional[int]
    residence_zone: Optional[str]

    class Config:
        orm_mode = True
