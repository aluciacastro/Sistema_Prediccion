# backend/app/application/use_cases/generate_dashboard_data.py
from sqlalchemy.orm import Session
from sqlalchemy import func  # ✅ IMPORT NECESARIO
from app.infrastructure.database.models import Child, Prediction  # ✅ RUTA CORREGIDA

class GenerateDashboardDataUseCase:
    def execute(self, db: Session):
        """
        Genera datos estadísticos para el dashboard.
        Retorna el número de niños registrados, predicciones realizadas,
        y el porcentaje de cada estado nutricional.
        """
        total_children = db.query(func.count(Child.id)).scalar()
        total_predictions = db.query(func.count(Prediction.id)).scalar()

        # Distribución de estados nutricionales
        nutritional_distribution = (
            db.query(Prediction.nutritional_status, func.count(Prediction.id))
            .group_by(Prediction.nutritional_status)
            .all()
        )

        distribution_data = {
            status: count for status, count in nutritional_distribution
        }

        return {
            "total_children": total_children or 0,
            "total_predictions": total_predictions or 0,
            "distribution": distribution_data
        }
