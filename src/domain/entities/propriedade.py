from dataclasses import dataclass, field
from typing import List, Optional
from src.domain.entities.safra import Safra
from uuid import UUID, uuid4


@dataclass
class Propriedade:
    id: UUID = field(default_factory=uuid4)
    nome: str = ""
    cidade: str = ""
    estado: str = ""
    _area_total: float = field(default=0.0, repr=False)
    _area_agricultavel: float = field(default=0.0, repr=False)
    _area_vegetacao: float = field(default=0.0, repr=False)
    safras: List[Safra] = field(default_factory=list)

    def __post_init__(self):
        self._validar_uso_do_solo()

    def _validar_uso_do_solo(self):
        total = self._area_agricultavel + self._area_vegetacao
        if total > self._area_total:
            raise ValueError("A soma das áreas agricultável e de vegetação excede a área total da propriedade")

    def total_area_utilizada_por_culturas(self) -> float:
        return sum(cultura.area_utilizada for safra in self.safras for cultura in safra.culturas)

    @classmethod
    def criar(
            cls,
            nome: str,
            cidade: str,
            estado: str,
            area_total: float,
            area_agricultavel: float,
            area_vegetacao: float,
            safras: Optional[List[Safra]] = None
            ):
        obj = cls(
                nome=nome,
                cidade=cidade,
                estado=estado,
                safras=safras or []
                )
        obj.area_total = area_total
        obj.area_vegetacao = area_vegetacao
        obj.area_agricultavel = area_agricultavel
        return obj

    @property
    def area_total(self):
        return self._area_total

    @area_total.setter
    def area_total(self, value: float):
        self._area_total = value

    @property
    def area_agricultavel(self):
        return self._area_agricultavel

    @area_agricultavel.setter
    def area_agricultavel(self, value: float):
        self._area_agricultavel = value

    @property
    def area_vegetacao(self):
        return self._area_vegetacao

    @area_vegetacao.setter
    def area_vegetacao(self, value: float):
        self._area_vegetacao = value

