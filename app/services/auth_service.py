from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status

# Configurações para JWT
SECRET_KEY = "chaveTeste"  # Substitua por uma chave segura em produção
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Configurações para criptografia de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função para verificar a senha
def verificar_senha(senha_plana: str, senha_criptografada: str):
    return pwd_context.verify(senha_plana, senha_criptografada)

# Função para criptografar a senha
def criptografar_senha(senha: str):
    return pwd_context.hash(senha)

# Função para autenticar o usuário
def autenticar_usuario(email: str, senha: str):
    # Aqui você deve buscar o usuário no banco de dados
    # Exemplo fictício:
    usuario_admin = {
        "email": "hadmin@gmail.com",
        "senha": criptografar_senha("chaveTeste"),  # Senha criptografada
        "nome": "Admin"
    }

    # Verifique se o usuário existe e se a senha está correta
    if email != usuario_admin["email"] or not verificar_senha(senha, usuario_admin["senha"]):
        return None

    return usuario_admin

# Função para criar o token JWT
def criar_token(usuario: dict):
    dados = {
        "sub": usuario["email"],  # Subject (geralmente o email ou ID do usuário)
        "nome": usuario["nome"],
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    token = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Função para validar o token JWT
def validar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )