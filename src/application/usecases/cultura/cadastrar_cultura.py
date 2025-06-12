from src.domain.entities import Cultura
from src.domain.repositories.cultura_repository_interface import CulturaRepositoryInterface


class CadastrarCulturaUseCase:
    def __init__(self, repository: CulturaRepositoryInterface):
        self.repository = repository

    def executar(
            self,
            nome: str,
            area_utilizada: float
            ) -> Cultura:
        cultura = Cultura(
                nome=nome,
                area_utilizada=area_utilizada
                )
        self.repository.adicionar(cultura)
        return cultura
