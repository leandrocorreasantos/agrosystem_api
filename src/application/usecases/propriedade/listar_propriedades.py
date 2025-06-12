from src.domain.repositories.propriedade_repository_interface import PropriedadeRepositoryInterface


class ListarPropriedadeUseCase:
    def __init__(self, repository: PropriedadeRepositoryInterface):
        self.repository = repository

    def executar(self):
        return self.repository.buscar_todos()
