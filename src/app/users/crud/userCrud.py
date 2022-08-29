"""
CRUD 
Created Read Updated Deleted 
All the interaction with the database 
"""
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.databaseConfig import get_session

from users.models.userModel import UserDB
from core.config import settings
import logging

# from users.security.security import Hash
# app.users.security.security
log = logging.getLogger("uvicorn")


class CRUDUser(): 
    def __init__(self) -> None:
        """
        defs 
        * get by email 
        * get users 
        * Update 
        * update password 
        * remove user 
        
        -from databases import database 
        database.fetch_all(query)
        database.fetch_one(query)
        database.iterate(query)
        database.execute(query)
        database.execute_many(query)
        """
        pass
       
        
async def get_by_email(email, 
                       session : AsyncSession): 
    query =select(UserDB).where(UserDB.email == email)
    user_query = await session.execute(query)
    user=  user_query.scalars().first()
    return user


async def get_all(session: AsyncSession): 
    # async with session as client: 
    log.info("crud: entry")
    result = await session.execute(select(UserDB))
    # print(result)
    result = result.scalars().all()
    # print(result)
    return [user for user in result ]


    
async def create_user(user: UserDB ,
                      session: AsyncSession): 
    log.info("crud: entry")
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
    
    
async def update_user(user: UserDB ,
                      session: AsyncSession): 
    """
    """
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
    
# async def put_super_user(session: AsyncSession):
    
#     results = await session.execute(select(UserDB).where(UserDB.email == settings.FIRST_SUPERUSER))
#     user = results.first()
#     if not user: 
#         log.info("SUPERUSER")
#         user = UserDB(email= settings.FIRST_SUPERUSER, 
#                     hashed_password= Hash.hash_password(settings.FIRST_SUPERUSER_PASSWORD), 
#                     is_super_user=True)
#         session.add(user)
#         await session.commit()
#         await session.refresh(user)
#         return {"super": "initializated"}     


# user = CRUDUser()