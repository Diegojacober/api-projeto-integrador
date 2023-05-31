from typing import List
import os
import urllib

from pydantic import BaseSettings

from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    
    __HOST = os.environ.get('DB_HOST', 'localhost')
    __USER = os.environ.get('DB_USER', 'root')
    __PASS = os.environ.get('DB_PASS', '')
    __DATABASE = os.environ.get('DB_NAME', 'integrador')

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
