## Compoente para utilização de rotas
from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v1/cursos')
async def get_cursos():
    return {"info":"Todos os cursos!"}