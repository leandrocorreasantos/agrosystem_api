from typing import List
from src.domain.entities import Safra
from src.domain.entities.cultura import Cultura
from src.domain.repositories.safra_repository_interface import SafraRepositoryInterface


class CadastrarSafraUseCase:
    def __init__(self, repository: SafraRepositoryInterface):
        self.repository = repository

    def executar(
            self,
            ano: str,
            culturas: List[Cultura]
            ) -> Safra:
        safra = Safra(
                ano=ano,
                culturas=culturas
                )
        self.repository.adicionar(safra)
        return safra
