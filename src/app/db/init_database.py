#SQLModel based on pydantic and SQLalchemy 
from requests import put
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from users.crud.userCrud import put_super_user
from db.databaseConfig import get_session

async def init_database(*, session : AsyncSession = Depends(get_session)):
    """
    initialization of the database sync 
    """
    
    # db = get_session()
    res = await put_super_user(session)
    print(res)