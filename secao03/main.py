from typing import Optional
from fastapi import FastAPI
## Para tratar excecão
from fastapi import HTTPException
## Para ter todos os tipos de status
from fastapi import status

from models import Curso

app = FastAPI()

##Dicionario de cursos
cursos = {
    1: {
        "titulo": "Programação para Leigos",
        "aulas": 122,
        "horas": 58
    },
    2: {
        "titulo": "Algoritmos e Lógica de Programação",
        "aulas": 115,
        "horas": 45
    }
}

@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int):
    try:
        auxCurso = cursos[curso_id]
        return auxCurso
    except KeyError: ## KeyError é quando uma chave não é encontrada
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.')
    

## Mudando status da resposta de sucesso para 201
@app.post('/cursos', status_code=status.HTTP_201_CREATED)
## Deixando o post ser optional mandar o curso
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso


## usado para executar a api com ```python main.py ```
if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)