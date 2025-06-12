from src.domain.entities import Propriedade
from src.domain.entities.safra import Safra
from src.domain.repositories.propriedade_repository_interface import PropriedadeRepositoryInterface


class CadastrarPropriedadeUseCase:
    def __init__(self, repository: PropriedadeRepositoryInterface):
        self.repository = repository

    def executar(
            self,
            nome: str,
            cidade: str,
            estado: str,
            area_total: float,
            area_agricultavel: float,
            area_vegetacao: float,
            safras: list[Safra]
            ) -> Propriedade:
        propriedade = Propriedade.criar(
                nome=nome,
                cidade=cidade,
                estado=estado,
                area_total=area_total,
                area_agricultavel=area_agricultavel,
                area_vegetacao=area_vegetacao,
                safras=safras,
                )
        self.repository.adicionar(propriedade)
        return propriedade
