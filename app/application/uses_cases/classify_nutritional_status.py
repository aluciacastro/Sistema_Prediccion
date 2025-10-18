# backend/app/application/use_cases/classify_nutritional_status.py
from app.application.dto.prediction_request_dto import PredictionRequestDTO
from app.domain.values_objects.nutritional_status import NutritionalStatus



class ClassifyNutritionalStatusUseCase:
    def execute(self, request: PredictionRequestDTO) -> NutritionalStatus:
        """Clasifica el estado nutricional del niño según su IMC."""
        if request.height_cm <= 0:
            bmi = 0
        else:
            bmi = request.weight_kg / ((request.height_cm / 100) ** 2)

        # Clasificación simple basada en rangos de IMC (puedes reemplazar con lógica OMS)
        if bmi <= 13:
            return NutritionalStatus.SEVERE
        elif bmi <= 14.5:
            return NutritionalStatus.MODERATE
        else:
            return NutritionalStatus.NORMAL
