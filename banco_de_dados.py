import sqlite3

DB_NAME = "usuarios.db"

def conectar():
    """Cria uma conexão com o banco de dados e retorna o cursor."""
    return sqlite3.connect(DB_NAME)

def criar_tabela():
    """Cria a tabela de usuários se não existir."""
    try:
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(''' 
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    idade INTEGER NOT NULL,
                    cidade TEXT NOT NULL
                )
            ''')
            conexao.commit()
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela: {e}")

def adicionar_usuario(nome, idade, cidade):
    """Adiciona um novo usuário ao banco de dados."""
    try:
        with conectar() as conexao:
            cursor = conexao.cursor()
            print(f"Inserindo usuário: {nome}, {idade}, {cidade}")
            cursor.execute("INSERT INTO usuarios (nome, idade, cidade) VALUES (?, ?, ?)", (nome, idade, cidade))
            conexao.commit()
            print("Usuário adicionado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao adicionar usuário: {e}")


def listar_usuarios():
    """Retorna a lista de usuários cadastrados."""
    try:
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM usuarios")
            return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Erro ao listar usuários: {e}")
        return []

def atualizar_usuario(id_usuario, nome, idade, cidade):
    """Atualiza os dados de um usuário pelo ID."""
    try:
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("UPDATE usuarios SET nome = ?, idade = ?, cidade = ? WHERE id = ?", 
                           (nome, idade, cidade, id_usuario))
            conexao.commit()
    except sqlite3.Error as e:
        print(f"Erro ao atualizar usuário: {e}")

def remover_usuario(id_usuario):
    try:
        with conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
            if cursor.rowcount == 0:
                print(f"Erro: Não existe um usuário com o ID {id_usuario}.")
            else:
                conexao.commit()
                print(f"Usuário com ID {id_usuario} removido com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao remover usuário: {e}")


if __name__ == "__main__":
    criar_tabela()
