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

import logging

log = logging.getLogger("uvicorn")



#? created user from router
async def create_user_db(user: User, 
                    # user_in: UserIn,
                   session : AsyncSession
                   ):

    #todo user email lower 
    # user_in = user_in.dict()
    # user_in["email"] = user_in["email"].lower()
    
    #todo user exist in the db 
    # user_query = () 
    #     db.query(models.User)
    #               .filter(models.User.email ==
    #                       EmailStr(user_in["email"])))
    
    #todo riase error 
    # user = user_query.first()
    # if user:
    #     raise HTTPException(status_code=status.HTTP_409_CONFLICT,
    #                         detail='Account already exist')

    #todo Hashed the password 
    # try:
        # user_in["hashed_password"] = Hash.hash_password(user_in["password"])
        # del user_in["password"]
        # # del user_in["password_confirm"]
        # user_in["gender"] = user_in["gender"].value

        # new_user = models.User(**user_in)

    #todo Add the user to the db by the crud 
    log.info("endpoint: entry")
    print(type(user), user)
    print(User(**user.dict()))
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