# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.interfaces.api.v1.router import router_v1

app = FastAPI(
    title="Sistema de Predicción y Clasificación de Desnutrición",
    version="1.0.0",
    description="API para el análisis nutricional infantil usando técnicas de Machine Learning."
)

# Configuración de CORS (permite llamadas desde el frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes reemplazar '*' por la URL del frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta raíz
@app.get("/")
def root():
    return {"message": "✅ API del Sistema de Predicción Nutricional funcionando correctamente"}

# 🔹 Incluir el router de la versión 1
app.include_router(router_v1)
