"""
Security about all the user 
    * Hash and verify the password 
    * Token 
    * Dependency get_user 
    * Dependency get_super_user 
"""

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    """
    class to hash and verify the password 
    """
    def hash_password(password):
        return pwd_context.hash(password)
    
    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)
    

