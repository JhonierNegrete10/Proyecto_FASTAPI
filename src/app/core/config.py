import os 
from dotenv import load_dotenv
from pathlib import Path 
from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    # settings of the docker-compose 
    PROJECT_NAME:str = "backend-Prueba"
    PROJECT_VERSION:str = "0.1"
    POSTGRES_DB:str = os.getenv('POSTGRES_DB')
    POSTGRES_USER:str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD:str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_SERVER:str = os.getenv('POSTGRES_SERVER')
    POSTGRES_PORT:str = os.getenv('POSTGRES_PORT')
    DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    FIRST_SUPERUSER:str = os.getenv("FIRST_SUPERUSER")
    FIRST_SUPERUSER_PASSWORD :str = os.getenv("FIRST_SUPERUSER_PASSWORD")
    
    
settings = Settings()