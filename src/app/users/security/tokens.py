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
    
"""
<<---------------RSA256----------->>
import time
from jose import jws
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend as crypto_default_backend

key = rsa.generate_private_key(backend=crypto_default_backend(), public_exponent=65537, key_size=2048)
private_key = key.private_bytes(crypto_serialization.Encoding.PEM, crypto_serialization.PrivateFormat.PKCS8, crypto_serialization.NoEncryption())

claims = {
        'iss': 'https://e97b8a9d672e4ce4845ec6947cd66ef6-sb.baas.nintendo.com',
        'sub': 'fdfdc610f849726e',
        'aud': '20c875ad0d4bfc94',
        'iat': time.time() - 20,
        'exp': time.time() + 20,
        'jti': '807443d3-3b27-4bf9-8e3e-e3f90e1ea055',
        'typ': 'id_token'
}

print 'About to sign'
signed = jws.sign(claims, private_key, algorithm='RS256')
print signed

"""