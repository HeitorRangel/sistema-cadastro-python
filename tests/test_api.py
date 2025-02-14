import requests

# Função para fazer login e obter o token JWT
def fazer_login():
    url = "http://localhost:8000/auth/login"
    dados_login = {
        "email": "hadmin@gmail.com",
        "senha": "chaveTeste"
    }
    response = requests.post(url, json=dados_login)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print("Erro ao fazer login:", response.json())
        return None

# Função para listar usuários
def listar_usuarios(token):
    url = "http://localhost:8000/usuarios/"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao listar usuários:", response.json())
        return None

# Função para atualizar um usuário
def atualizar_usuario(token, usuario_id, dados):
    url = f"http://localhost:8000/usuarios/{usuario_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.put(url, json=dados, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao atualizar usuário:", response.json())
        return None

# Função para remover um usuário
def remover_usuario(token, usuario_id):
    url = f"http://localhost:8000/usuarios/{usuario_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao remover usuário:", response.json())
        return None

# Executa as funções
if __name__ == "__main__":
    # Faz login e obtém o token
    token = fazer_login()
    if token:
        print("Token JWT recebido:", token)

        # Lista os usuários
        usuarios = listar_usuarios(token)
        if usuarios:
            print("Usuários cadastrados:", usuarios)

        # Atualiza um usuário
        dados_atualizacao = {
            "nome": "Usuário Atualizado",
            "idade": 30,
            "cidade": "Rio de Janeiro"
        }
        usuario_atualizado = atualizar_usuario(token, 1, dados_atualizacao)
        if usuario_atualizado:
            print("Usuário atualizado:", usuario_atualizado)

        # Remove um usuário
        resposta_remocao = remover_usuario(token, 1)
        if resposta_remocao:
            print("Resposta da remoção:", resposta_remocao)