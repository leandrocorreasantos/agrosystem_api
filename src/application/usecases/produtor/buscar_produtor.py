from src.domain.repositories.produtor_repository_interface import ProdutorRepositoryInterface
from uuid import UUID


class BuscarProdutorUseCase:
    def __init__(self, repository: ProdutorRepositoryInterface):
        self.repository = repository

    def executar(self, produtor_id: UUID):
        produtor = self.repository.buscar_por_id(produtor_id)
        if not produtor:
            raise ValueError("Produtor não encontrado")
        return produtor
