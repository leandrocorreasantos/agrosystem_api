from src.domain.repositories.propriedade_repository_interface import PropriedadeRepositoryInterface
from uuid import UUID


class RemoverPropriedadeUseCase:
    def __init__(self, repository: PropriedadeRepositoryInterface):
        self.repository = repository

    def executar(self, propriedade_id: UUID):
        propriedade = self.repository.buscar_por_id(propriedade_id)
        if not propriedade:
            raise ValueError("Propriedade não encontrada")
        self.repository.remover(propriedade_id)
