# 🧠 Sistema de Predicción y Clasificación de la Desnutrición Infantil

Proyecto backend desarrollado con **FastAPI**, **PostgreSQL** y **Machine Learning** para predecir y clasificar el estado nutricional de niños menores de 5 años en Valledupar.

---

## 🚀 Características

- API REST con FastAPI  
- Base de datos PostgreSQL (SQLAlchemy)  
- Modelos entrenados con Scikit-Learn  
- Arquitectura modular siguiendo principios **SOLID**  
- Contenerización con Docker y Docker Compose  
- Integración con pgAdmin  

---

## ⚙️ Instalación local

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/sistema-desnutricion.git
   cd sistema-desnutricion
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt  
3. Ejecuta el servidor:
   ```bash
   uvicorn main:app --reload           