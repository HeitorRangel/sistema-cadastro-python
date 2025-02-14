from fastapi import APIRouter, Depends, HTTPException
from sqlite3 import Connection
from app.services.usuario_service import UsuarioService
from app.repositories.usuario_repository import UsuarioRepository
from app.models.usuario_model import UsuarioCreate, Usuario
from app.db.database import get_db_connection

router = APIRouter()

@router.post("/", response_model=Usuario)
def criar_usuario(usuario: UsuarioCreate, db: Connection = Depends(get_db_connection)):
    repository = UsuarioRepository(db)
    service = UsuarioService(repository)
    usuario_id = service.criar_usuario(usuario)
    return {**usuario.dict(), "id": usuario_id}

@router.get("/", response_model=list[Usuario])  # Use o modelo na resposta
def listar_usuarios(db: Connection = Depends(get_db_connection)):
    repository = UsuarioRepository(db)
    service = UsuarioService(repository)
    return service.listar_usuarios()

@router.put("/{id}", response_model=Usuario)
def atualizar_usuario(id: int, usuario: UsuarioCreate, db: Connection = Depends(get_db_connection)):
    repository = UsuarioRepository(db)
    service = UsuarioService(repository)
    service.atualizar_usuario(id, usuario)
    return {**usuario.dict(), "id": id}

@router.delete("/{id}")
def remover_usuario(id: int, db: Connection = Depends(get_db_connection)):
    repository = UsuarioRepository(db)
    service = UsuarioService(repository)
    service.remover_usuario(id)
    return {"message": "Usuário removido com sucesso"}