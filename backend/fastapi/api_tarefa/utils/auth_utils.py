from datetime import datetime, timezone, timedelta
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from passlib.context import CryptContext
from repositories.authDAO import AuthDAO

auth_dao = AuthDAO()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_hash_password(password:str, hash_pw:str):
    return pwd_context.verify(password, hash_pw)

SECRET_KEY = "Backend"
ALGORITHM = "HS256"

def create_jwt_token(email:str):
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    data ={
        'sub': email,
        'exp': expire
    }
    token = jwt.encode(data, SECRET_KEY, ALGORITHM)
    token_refresh = create_refresh_token(email)
    return token, token_refresh

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: Annotated[str, Depends(oauth_scheme)]):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        email = data['sub']
        user = auth_dao.buscar_usuario_por_email(email)
        return user
    except:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail= "Token inválido ou expirado."
        )


def create_refresh_token(email: str):
    expire =datetime.now(timezone.utc) + timedelta(days=7)
    data = {'sub': email, 'exp': expire}
    return jwt.encode(data, SECRET_KEY, ALGORITHM)

def verify_refresh_token(refresh_token: str):
    try:
        data = jwt.decode(refresh_token, SECRET_KEY, algorithms=ALGORITHM)
        email = data.get("sub")
        user = auth_dao.buscar_usuario_por_email(email)
        if user:
            return create_jwt_token(email)
    except:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail= "Token inválido ou expirado."
        )
