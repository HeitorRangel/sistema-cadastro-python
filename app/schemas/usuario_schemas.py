from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    nome: str
    idade: int
    cidade: str

    class Config:
        schema_extra = {
            "example": {
                "nome": "João Silva",
                "idade": 30,
                "cidade": "São Paulo"
            }
        }