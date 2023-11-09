from fastapi import FastAPI

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
    auxCurso = cursos[curso_id]
    auxCurso.update({
        "id": curso_id
    })
     
    return auxCurso

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)