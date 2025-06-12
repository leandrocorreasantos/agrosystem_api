from typing import List, Optional
from uuid import UUID
from src.infrastructure.db.models import SafraModel
from src.domain.entities import Safra
from src.domain.repositories.safra_repository_interface import SafraRepositoryInterface
from src.infrastructure.db import db


class SafraRepository(SafraRepositoryInterface):

    def adicionar(self, safra: Safra) -> None:
        model = SafraModel(
                id=safra.id,
                ano=safra.ano,
                culturas=safra.culturas
                )
        db.session.add(model)
        db.session.commit()

    def buscar_por_id(self, safra_id: UUID) -> Optional[Safra]:
        model = SafraModel.query.get(safra_id)
        if model:
            return self._to_entity(model)
        return None

    def buscar_todos(self) -> List[Safra]:
        models = SafraModel.query.all()
        return [self._to_entity(m) for m in models]

    def atualizar(self, safra: Safra) -> None:
        model = SafraModel.query.get(safra_id)
        if model:
            model.ano = safra.ano
            model.culturas = safra.culturas
            db.session.commit()

    def remover(self, safra_id: UUID) -> None:
        model = SafraModel.query.get(safra_id)
        if model:
            db.session.delete(model)
            db.session.commit()

    def _to_entity(self, model: SafraModel) -> Safra:
        return Safra(
                id=model.id,
                ano=model.ano,
                culturas=model.culturas
                )

