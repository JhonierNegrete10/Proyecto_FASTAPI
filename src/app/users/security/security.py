"""
Security about all the user 
    * Hash and verify the password 
    * Token 
    * Dependency get_user 
    * Dependency get_super_user 
"""
from fastapi_permissions import (
    Allow,
    Authenticated,
    Deny,
    Everyone,
    configure_permissions,
    list_permissions,
) 
from fastapi import Request, Depends,HTTPException,status 
from fastapi.security import (
OAuth2PasswordBearer, 
OAuth2PasswordRequestForm,
SecurityScopes
)

from users.models.userModel import UserDB
from security.token import TokenData, verify_token

from passlib.context import CryptContext

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login",
    scopes={"me": "Read information about the current user.", 
            # "items": "Read items."
            })


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    """
    class to hash and verify the password 
    """
    def hash_password(password):
        return pwd_context.hash(password)
    
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)
    
    
def get_current_user(request:Request, token: str = Depends(oauth2_scheme)):
    """
    get current user 
    """    
    if not token:
        return None 
    else:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return verify_token(token,credentials_exception)


def get_current_user_only( token: str = Depends(oauth2_scheme)):
    """
    get current user 
    """    
    if not token:
        return None 
    else:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    """
    security_scopes.scopes
    # TODO: investigate Security Scopes from fastapi
    """
    return verify_token(token,credentials_exception)


def get_active_principals(current_user: TokenData = Depends(get_current_user)):
    
    if user:
        # user is logged in
        principals = [Everyone, Authenticated]
        principals.extend(getattr(user, "principals", []))
    else:
        # user is not logged in
        principals = [Everyone]
    return principals