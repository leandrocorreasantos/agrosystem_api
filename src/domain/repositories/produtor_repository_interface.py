from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities import Produtor
from uuid import UUID


class ProdutorRepositoryInterface(ABC):

    @abstractmethod
    def adicionar(self, produtor: Produtor) -> None:
        pass

    @abstractmethod
    def buscar_por_id(self, produtor_id: UUID) -> Optional[Produtor]:
        pass

    @abstractmethod
    def buscar_todos(self) -> List[Produtor]:
        pass

    @abstractmethod
    def atualizar(self, produtor: Produtor) -> None:
        pass

    @abstractmethod
    def remover(self, produtor_id: UUID) -> None:
        pass
