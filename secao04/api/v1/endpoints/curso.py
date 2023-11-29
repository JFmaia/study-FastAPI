from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.cursos_model import CursoModel
from schemas.curso_schema import CursoSchema
from core.database import get_db


router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CursoSchema)
async def post_curso(curso: CursoSchema, db: AsyncSession = Depends(get_db)):
    novo_curso = CursoModel(titulo = curso.titulo, aulas=curso.aulas,horas= curso.horas)

    db.add(novo_curso)
    await db.commit()

    return novo_curso


@router.get('/', response_model=List[CursoSchema])
async def get_cursos(db: AsyncSession = Depends(get_db)):
  async with db as session:
     query = select(CursoModel)
     result = await session.execute(query)
     cursos: List[CursoModel] = result.scalars().all()

     return cursos