from sqlite3 import connect, Connection

DATABASE_URL = "usuarios.db"

def get_db_connection() -> Connection:
    """Retorna uma conexão com o banco de dados SQLite."""
    return connect(DATABASE_URL)

def criar_tabela():
    """Cria a tabela de usuários se não existir."""
    try:
        with get_db_connection() as conexao:
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
    except Exception as e:
        print(f"Erro ao criar tabela: {e}")