from src.domain.repositories.cultura_repository_interface import CulturaRepositoryInterface
from uuid import UUID


class BuscarCulturaUseCase:
    def __init__(self, repository: CulturaRepositoryInterface):
        self.repository = repository

    def executar(self, cultura_id: UUID):
        cultura = self.repository.buscar_por_id(cultura_id)
        if not cultura:
            raise ValueError("Cultura não encontrada")
        return cultura
