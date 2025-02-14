from app.repositories.usuario_repository import UsuarioRepository
from app.models.usuario_model import Usuario

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, usuario):
        usuario_id = self.repository.criar_usuario(usuario)
        if usuario_id is None:
            raise ValueError("Usuário já existe no banco de dados.")
        return usuario_id
        
        usuario_id = self.repository.criar_usuario(usuario)
        if usuario_id is None:
            raise ValueError("Usuário já existe no banco de dados.")
        return usuario_id

    def listar_usuarios(self):
        return self.repository.listar_usuarios()

    def atualizar_usuario(self, id: int, usuario: Usuario):
        if not self.repository.usuario_existe(id):
            raise ValueError(f"Usuário com ID {id} não encontrado.")
        return self.repository.atualizar_usuario(id, usuario)

    def remover_usuario(self, id: int):
        if not self.repository.usuario_existe(id):
            raise ValueError(f"Usuário com ID {id} não encontrado.")
        return self.repository.remover_usuario(id)