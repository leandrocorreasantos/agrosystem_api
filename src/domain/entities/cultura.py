from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class Cultura:
    id: UUID = field(default_factory=uuid4)
    nome: str = ""
    area_utilizada: float = 0.0
