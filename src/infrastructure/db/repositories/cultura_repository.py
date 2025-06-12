from typing import List, Optional
from uuid import UUID
from src.infrastructure.db.models import CulturaModel
from src.infrastructure.db import db
from src.domain.entities import Cultura
from src.domain.repositories.cultura_repository_interface import CulturaRepositoryInterface


class CulturaRepository(CulturaRepositoryInterface):

    def adicionar(self, cultura: Cultura) -> None:
        model = CulturaModel(
                id=cultura.id,
                nome=cultura.nome,
                area_utilizada=cultura.area_utilizada
                )
        db.session.add(model)
        db.session.commit()

    def buscar_por_id(self, cultura_id: UUID) -> Optional[Cultura]:
        model = CulturaModel.query.get(cultura_id)
        if model:
            return self._to_entity(model)
        return None

    def buscar_todos(self) -> List[Cultura]:
        models = CulturaModel.query.all()
        return [self._to_entity(m) for m in models]

    def atualizar(self, cultura: Cultura) -> None:
        model = CulturaModel.query.get(cultura.id)
        if model:
            model.nome = cultura.nome
            model.area_utilizada = cultura.area_utilizada
            db.session.commit()

    def remover(self, cultura_id: UUID) -> None:
        model = CulturaModel.query.get(cultura_id)
        if model:
            db.session.delete(model)
            db.session.commit()

    def _to_entity(self, model: CulturaModel) -> Cultura:
        return Cultura(
                id=model.id,
                nome=model.nome,
                area_utilizada=model.area_utilizada
                )
