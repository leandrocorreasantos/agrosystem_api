from dataclasses import dataclass, field
from typing import List, Optional
from src.domain.entities.propriedade import Propriedade
from uuid import UUID, uuid4
from src.domain.services.validar_documento_service import ValidarDocumentoService


@dataclass
class Produtor:
    id: UUID = field(default_factory=uuid4)
    nome: str = ""
    _documento: str = field(default="", repr=False) # cpf ou cnpj
    propriedades: List[Propriedade] = field(default_factory=list)

    def __post_init__(self):
        self._validar_documento(self._documento)

    def _validar_documento(self, documento: str):
        return ValidarDocumentoService.validar(documento)

    @classmethod
    def criar(
            cls,
            nome: str,
            documento: str,
            propriedades: Optional[List[Propriedade]] = None
            ):
        obj = cls(
                nome=nome,
                propriedades = propriedades or []
                )
        obj.documento = documento
        return obj

    @property
    def documento(self):
        return self._documento

    @documento.setter
    def documento(self, value: str):
        self._documento = value

