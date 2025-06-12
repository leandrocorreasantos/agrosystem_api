from src.domain.repositories.cultura_repository_interface import CulturaRepositoryInterface


class ListarCulturaUseCase:
    def __init__(self, repository: CulturaRepositoryInterface):
        self.repository = repository

    def executar(self):
        return self.repository.buscar_todos()
