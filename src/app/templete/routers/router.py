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

from app.concept.endpoints.conceptEndpoints import  *


import logging

log = logging.getLogger("uvicorn")

router = APIRouter(
    prefix= "/router", 
    tags = ["router"]
)

