# backend/app/domain/value_objects/nutritional_status.py
from enum import Enum

class NutritionalStatus(str, Enum):
    NORMAL = "normal"
    MODERATE = "moderate"
    SEVERE = "severe"
