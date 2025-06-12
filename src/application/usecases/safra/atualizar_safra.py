from typing import List
from src.domain.entities import Safra
from src.domain.entities import Cultura
from src.domain.repositories.safra_repository_interface import SafraRepositoryInterface
from uuid import UUID


class AtualizarSafraUseCase:
    def __init__(self, repository: SafraRepositoryInterface):
        self.repository = repository

    def executar(
            self,
            safra_id: UUID,
            ano: str,
            culturas: List[Cultura]
            ) -> Safra:
        safra = self.repository.buscar_por_id(safra_id)
        if not safra:
            raise ValueError("Safra não encontrada")

        safra.ano = ano
        safra.culturas = culturas
        self.repository.atualizar(safra)

        return safra
