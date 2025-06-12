from src.domain.repositories.safra_repository_interface import SafraRepositoryInterface
from uuid import UUID


class RemoverSafraUseCase:
    def __init__(self, repository: SafraRepositoryInterface):
        self.repository = repository

    def executar(self, safra_id: UUID):
        safra = self.repository.buscar_por_id(safra_id)
        if not safra:
            raise ValueError("Safra não encontrada")
        self.repository.remover(safra_id)
