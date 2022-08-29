"""
HTTP Routers 
Web -> routers -> endpoints 
"""
from typing import List


from fastapi import APIRouter
from fastapi import Depends
from fastapi import status


from users.endpoints.userEndpoints import *

# from app.users.security import tokens
from users.Security.tokens import TokenData
from users.Security.security import get_current_user

import logging

log = logging.getLogger("uvicorn")

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/", 
            status_code=status.HTTP_200_OK, 
            # response_model=List[UserOut], 
            )
async def show_users(*, session : AsyncSession = Depends(get_session), 
                     current_user: TokenData = Depends(get_current_user)): 
    """Show all users 
    Returns:
       list of users 
    """
    # data = user.get_users(db)
    log.info("routers: entry")
    
    data = await show_users_endpoint(session)
    return data

    
@router.post("/", 
             response_model=UserOut
             )
async def create_user(*, 
                      user_in: UserIn, 
                      session : AsyncSession = Depends(get_session)): 
    """
    Create a user 
    """
    #todo: add background task to send email 
    
    #* Entrypoint to endpoint manage 
    user_out = await create_user_db(user_in, session)
    
    return user_out 


@router.get("/me")
async def permissions(*,
                      email:str, 
                      session : AsyncSession = Depends(get_session)): 
    """
    """
    user = await change_permissions(email, session)
    
    return user 
    
    
