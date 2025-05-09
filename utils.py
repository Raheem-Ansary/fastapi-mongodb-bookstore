from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "9b3a1f2e78e21bc6adadf3d95e2e0cc4f5dfce158e93b7398e5dc8638b2b6de7"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed):
    return pwd_context.verify(plain_password, hashed)

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=1)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
