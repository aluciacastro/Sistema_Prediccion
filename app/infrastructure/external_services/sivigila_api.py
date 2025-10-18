# backend/app/infrastructure/external_services/sivigila_api.py
import requests
from typing import Dict, Any

class SivigilaClient:
    def __init__(self, base_url: str = "https://api.sivigila.example"):
        self.base_url = base_url

    def get_national_stats(self) -> Dict[str, Any]:
        # Minimal wrapper - in real project add retries, auth, timeouts
        resp = requests.get(f"{self.base_url}/stats")
        resp.raise_for_status()
        return resp.json()
