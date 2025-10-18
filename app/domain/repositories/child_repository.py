# backend/app/domain/repositories/child_repository.py
from abc import ABC, abstractmethod
from typing import Optional, List
from app.domain.entities.child import Child

class ChildRepository(ABC):
    @abstractmethod
    def create(self, child: Child) -> Child: ...
    @abstractmethod
    def get_by_id(self, child_id: int) -> Optional[Child]: ...
    @abstractmethod
    def list(self, limit: int = 100, offset: int = 0) -> List[Child]: ...
    @abstractmethod
    def update(self, child_id: int, data: dict) -> Optional[Child]: ...
