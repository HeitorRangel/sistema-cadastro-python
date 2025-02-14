import requests

BASE_URL = "http://localhost:8000"

def test_criar_usuario():
    response = requests.post(
        f"{BASE_URL}/usuarios/",
        json={"nome": "Teste", "idade": 25, "cidade": "Testelandia"}
    )
    assert response.status_code == 200
    assert "id" in response.json()

def test_listar_usuarios():
    response = requests.get(f"{BASE_URL}/usuarios/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)