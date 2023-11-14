"""
Pasta onde se localizar todas as dependencias utilizadas nos endpoints do fastAPI
"""
from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

async def get_session() -> Generator:
    session: AsyncSession = Session()

    ## Pedindo para devolver a sessão e esperar
    try: 
        yield session
    finally: ## Usou? fechou para não gastar conexões
        await session.close()