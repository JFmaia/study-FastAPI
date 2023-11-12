from fastapi import FastAPI, Response, HTTPException, status, Path, Query, Header
from models import Curso, Aluno
from typing import Optional

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

##Dicionario de alunos
alunos = {
    1: {
        "nome": "Gustavo Calvalcante da Silva",
        "idade": 22,
        "nota": 5
    },
    2: {
        "titulo": "José Flávio da Silva Maia",
        "aulas": 18,
        "nota": 3
    },
    3: {
        "titulo": "Cristal Maia Bezerra",
        "aulas": 18,
        "nota": 4
    },
    4: {
        "titulo": "Jusoe Flávio da Silva Maia",
        "aulas": 18,
        "nota": 5
    },
    5: {
        "titulo": "Mateus Flávio da Silva Maia",
        "aulas": 18,
        "nota": 4
    },
    6: {
        "titulo": "Douglas Batista da Silva",
        "aulas": 18,
        "nota": 4
    }
}

@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(title='ID do curso', description='Deve ser entre 1 e 2', gt=0, lt=3)): ##Usando path para filtrar e informar
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


@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um curso com id {curso_id}")

@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um curso com id {curso_id}")


## Utilizando Query Parametrys para testar e aprender
## Da para usar query tbm para limitar entradas de dados ou filtros
@app.get('/calculadora')
async def calcular(a: int = Query(gt=5), b: int = Query(gt=10) ,c: Optional[int] = None):
    soma: int = a + b
    if c:
        soma = soma + c
    return {"resusltado": soma}


## Treinando Header parametros
@app.get('/alunos')
async def get_alunos():
    return alunos
    
@app.post('/alunos', status_code=status.HTTP_201_CREATED)
async def post_alunos(aluno: Aluno,): 
    i: int = len(alunos) + 1
    alunos[i] = aluno
    del aluno.id
    return aluno

@app.get('/alunos/{aluno_id}')
async def get_aluno(aluno_id: int):
    if aluno_id in alunos:
        return alunos[aluno_id]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um aluno com id {aluno_id}")

## Usando Query parametros e header
@app.get('/LenAlunos')
async def getLen_alunos(nota: int = Query(lt=5), x_geek: str = Header(default=None)):
    listAlunos = []
    for i, aluno in alunos.items():
        ## Forma de comparar itens de um dicionario no python
        if "nota" in aluno and aluno["nota"] == nota:
            listAlunos.append(aluno)

    if len(listAlunos) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nenhum aluno deu nota {nota}!")
    else:
        print(x_geek)
        return listAlunos
   
## usado para executar a api com ```python main.py ```
if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)