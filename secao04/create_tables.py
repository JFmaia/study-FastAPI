from core.database import engine, Base
from models.cursos_model import CursoModel

async def create_tables():
    from models.cursos_model import CursoModel
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    print("Tabelas criadas com sucesso.")

# Execute a criação de tabelas
if __name__ == "__main__":
    import asyncio

    asyncio.run(create_tables())