import pandas as pd
from sqlite3 import Connection

def exportar_usuarios_csv(db: Connection, nome_arquivo: str = "usuarios.csv"):
    df = pd.read_sql("SELECT * FROM usuarios", db)
    df.to_csv(nome_arquivo, index=False)
    return nome_arquivo

def importar_usuarios_csv(db: Connection, nome_arquivo: str = "usuarios.csv"):
    df = pd.read_csv(nome_arquivo)
    df.to_sql("usuarios", db, if_exists="append", index=False)
    return len(df)