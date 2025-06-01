from fastapi import FastAPI
from routes.auth_routes import router as roteador_auth
from routes.task_routes import router as roteador_task


app = FastAPI()


# Rotas de Autenticaco
app.include_router(roteador_auth)

# Rotas de Tarefas
app.include_router(roteador_task)

@app.get("/")
def home():
    return {"message": "API Tarefas ativa!"}