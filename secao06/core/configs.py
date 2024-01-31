from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    API_V1_STR: str

    @property
    def DB_URL(self) -> str:
        return f'postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@localhost:{self.DATABASE_PORT}/{self.POSTGRES_DB}'
   
    DBBaseModel: ClassVar = declarative_base()

    #DIca de como gerar token no pront do python: token: str = secrets.token_urlsafe(32)
    JWT_SECRET: str
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        env_file = './.env'
        case_sensitive = True


settings: Settings = Settings()