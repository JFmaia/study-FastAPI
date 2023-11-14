"""
Pasta onde se localiza a comunicação com o banco de dados, serialização e deserialização de dados! 
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from core.config import settings

## Usa para criar tabelas no banco
engine: AsyncEngine = create_async_engine(settings.DB_URL)

## Abrir conexão com o db
Session: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_= AsyncSession,
    bind=engine
)