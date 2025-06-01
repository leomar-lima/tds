from models.__init__ import BaseModel

class UsuarioBase(BaseModel):
    username: str
    email: str
    password_hash: str

class Usuario(UsuarioBase):
    id: int | None = None

class UsuarioCreate(UsuarioBase):
    pass

