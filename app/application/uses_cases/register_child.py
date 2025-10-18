# backend/app/application/use_cases/register_child.py
from dataclasses import asdict
from typing import Protocol
from app.domain.entities.child import Child
from app.domain.repositories.child_repository import ChildRepository

class RegisterChildUseCase:
    def __init__(self, child_repo: ChildRepository):
        self._child_repo = child_repo

    def execute(self, child: Child) -> Child:
        # business rules/validation could be placed here
        created = self._child_repo.create(child)
        return created
