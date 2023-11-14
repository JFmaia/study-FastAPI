from typing import Optional
## Adicionando o validator
from pydantic import BaseModel, validator

class Curso(BaseModel):
    ## Mostrando que o campo é opicional
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    ## validando o campo titulo com as regras que definimos
    @validator('titulo')
    def validar_titulo(cls, value):
        palavras = value.split(' ')
        ## Validação 1
        if len(palavras) < 3:
            raise ValueError('O título deve ter pelo menos 3 palavras!')
        ## Validação 2
        if value.islower():
            raise ValueError('O título deve ser capitalizado.')

        return value
    
class Aluno(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    nota: int


## Cursos fakes
cursos = [
  Curso(id=1, titulo='Programação para Leigos', aulas=42, horas=56),
  Curso(id=2, titulo='Algoritmos e Logica de Programação', aulas=50, horas=70),
]

##Alunos fakes
alunos = [
  Aluno(id=1,nome= "Gustavo Calvalcante da Silva", idade= 22, nota= 5),
  Aluno(id=2,nome= "José Flávio da S. Maia", idade= 23, nota= 4),
  Aluno(id=3,nome= "João Maia Mineiro Alborgerqui", idade= 18, nota= 3),
  Aluno(id=4,nome= "Julio Mario Cabral", idade= 45, nota= 5),
]