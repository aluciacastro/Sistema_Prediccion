# backend/app/infrastructure/ml/preprocessors/feature_engineer.py
import pandas as pd
from typing import Dict, Any

class FeatureEngineer:
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        # Example: add BMI feature
        df["height_m"] = df["height_cm"] / 100.0
        df["bmi"] = df["weight_kg"] / (df["height_m"].replace(0, 1) ** 2)
        # encode sex
        df["sex_m"] = (df["sex"].str.upper() == "M").astype(int)
        # replace inf/nan
        df = df.replace([float("inf"), float("-inf")], 0).fillna(0)
        # keep only model features (example)
        features = ["age_months", "bmi", "sex_m", "socioeconomic_level"]
        for f in features:
            if f not in df:
                df[f] = 0
        return df[features]
