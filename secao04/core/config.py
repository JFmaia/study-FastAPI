"""
Pasta para configurações gerais usadas na aplicação
"""
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    

    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+async://jfmaia:p4ssw0rd@localhost:5432/faculdade"
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True

settings = Settings()