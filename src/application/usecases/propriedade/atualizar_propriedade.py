from src.domain.entities import Propriedade
from src.domain.entities import Safra
from src.domain.repositories.propriedade_repository_interface import PropriedadeRepositoryInterface
from uuid import UUID


class AtualizarPropriedadeUseCase:
    def __init__(self, repository: PropriedadeRepositoryInterface):
        self.repository = repository

    def executar(
            self,
            propriedade_id: UUID,
            nome: str,
            cidade: str,
            estado: str,
            area_total: float,
            area_agricultavel: float,
            area_vegetacao: float,
            safras: list[Safra]
            ):
        propriedade = self.repository.buscar_por_id(propriedade_id)
        if not propriedade:
            raise ValueError("Propriedade não encontrada")

        propriedade.nome = nome
        propriedade.cidade = cidade
        propriedade.estado = estado
        propriedade.area_total = area_total
        propriedade.area_agricultavel = area_agricultavel
        propriedade.area_vegetacao = area_vegetacao
        propriedade.safras = safras

        return propriedade
