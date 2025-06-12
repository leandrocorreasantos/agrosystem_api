from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities import Propriedade
from uuid import UUID


class PropriedadeRepositoryInterface(ABC):

    @abstractmethod
    def adicionar(self, propriedade: Propriedade) -> None:
        pass

    @abstractmethod
    def buscar_por_id(self, propriedade_id: UUID) -> Optional[Propriedade]:
        pass

    @abstractmethod
    def buscar_todos(self) -> List[Propriedade]:
        pass

    @abstractmethod
    def atualizar(self, propriedade: Propriedade) -> None:
        pass

    @abstractmethod
    def remover(self, propriedade_id: UUID) -> None:
        pass
