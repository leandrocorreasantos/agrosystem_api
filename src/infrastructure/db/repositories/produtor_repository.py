from typing import List, Optional
from uuid import UUID
from src.infrastructure.db.models import ProdutorModel
from src.domain.entities import Produtor
from src.domain.repositories.produtor_repository_interface import ProdutorRepositoryInterface
from src.infrastructure.db import db


class ProdutorRepository(ProdutorRepositoryInterface):

    def adicionar(self, produtor: Produtor) -> None:
        model = ProdutorModel(
                id=produtor.id,
                nome=produtor.nome,
                documento=produtor.documento
                )
        db.session.add(model)
        db.session.commit()

    def buscar_por_id(self, produtor_id: UUID) -> Optional[Produtor]:
        model = ProdutorModel.query.get(produtor_id)
        if model:
            return self._to_entity(model)
        return None

    def buscar_todos(self) -> List[Produtor]:
        models = ProdutorModel.query.all()
        return [self._to_entity(m) for m in models]

    def atualizar(self, produtor: Produtor) -> None:
        model = ProdutorModel.query.get(produtor.id)
        if model:
            model.nome = produtor.nome
            model.documento = produtor.documento
            model.propriedades = produtor.propriedades
            db.session.commit()

    def remover(self, produtor_id: UUID) -> None:
        model = ProdutorModel.query.get(produtor_id)
        if model:
            db.session.delete(model)
            db.session.commit()

    def _to_entity(self, model: ProdutorModel) -> Produtor:
        obj = Produtor(
                id=model.id,
                nome=model.nome,
                propriedades=model.propriedades
                )
        obj.documento = model.documento
        return obj
