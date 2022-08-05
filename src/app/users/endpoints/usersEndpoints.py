"""
Endpoints of User 
Raise errors http 

routers -> endpoints -> CRUD 
"""

from fastapi import HTTPException, status
from fastapi import Depends 

from sqlalchemy.ext.asyncio import AsyncSession

from db.databaseConfig import get_session

from users.crud import userCrud 
from users.models.userModel import *
from users.security.security import Hash

import logging

log = logging.getLogger("uvicorn")



#? created user from router
async def create_user_db(user: UserIn, 
                    # user_in: UserIn,
                   session : AsyncSession
                   ):
    """
    - Input UserIn model 
    - Hashed the password 
    - Create user with model User of the table 
    - Injection of the dependecy Session of the db 
    """
    #todo user email lower 
    user.email = user.email.lower()
    
    #todo user exist in the db 
    user_exist = userCrud.get_by_email(user.email, session)
    
    #todo riase error 
    print(user_exist)
    if user_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Account already exist')

    #todo Hashed the password 
    user.hashed_password = Hash.hash_password(user.hashed_password)

    #todo change from userIn to User schema  
    log.info("endpoint: entry")
    user =User(**user.dict())
    
    #todo: Add User to db by crud    
    user_db = await userCrud.create_user(user, session)
    return user_db
    # except Exception as e:

    #     raise HTTPException(
    #         status_code=status.HTTP_409_CONFLICT,
    #         detail=f"Error creando usuario {e}"
    #     )
  
        
async def show_users_endpoint(session): 
    """
    call db, raise errors 
    """
    log.info("endpoint: entry")
    users = await userCrud.get_all(session)
    
    return users