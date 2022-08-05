"""
CRUD 
Created Read Updated Deleted 
All the interaction with the database 
"""
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.databaseConfig import get_session

from users.models.userModel import User

import logging

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
        """
        pass
       
        
async def get_by_email(email, 
                       session : AsyncSession): 
    user_query = await session.get(User, email)
    return user_query 


async def get_all(session: AsyncSession): 
    # async with session as client: 
    log.info("crud: entry")
    result = await session.execute(select(User))
    print(result)
    result = result.scalars().all()
    print(result)
    return [user for user in result ]


    
async def create_user(user: User ,
                      session: AsyncSession): 
    log.info("crud: entry")
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
    
     


# user = CRUDUser()