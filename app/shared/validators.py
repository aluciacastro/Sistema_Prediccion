# backend/app/shared/validators.py
from pydantic import validator, BaseModel, ValidationError

class ChildValidator(BaseModel):
    weight_kg: float
    height_cm: float

    @validator("weight_kg")
    def weight_positive(cls, v):
        if v <= 0:
            raise ValidationError("weight_kg must be positive")
        return v

    @validator("height_cm")
    def height_positive(cls, v):
        if v <= 0:
            raise ValidationError("height_cm must be positive")
        return v
