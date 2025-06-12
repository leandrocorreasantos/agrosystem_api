from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities import Cultura
from uuid import UUID


class CulturaRepositoryInterface(ABC):

    @abstractmethod
    def adicionar(self, cultura: Cultura) -> None:
        pass

    @abstractmethod
    def buscar_por_id(self, cultura_id: UUID) -> Optional[Cultura]:
        pass

    @abstractmethod
    def buscar_todos(self) -> List[Cultura]:
        pass

    @abstractmethod
    def atualizar(self, cultura: Cultura) -> None:
        pass

    @abstractmethod
    def remover(self, cultura_id: UUID) -> None:
        pass
