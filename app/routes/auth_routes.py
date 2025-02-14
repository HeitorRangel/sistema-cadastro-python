from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.models.usuario_model import UsuarioLogin
from app.services.auth_service import autenticar_usuario, criar_token

router = APIRouter()

@router.post("/login")
def login(usuario: UsuarioLogin):
    usuario_autenticado = autenticar_usuario(usuario.email, usuario.senha)
    if not usuario_autenticado:
        raise HTTPException(status_code=400, detail="Email ou senha incorretos.")
    token = criar_token(usuario_autenticado)
    return {"access_token": token, "token_type": "bearer"}