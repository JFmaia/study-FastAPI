from typing import Optional

from pydantic import BaseModel

class Curso(BaseModel):
    ## Mostrando que o campo é opicional
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int


