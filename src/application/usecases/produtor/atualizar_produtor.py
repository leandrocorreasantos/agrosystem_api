from src.domain.entities import Propriedade
from src.domain.repositories.produtor_repository_interface import ProdutorRepositoryInterface
from uuid import UUID


class AtualizarProdutorUseCase:
    def __init__(self, repository: ProdutorRepositoryInterface):
        self.repository = repository

    def executar(
            self, 
            produtor_id: UUID, 
            nome: str, 
            documento: str,
            propriedades: list[Propriedade]
            ):
        produtor = self.repository.buscar_por_id(produtor_id)
        if not produtor:
            raise ValueError("Produtor não encontrado")

        produtor.nome = nome
        produtor.documento = documento
        produtor.propriedades = propriedades
        self.repository.atualizar(produtor)

        return produtor

