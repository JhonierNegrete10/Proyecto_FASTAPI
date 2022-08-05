"""
HTTP Routes 
Web -> routers -> endpoints 
"""

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from users.endpoints.usersEndpoints import *

import logging

log = logging.getLogger("uvicorn")

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/", 
            status_code=status.HTTP_200_OK)
async def show_users(*, session : AsyncSession = Depends(get_session)): 
    """Show all users 
    Returns:
       list of users 
    """
    # data = user.get_users(db)
    log.info("routers: entry")
    
    data = await show_users_endpoint(session)
    return data
    
@router.post("/", 
             )
async def create_user(*, 
                      user_in: User, 
                      session : AsyncSession = Depends(get_session)): 
    #todo: add background task to send email 
    
    #* Entrypoint to endpoint manage 
    
    data = await create_user_db(user_in, session)
    return {"user": "created"}
