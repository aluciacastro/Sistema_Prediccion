# backend/app/interfaces/api/v1/endpoints/analytics.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.application.uses_cases.generate_dashboard_data import GenerateDashboardDataUseCase



router = APIRouter()

@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    use_case = GenerateDashboardDataUseCase(db)
    data = use_case.execute()
    return data
