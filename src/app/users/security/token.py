from jose import JWTError, jwt
from datetime import datetime, timedelta

from core.config import settings 
from sqlmodel import SQLModel

from typing import List, Optional,Union 

class Token(SQLModel):
    access_token: str
    token_type: str

class TokenData(SQLModel):
    sub: Union[str, None] = None
    scopes: List[str] = []

   
def create_access_token(data: dict) :
    """Create access token
     
    Args: 
        - Data: TokenData =  {"sub": User.email}
        
    Return: 
        encoded_jwt: jwt.econde()
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=5*60*24)
    to_encode.update({"exp": expire}) 
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verify_token(token:str,credentials_exception)-> TokenData:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        sub: str = payload.get("sub")
        
        if sub is None:
            raise credentials_exception
        token_data = TokenData(sub=sub)
        return token_data
    except JWTError:
        raise credentials_exception
    