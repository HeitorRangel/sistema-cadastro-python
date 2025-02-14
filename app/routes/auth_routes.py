from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.services.auth_service import autenticar_usuario, criar_token
from app.models.usuario_model import UsuarioLogin

router = APIRouter()

@router.post("/login")
def login(usuario: UsuarioLogin):
    # Autentica o usuário
    usuario_autenticado = autenticar_usuario(usuario.email, usuario.senha)
    if not usuario_autenticado:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Gera o token JWT
    token = criar_token(usuario_autenticado)
    return {"access_token": token, "token_type": "bearer"}