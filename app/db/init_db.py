from app.db.database import conectar_banco

def criar_tabelas():
    """Cria todas as tabelas do banco de dados se não existirem."""
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
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
    conexao.close()
