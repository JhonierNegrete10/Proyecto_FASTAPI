from sqlalchemy.orm import Session 
# from app.db import models
from fastapi import HTTPException,status 
from security.security import Hash

from fastapi import APIRouter,Depends, Response,status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.ext.asyncio import AsyncSession
from utils import token 
from db.databaseConfig import get_session

router = APIRouter(
    prefix="/login",
    tags=["Login"]
)

@router.post('/',
             status_code=status.HTTP_200_OK)
def login(
    # response: Response,
    user_login: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_session),
        #   Authorize: AuthJWT = Depends(),
          ):
    """
    
    user_email: EmailStr = user_login.username.lower()
    user_auth = UserLogin(email= user_email, password= user_login.password)
    auth_token = auth.auth_user(user_auth, db)
    
    """
    # access_token = token.create_access_token({"sub": email})
    # data = {"access_token": access_token, "token_type": "bearer"}
    # return [data] 
    # response.set_cookie('access_token', auth_token["access_token"], 30,
    #                     30, '/', None, False, True, 'lax')
    
    # response.set_cookie('logged_in', 'True', 30,
    #                     30, '/', None, False, False, 'lax')
    return # auth_token