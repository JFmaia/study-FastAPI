from sqlmodel import SQLModel
from core.database import engine
from models.curso_model import CursoModel

async def create_tables() -> None:
    from models.curso_model import CursoModel

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)
    print('Tabelas criadas com sucesso...')

if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())
