# backend/app/infrastructure/ml/preprocessors/data_cleaner.py
import pandas as pd
from typing import Dict, Any

class DataCleaner:
    def clean(self, record: Dict[str, Any]) -> pd.DataFrame:
        df = pd.DataFrame([record])
        # Example cleaning steps
        numeric_cols = ["weight_kg", "height_cm", "age_months"]
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors="coerce")
        df = df.fillna(0)
        return df
