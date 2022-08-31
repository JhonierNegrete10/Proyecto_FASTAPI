"""
Endpoints of User 
Raise errors http 

routers -> endpoints -> CRUD 
"""

from fastapi import HTTPException, status
from fastapi import Depends 
from fastapi.encoders import jsonable_encoder
import json 
from sqlalchemy.ext.asyncio import AsyncSession

from db.databaseConfig import get_session

from users.crud import userCrud 
from users.models.userModel import *
from users.Security.security import Hash

from workers.tasks import publish_user_created_task, receive_user_published_task, receive_user_task

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
    user_exist = await userCrud.get_by_email(user.email, session)
    
    #todo riase error 
    print(user_exist)
    if user_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Account already exist')

    #todo Hashed the password 
    user.hashed_password = Hash.hash_password(user.hashed_password)

    #todo change from userIn to User schema  
    log.info("endpoint: entry")
    user_db =UserDB(**user.dict())
    # user_db.principals= f"user:{user_db.email}"
    #todo: Add User to db by crud    
    user_result = await userCrud.create_user(user_db, session)
    return user_result
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

async def change_permissions(email ,session): 
    """
    
    """
    
    user: UserDB = await userCrud.get_by_email(email, session)
    print("-"*30)
    print(user.principals())
    user.permissions = ["role:admin"]
    return user.principals()
    # if not  "role:admin" in user.principals: 
    #     user.principals.append("role:admin")
        
    user = await userCrud.update_user(user, session)
    
    return user 
    
    
async def get_user_published_endpoint(): 
    """
    
    """
    # userCrud.recive_user_published_endpoint(email, session)
    data = receive_user_published_task.delay()
    return data 
    
    
async def get_queue_published_endpoint(): 
    """
    
    """
    # userCrud.recive_user_published_endpoint(email, session)
    data = receive_user_task()
    
    return json.loads( data )
    
    
async def publish_user_created_endpoint(email, session): 
    """
    
    """
    # userCrud.recive_user_published_endpoint(email, session)
    user = await userCrud.get_by_email(email, session)
    data = jsonable_encoder(user)
    data = json.dumps(data)
    # print(data)
    # msm = publish_user_created_task.delay(data)
    task = publish_user_created_task.delay(data)
    return   task.id


    
    
    