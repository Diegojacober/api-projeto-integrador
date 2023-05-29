from typing import List
import os
from dotenv import load_dotenv

from pydantic import BaseSettings

from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    load_dotenv()
    __HOST = os.getenv('DB_HOST')
    __USER = os.getenv('DB_USER')
    __PASS = os.getenv('DB_PASS')
    __DATABASE = os.getenv('DB_NAME')

    API_V1_STR: str = '/api/v1'
    DB_URL: str = f"mysql+asyncmy://{__USER}:{__PASS}@{__HOST}/{__DATABASE}"
    DB_BASEMODEL = declarative_base()
    
    JWT_SECRET: str = 'Bs8gubS9D3gBBps05bHrjMcUkAesZp5xjq1VThEf4Lo'
    
    
    """
    Gerar token para o jwt_secret
    import secrets
    
    token: str = secrets.token_urlsafe(32)
    """
    # sha-256
    ALGORITHM: str = 'HS256'
    
    # tempos em minutos, uma semana 60min * 24horas * 35 dias = 5 semanas
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 35
    
    class Config:
        case_sensitive = True
    
settings: Settings = Settings()
