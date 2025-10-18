# backend/app/infrastructure/ml/predictor.py
import os
import pickle
from typing import Dict, Any
from app.core.config import settings
from app.application.dto.prediction_request_dto import PredictionRequestDTO
from app.domain.entities.prediction import PredictionResult
from app.infrastructure.ml.preprocessors.data_cleaner import DataCleaner
from app.infrastructure.ml.preprocessors.feature_engineer import FeatureEngineer

class PredictorService:
    def __init__(self, model_name: str = "random_forest_model.pkl"):
        models_dir = settings.ML_MODELS_PATH
        self.model_path = os.path.join(models_dir, model_name)
        self.model = self._load_model(self.model_path)
        self.cleaner = DataCleaner()
        self.fe = FeatureEngineer()

    def _load_model(self, path: str):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Model not found at {path}")
        with open(path, "rb") as f:
            return pickle.load(f)

    def predict(self, request: PredictionRequestDTO) -> PredictionResult:
        record = {
            "age_months": request.age_months,
            "weight_kg": request.weight_kg,
            "height_cm": request.height_cm,
            "sex": request.sex,
            "socioeconomic_level": request.socioeconomic_level or 0,
        }
        df = self.cleaner.clean(record)
        X = self.fe.transform(df)
        probs = self.model.predict_proba(X)[0] if hasattr(self.model, "predict_proba") else None
        if probs is None:
            pred_idx = int(self.model.predict(X)[0])
            # fallback probabilities unknown
            probs_dict = {"unknown": 1.0}
            pred_label = str(pred_idx)
        else:
            classes = list(self.model.classes_)
            probs_dict = {cls: float(prob) for cls, prob in zip(classes, probs)}
            pred_label = max(probs_dict, key=probs_dict.get)

        return PredictionResult(
            child_id=request.child_id,
            predicted_label=str(pred_label),
            probabilities=probs_dict,
            metadata={"features": X.iloc[0].to_dict()}
        )
