"""
Http Routers
Web -> routers -> endpoints 
"""

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status 
from fastapi import HTTPException 
from fastapi import  Query

from typing import Optional, Any, List

from items.endpoints.itemEndpoints import  *
from users.crud.userCrud import get_by_email
from users.Security.tokens import TokenData 

from users.Security.security import Permission
from users.Security.security import get_current_user
from fastapi_permissions import list_permissions
import logging

log = logging.getLogger("uvicorn")

router = APIRouter(
    prefix= "/items", 
    tags = ["Items"]
)


@router.get("/")
async def show_items(
    ilr: ItemListResource = Permission("view", ItemListResource),
    current_user: TokenData =Depends(get_current_user),
    session : AsyncSession = Depends(get_session)
):
    """# summary

    """
    user = await get_by_email(email= current_user.sub, session= session)
    list_items_db = await get_all( session= session) 
    available_permissions = {
        index: list_permissions(user.principals(), get_item(index))
        for index in list_items_db
    }
    return [
        {
            "items": list_items_db,
            "available_permissions": available_permissions,
        }
    ]


# permission result for the fake users:
# - bob: denied
# - alice: granted


@router.post("/")
async def create_item(*, item_in : ItemBase,  
                      acls: list = Permission("create", NewItemAcl)):
    """
    * recibe el jwt, con la signature 
    
    """
    
    return [{"items": "I can haz cheese?", "list": acls}]


# here is the second interesting thing: instead of using a resource class,
# a dependable can be used. This way, we can easily acces database entries

# permission result for the fake users:
# - bob: item 1: granted, item 2: granted
# - alice: item 1: granted, item 2: granted


# @router.get("/item/{item_id}")
# async def show_item(item: Item = Permission("view", get_item)):
#     return [{"item": item}]


# permission result for the fake users:
# - bob: item 1: granted, item 2: granted
# - alice: item 1: DENIED, item 2: granted


# @app.get("/item/{item_id}/use")
# async def use_item(item: Item = Permission("use", get_item)):
#     return [{"item": item}]