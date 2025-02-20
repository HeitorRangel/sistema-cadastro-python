import sqlite3
from sqlite3 import Connection

DATABASE_URL = "usuarios.db"

def conectar_banco() -> Connection:
    """Abre uma conexão com o banco de dados SQLite."""
    return sqlite3.connect(DATABASE_URL)

def criar_tabelas():
    """Cria as tabelas do banco de dados se não existirem."""
    with conectar_banco() as conexao:
        cursor = conexao.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                cidade TEXT NOT NULL,
                estado TEXT NOT NULL,
                genero TEXT,
                data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                renda_mensal FLOAT,
                profissao TEXT,
                nivel_escolaridade TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS compras (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER,
                data_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                valor FLOAT NOT NULL,
                categoria TEXT NOT NULL,
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE
            )
        ''')
        
        conexao.commit()

if __name__ == "__main__":
    criar_tabelas()
    print("Tabelas criadas com sucesso!")
