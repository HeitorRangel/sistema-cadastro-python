from sqlite3 import Connection, IntegrityError
from app.models.usuario_model import Usuario

class UsuarioRepository:
    def __init__(self, db: Connection):
        self.db = db

    def criar_usuario(self, usuario):
        """Adiciona um novo usuário ao banco de dados."""
        try:
            cursor = self.db.cursor()
            cursor.execute(
                "INSERT INTO usuarios (nome, idade, cidade) VALUES (?, ?, ?)",
                (usuario.nome, usuario.idade, usuario.cidade)
            )
            self.db.commit()
            return cursor.lastrowid
        except IntegrityError as e:
            print(f"Erro ao adicionar usuário: {e}")
            return None  # Retorna None em caso de duplicação

    def listar_usuarios(self):
        """Retorna a lista de usuários cadastrados."""
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()
        # Converte as tuplas em dicionários
        usuarios = [
            {"id": row[0], "nome": row[1], "idade": row[2], "cidade": row[3]}
            for row in rows
        ]
        return usuarios

    def usuario_existe(self, id: int):
        """Verifica se um usuário com o ID especificado existe."""
        cursor = self.db.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE id = ?", (id,))
        return cursor.fetchone() is not None

    def atualizar_usuario(self, id: int, usuario: Usuario):
        """Atualiza os dados de um usuário pelo ID."""
        if not self.usuario_existe(id):
            raise ValueError(f"Usuário com ID {id} não encontrado.")
        
        cursor = self.db.cursor()
        cursor.execute(
            "UPDATE usuarios SET nome = ?, idade = ?, cidade = ? WHERE id = ?",
            (usuario.nome, usuario.idade, usuario.cidade, id)
        )
        self.db.commit()

    def remover_usuario(self, id: int):
        """Remove um usuário pelo ID."""
        if not self.usuario_existe(id):
            raise ValueError(f"Usuário com ID {id} não encontrado.")
        
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
        self.db.commit()