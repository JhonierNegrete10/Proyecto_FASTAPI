"""
UserModel is typing for sqlmodel 
is the library to conect betwn sqlalchemy and pydantic 
in one usefull class 
"""

from enum import Enum
from typing import List, Optional
from pydantic import EmailStr 
from datetime import date, datetime
from sqlmodel import Field, SQLModel
from uuid import UUID, uuid4

"""
- User: Table of sql : same time userIn  
    ? ID or the email is enough 
- UserBase: email as primary jey 
- UserLogin
todo userUpdate 
todo userShow o userOut
"""

# gender enum model 
class gender(Enum): 
    male: str= "male"
    female: str= "female"



#Models to response for the api - Pydantic 
class UserBase(SQLModel):
    email: EmailStr= Field(...,
                        #    primary_key=True
                           )


class UserLogin(UserBase):
    password:str= Field(
        min_length=8,
        max_length=64,
        default = "12345678"
    )


class UserIn(UserBase): 
    """
    Schema User from http body
    """
    birth_date: Optional[date] =Field(default=date(2000,1,1))  
    hashed_password:str = Field(
        min_length=8,
        max_length=64,
        default="12345678"
    )
    first_name: str = Field(
        min_length=1,
        max_length=50,
        default = "Ándres"
    )
    last_name: str = Field(
        min_length=1,
        max_length=50,
        default= "López Gómez"
    )
    gender:str = Field(default="male") 
    phone:str = Field(
        default = "300122344"
    )
     
 
        
#Schema Of the user in the database  
class UserDB(UserIn, table= True): 
    """
     - model of the table, in the db  
    
    """
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    
    photo: Optional[str] = None
    
    created_at:datetime =datetime.now() 
    updated_at:datetime =datetime.now() 
    
    is_super_user: bool = Field(default = False)
    is_active: bool = Field(default = False, 
            description="It is a active user when verify email code ")
    verify_code: Optional[str] = None 
    permissions: List[str] = Field(default=None)
 #= [f"user:{self.email}"]
    # principals : List[str] = Field(default=None)
    
    def principals(self):
        # self.principals : List[str] = Field(default=None)
        return self.permissions

class UserOut(UserBase):
    first_name: str 
    last_name: str 
     
    
