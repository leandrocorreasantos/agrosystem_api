from dataclasses import dataclass, field
from typing import List
from src.domain.entities.cultura import Cultura
from uuid import UUID, uuid4


@dataclass
class Safra:
    id: UUID = field(default_factory=uuid4)
    ano: str = ""
    culturas: List[Cultura] = field(default_factory=list)

