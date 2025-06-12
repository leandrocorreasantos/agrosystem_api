from typing import List, Optional
from uuid import UUID
from src.infrastructure.db import db
from src.infrastructure.db.models import PropriedadeModel
from src.domain.entities import Propriedade
from src.domain.repositories.propriedade_repository_interface import PropriedadeRepositoryInterface


class PropriedadeRepository(PropriedadeRepositoryInterface):

    def adicionar(self, propriedade: Propriedade) -> None:
        model = PropriedadeModel(
                id=propriedade.id,
                nome=propriedade.nome,
                cidade=propriedade.cidade,
                estado=propriedade.estado,
                area_total=propriedade.area_total,
                area_agricultavel=propriedade.area_agricultavel,
                area_vegetacao=propriedade.area_vegetacao,
                safras=propriedade.safras
                )
        db.session.add(model)
        db.session.commit()

    def buscar_por_id(self, propriedade_id: UUID) -> Optional[Propriedade]:
        model = PropriedadeModel.query.get(propriedade_id)
        if model:
            return self._to_entity(model)
        return None

    def buscar_todos(self) -> List[Propriedade]:
        models = PropriedadeModel.query.all()
        return [self._to_entity(m) for m in models]

    def atualizar(self, propriedade: Propriedade) -> None:
        model = PropriedadeModel.query.get(propriedade.id)
        if model:
            model.nome = propriedade.nome
            model.cidade = propriedade.cidade
            model.estado = propriedade.estado
            model.area_total = propriedade.area_total
            model.area_agricultavel = propriedade.area_agricultavel
            model.area_vegetacao = propriedade.area_vegetacao
            safras = propriedade.safras
            db.session.commit()

    def remover(self, propriedade_id: UUID) -> None:
        model = PropriedadeModel.query.get(propriedade_id)
        if model:
            db.session.delete(model)
            db.session.commit()

    def _to_entity(self, model: Propriedade):
        obj = Propriedade(
                id=model.id,
                nome=model.nome,
                cidade=model.cidade,
                estado=model.estado,
                safras=model.safras
                )
        obj.area_total = model.area_total
        obj.area_vegetacao = model.area_vegetacao
        obj.area_agricultavel = model.area_agricultavel
        return obj
