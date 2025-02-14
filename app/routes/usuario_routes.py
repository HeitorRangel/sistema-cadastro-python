from fastapi import APIRouter, Depends, HTTPException
from sqlite3 import Connection
from app.services.usuario_service import UsuarioService
from app.repositories.usuario_repository import UsuarioRepository
from app.models.usuario_model import UsuarioCreate, Usuario
from app.db.database import get_db_connection
from app.dependencies import obter_usuario_atual

router = APIRouter()

# Endpoint para criar usuário (não requer autenticação)
@router.post("/", response_model=Usuario)
def criar_usuario(usuario: UsuarioCreate, db: Connection = Depends(get_db_connection)):
    repository = UsuarioRepository(db)
    service = UsuarioService(repository)
    usuario_id = service.criar_usuario(usuario)
    return {**usuario.dict(), "id": usuario_id}

# Endpoint para listar usuários (protegido por autenticação JWT)
@router.get("/", response_model=list[Usuario])
def listar_usuarios(db: Connection = Depends(get_db_connection), usuario_atual: dict = Depends(obter_usuario_atual)):
    repository = UsuarioRepository(db)
    service = UsuarioService(repository)
    usuarios = service.listar_usuarios()
    return usuarios

# Endpoint para atualizar usuário (protegido por autenticação JWT)
@router.put("/{id}", response_model=Usuario)
def atualizar_usuario(id: int, usuario: UsuarioCreate, db: Connection = Depends(get_db_connection), usuario_atual: dict = Depends(obter_usuario_atual)):
    repository = UsuarioRepository(db)
    service = UsuarioService(repository)
    service.atualizar_usuario(id, usuario)
    return {**usuario.dict(), "id": id}

# Endpoint para remover usuário (protegido por autenticação JWT)
@router.delete("/{id}")
def remover_usuario(id: int, db: Connection = Depends(get_db_connection), usuario_atual: dict = Depends(obter_usuario_atual)):
    repository = UsuarioRepository(db)
    service = UsuarioService(repository)
    service.remover_usuario(id)
    return {"message": "Usuário removido com sucesso"}