"""
CRUD 
Created Read Updated Deleted 
All the interaction with the database 
"""
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.databaseConfig import get_session

from items.models.itemModel import ItemDB
from core.config import settings
import logging

# from users.security.security import Hash
# app.users.security.security
log = logging.getLogger("uvicorn")


async def get_item(item_id, session: AsyncSession): 
    """
    """
    query = select(ItemDB).where(ItemDB.id == item_id)
    item_query = await session.execute(query)
    item=  item_query.scalars().first()
    return item

async def get_all(session: AsyncSession): 
    # async with session as client: 
    log.info("crud: entry")
    result = await session.execute(select(ItemDB))
    # print(result)
    result = result.scalars().all()
    # print(result)
    return [item for item in result ]