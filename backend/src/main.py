from fastapi import FastAPI
from src.routers import tasks

app = FastAPI(
    title="Task Manager API",
    description="API REST para gestión de usuarios, proyectos y tareas",
    version="0.1.0"
)

app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a Task Manager API", "status": "online"}