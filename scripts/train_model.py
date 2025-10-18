# backend/scripts/train_model.py
# Script skeleton to train a model and save it into infrastructure/ml/models/
import pickle
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from pathlib import Path

def train_dummy(output_path: str):
    X = np.random.rand(100, 4)
    y = np.random.choice(["normal", "moderate", "severe"], size=100)
    model = RandomForestClassifier(n_estimators=10)
    model.fit(X, y)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    train_dummy("app/infrastructure/ml/models/random_forest_model.pkl")
