from enum import Enum

from typing import List, Optional

from pydantic import EmailStr 

from datetime import date, datetime

from sqlmodel import Field, SQLModel

from uuid import UUID, uuid4

from fastapi_permissions import configure_permissions, Allow, Deny, Authenticated

class ItemBase(SQLModel): 
    name: str = Field( default= "item name")
    owner: str = Field( default= "admin")
    
class ItemDB(ItemBase, table = True): 
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    
    def __acl__(self):
        return [
            (Allow, Authenticated, "view"),
            (Allow, "role:admin", "edit"),
            (Allow, f"user:{self.owner}", "delete"),
        ]
    