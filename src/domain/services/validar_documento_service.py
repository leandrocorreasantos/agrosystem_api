import re


class ValidarDocumentoService:
    @staticmethod
    def validar(documento: str) -> bool:
        doc = re.sub(r"\D", "", documento)
        return len(doc) ==  11 or len(doc) == 14 # validação simples
