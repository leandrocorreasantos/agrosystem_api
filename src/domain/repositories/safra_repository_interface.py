from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities import Safra
from uuid import UUID


class SafraRepositoryInterface(ABC):

    @abstractmethod
    def adicionar(self, safra: Safra) -> None:
        pass

    @abstractmethod
    def buscar_por_id(self, safra_id: UUID) -> Optional[Safra]:
        pass

    @abstractmethod
    def buscar_todos(self) -> List[Safra]:
        pass

    @abstractmethod
    def atualizar(self, safra: Safra) -> None:
        pass

    @abstractmethod
    def remover(self, safra_id: UUID) -> None:
        pass
