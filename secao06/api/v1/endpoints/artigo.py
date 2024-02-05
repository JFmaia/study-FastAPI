from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import  AsyncSession
from sqlalchemy.future import  select

from models.artigo_model import ArtigoModel
from models.usuario_model import UsuarioModel
from schemas.artigo_schema import ArtigoSchema
from core.deps import get_session, get_current_user

router = APIRouter()

#POST Artigo
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ArtigoSchema)
async def post_artigo(
    artigo: ArtigoSchema, 
    usuario_logado: UsuarioModel = Depends(get_current_user), 
    db: AsyncSession = Depends(get_session)
):
    novo_artigo: ArtigoModel = ArtigoModel(
        titulo=artigo.titulo, 
        descricao=artigo.descricao, 
        url_fonte= artigo.url_fonte, 
        usuario_id=usuario_logado.id
    )

    db.add(novo_artigo)
    await db.commit()

    return novo_artigo

#GET Artigos
@router.get('/', response_model= List[ArtigoSchema], status_code=status.HTTP_200_OK)
async def get_artigos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ArtigoModel)
        result = await session.execute(query)
        artigos: List[ArtigoModel] = result.scalars().unique().all()

    return artigos

