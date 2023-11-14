""" 
Schemas recebem dados json passam para o sqlalchemy que traduz para sql e vise-verso!
"""
from typing import Optional
from pydantic import BaseModel as SCBaseModel

class CursoSchema(SCBaseModel):
    id: Optional[int]
    titulo: str
    aulas: int
    horas: int

    ## Definando que sim sera usado o modo orm
    class Config:
        orm_mode=True