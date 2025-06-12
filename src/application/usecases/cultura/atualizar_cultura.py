from src.domain.entities import Cultura
from src.domain.repositories.cultura_repository_interface import CulturaRepositoryInterface
from uuid import UUID


class AtualizarCulturaUseCase:
    def __init__(self, repository: CulturaRepositoryInterface):
        self.repository = repository

    def executar(
            self,
            cultura_id: UUID,
            nome: str,
            area_utilizada: float
            ):
        cultura = self.repository.buscar_por_id(cultura_id)
        if not cultura:
            raise ValueError("Cultura não encontrada")

        cultura.nome = nome
        cultura.area_utilizada = area_utilizada
        self.repository.atualizar(cultura)

        return cultura
