from src.domain.entities import Produtor
from src.domain.entities import Propriedade
from src.domain.repositories.produtor_repository_interface import ProdutorRepositoryInterface


class CadastrarProdutorUseCase:
    def __init__(self, repository: ProdutorRepositoryInterface):
        self.repository = repository

    def executar(
            self, 
            nome: str, 
            documento: str, 
            propriedades: list[Propriedade]
            ) -> Produtor:
        produtor = Produtor.criar(
                nome=nome,
                documento=documento,
                propriedades=propriedades,
                )

        self.repository.adicionar(produtor)
        return produtor

