from routes.__init__ import Annotated, Depends, HTTPException, status, router
from utils.auth_utils import AuthDAO,create_jwt_token, get_current_user, hash_password, verify_hash_password, verify_refresh_token
from models.auth import  SignInUser, SignUpUser, ResetPassword, ForgotPassword, RefreshToken

auth_dao = AuthDAO()

@router.post('/auth/Signin',status_code=status.HTTP_200_OK)
def login(data: SignInUser):
    usuario_existente = auth_dao.buscar_usuario_por_email(data.email)

    if not usuario_existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail= 'Email e/ou senha incorretos(s)!')
    if not verify_hash_password(data.senha, usuario_existente.password_hash):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail= 'Email e/ou senha incorretos(s)!')
    
    acesso_token, token_refresh = create_jwt_token(data.email)

    return {
        'username': usuario_existente.username,
        'token': acesso_token,
        'token_refresh': token_refresh}


@router.post('/auth/Signup', status_code=status.HTTP_201_CREATED)
def signup(data: SignUpUser):
    usuario_existente = auth_dao.buscar_usuario_por_email(data.email)

    if usuario_existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail= f'Já existe um usuário com email {data.email}.')

    data.password_hash = hash_password(data.password_hash)
    usuario = auth_dao.salvar(data)

    return usuario

@router.get('/auth/me', status_code=status.HTTP_200_OK)
def me(user:Annotated[SignUpUser, Depends(get_current_user)]):
    return {
        'username' : user.username,
        'email' : user.email
        }

@router.post("/auth/forgot-password", status_code=status.HTTP_200_OK)
def forgot_password(data: ForgotPassword):
    usuario_existente = auth_dao.buscar_usuario_por_email(data.email)
    if not usuario_existente:
        return None
    reset_token = auth_dao.forgot_password(data)
    if not reset_token:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
    
    return {"message": "Token de redefinição gerado", "reset_token": reset_token}

@router.post("/auth/reset-password", status_code=status.HTTP_200_OK)
def reset_password(data: ResetPassword):
    success = auth_dao.reset_password(data)
    if not success:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Token inválido ou expirado")

    return {"message": "Senha redefinida com sucesso"}


@router.post("/refresh", status_code=status.HTTP_200_OK)
def refresh_token(data: RefreshToken):
    novo_token, novo_token_refresh = verify_refresh_token(data.refresh_token)
    if not novo_token:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Refresh token inválido ou expirado")

    return {"access_token": novo_token, "new_token_refresh": novo_token_refresh, "token_type": "bearer"}