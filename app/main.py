from fastapi import FastAPI
from app.routes.usuario_routes import router as usuario_router
from app.routes.auth_routes import router as auth_router
from app.db.init_db import criar_tabelas  # Importando a função de inicialização

app = FastAPI(
    title="Sistema de Cadastro de Usuários",
    description="API para gerenciar usuários com operações CRUD e importação/exportação de CSV.",
    version="1.0.0"
)

# Evento de startup para criar as tabelas ao iniciar a API
@app.on_event("startup")
def startup():
    criar_tabelas()

# Inclui as rotas da API
app.include_router(usuario_router, prefix="/usuarios", tags=["usuarios"])
app.include_router(auth_router, prefix="/auth", tags=["autenticação"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
