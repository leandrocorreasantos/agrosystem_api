from src.domain.repositories.safra_repository_interface import SafraRepositoryInterface


class ListarSafraUseCase:
    def __init__(self, repository: SafraRepositoryInterface):
        self.repository = repository

    def executar(self):
        return self.repository.buscar_todos()
