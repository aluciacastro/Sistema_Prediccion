# backend/app/shared/utils.py
from datetime import date

def calculate_age_months(birth_date: date, reference_date: date | None = None) -> int:
    ref = reference_date or date.today()
    years = ref.year - birth_date.year
    months = ref.month - birth_date.month
    total = years * 12 + months
    if ref.day < birth_date.day:
        total -= 1
    return max(total, 0)
