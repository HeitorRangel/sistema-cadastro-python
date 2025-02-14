import sqlite3
from sqlite3 import Connection
from typing import List, Tuple, Optional

DATABASE_URL = "usuarios.db"

def conectar_banco() -> Connection:
    """Retorna uma conexão com o banco de dados SQLite."""
    return sqlite3.connect(DATABASE_URL)

def adicionar_usuario(nome: str, idade: int, cidade: str, estado: str, genero: Optional[str], renda_mensal: Optional[float], profissao: Optional[str], nivel_escolaridade: Optional[str]):
    """Adiciona um novo usuário ao banco de dados."""
    with conectar_banco() as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO usuarios (nome, idade, cidade, estado, genero, renda_mensal, profissao, nivel_escolaridade)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (nome, idade, cidade, estado, genero, renda_mensal, profissao, nivel_escolaridade))
        conexao.commit()

def listar_usuarios() -> List[Tuple]:
    """Lista todos os usuários cadastrados."""
    with conectar_banco() as conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM usuarios')
        return cursor.fetchall()

def registrar_compra(id_usuario: int, valor: float, categoria: str):
    """Registra uma compra para um usuário específico."""
    with conectar_banco() as conexao:
        cursor = conexao.cursor()
        cursor.execute('''
            INSERT INTO compras (id_usuario, valor, categoria)
            VALUES (?, ?, ?)
        ''', (id_usuario, valor, categoria))
        conexao.commit()

def listar_compras() -> List[Tuple]:
    """Lista todas as compras registradas no banco de dados."""
    with conectar_banco() as conexao:
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM compras')
        return cursor.fetchall()
