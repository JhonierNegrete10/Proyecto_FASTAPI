import os

#SQLModel based on pydantic and SQLalchemy 
from sqlmodel import SQLModel

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

import logging

log = logging.getLogger("uvicorn")

# DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/foo
DATABASE_URL = settings.DATABASE_URL

engine = create_async_engine(DATABASE_URL, 
                             echo=True, # Return all doing in the db 
                             future=True
                             )


async def init_db():
    global engine
    """
    initialization of the database sync 
    """
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)
    
    


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
                        engine, 
                        class_=AsyncSession, 
                        expire_on_commit=False
                        )
    async with async_session() as session:
        yield session