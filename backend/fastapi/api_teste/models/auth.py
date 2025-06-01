from models.__init__ import BaseModel
from models.user import UsuarioBase

class SignUpUser(UsuarioBase):
    pass

class SignInUser(BaseModel):
    email: str
    senha: str

class ResetPassword(BaseModel):
    token: str
    new_password: str

class ForgotPassword(BaseModel):
    email: str

class RefreshToken(BaseModel):
    refresh_token: str