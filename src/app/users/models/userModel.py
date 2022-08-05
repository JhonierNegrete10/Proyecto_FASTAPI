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
    email: EmailStr= Field(..., primary_key=True)


class UserLogin(UserBase):
    password:str= Field(
        min_length=8,
        max_length=64,
        default = "12345678"
    )


class UserIn(UserBase): 
    birth_date: Optional[date] =Field(default=date(2000,1,1))  
    hased_password:str = Field(
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
     

        
#models of the tables, in the db  
#Schema Of the user in the database  
class User(UserIn, table= True): 
    photo: Optional[str] = None
    created_at:datetime =datetime.now() 
    updated_at:datetime =datetime.now() 
    is_active: bool = Field(default = False, 
            description="It is a active user when verify email code ")
    verify_code: Optional[str] = None 

class UserOut(UserBase):
    first_name: str 
    last_name: str 
     
    
