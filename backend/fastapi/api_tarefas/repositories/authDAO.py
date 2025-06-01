import sqlite3
from repositories.__init__ import Usuario, SignUpUser, DB , ForgotPassword, ResetPassword
from datetime import datetime, timezone, timedelta
import secrets

class AuthDAO():
    def __init__(self):
        pass

    def buscar_usuario_por_email(self, email:str):
        with sqlite3.connect(DB) as c:
            cursor = c.cursor()
            sql = 'SELECT * FROM Usuario WHERE email = ?'
            cursor.execute(sql, (email,))
            resultado = cursor.fetchone()

            if not resultado:
                return None
            
            usuario = Usuario(id=resultado[0],
                            username=resultado[1],
                            email=resultado[2],
                            password_hash=resultado[3])
            
            return usuario
        
    def salvar(self, usuario: SignUpUser):
        with sqlite3.connect(DB) as c:
            cursor = c.cursor()

            sql = '''INSERT INTO Usuario(username, email, senha)
                    VALUES (?, ?, ? )'''
            
            cursor.execute(sql, (usuario.username, usuario.email, usuario.password_hash))

            id = cursor.lastrowid

            return Usuario(id=id, **usuario.dict())
  
            return reset_token
    def forgot_password(self, request: ForgotPassword):
        with sqlite3.connect(DB) as c:
            cursor = c.cursor()
            sql = 'UPDATE Usuario SET reset_token = ?, expire_token = ? WHERE email = ?'
            reset_token = secrets.token_hex(16)
            expire = datetime.now(timezone.utc) + timedelta(minutes=5)
            cursor.execute(sql,(reset_token, expire, request.email))

            return reset_token

        
    def reset_password(self, request: ResetPassword):
        from utils.auth_utils import hash_password
        with sqlite3.connect(DB) as c:
            cursor = c.cursor()
            sql = 'SELECT id FROM Usuario WHERE reset_token = ? AND expire_token > ?'
            cursor.execute(sql, (request.token, datetime.now(timezone.utc)))
            resultado = cursor.fetchone()

            if not resultado:
                return None
            
            sql = 'UPDATE Usuario SET senha = ?, reset_token = NULL, expire_token = NULL WHERE id = ?'
            cursor.execute(sql, (hash_password(request.new_password), resultado[0]))

        return True