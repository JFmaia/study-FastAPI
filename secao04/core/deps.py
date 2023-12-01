from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import SessionLocal

async def get_session() -> Generator:
    session: AsyncSession = SessionLocal()

    try: 
        yield session
    
    finally:
        await session.close()
    