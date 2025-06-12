from src.domain.repositories.produtor_repository_interface import ProdutorRepositoryInterface


class ListarProdutoresUseCase:
    def __init__(self, repository: ProdutorRepositoryInterface):
        self.repository = repository

    def executar(self):
        return self.repository.buscar_todos()
