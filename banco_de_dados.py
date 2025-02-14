import pandas as pd
import sqlite3

DB_NAME = "usuarios.db"

def exportar_usuarios_csv(nome_arquivo="usuarios.csv"):
    """Exporta os usuários do banco de dados para um arquivo CSV."""
    try:
        with sqlite3.connect(DB_NAME) as conexao:
            df = pd.read_sql("SELECT * FROM usuarios", conexao)
            df.to_csv(nome_arquivo, index=False)
        print(f"Dados exportados com sucesso para {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao exportar usuários: {e}")

def importar_usuarios_csv(nome_arquivo="usuarios.csv"):
    """Importa usuários de um arquivo CSV para o banco de dados."""
    try:
        df = pd.read_csv(nome_arquivo)
        with sqlite3.connect(DB_NAME) as conexao:
            df.to_sql("usuarios", conexao, if_exists="append", index=False)
        print(f"Dados importados com sucesso do {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao importar usuários: {e}")

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
                return False  # Retorna False se nenhum usuário foi removido
            else:
                conexao.commit()
                print(f"Usuário com ID {id_usuario} removido com sucesso!")
                return True  # Retorna True se a remoção foi bem-sucedida
    except sqlite3.Error as e:
        print(f"Erro ao remover usuário: {e}")
        return False



if __name__ == "__main__":
    criar_tabela()
