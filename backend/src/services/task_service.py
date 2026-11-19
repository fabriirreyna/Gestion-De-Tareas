from src.schemas.task import TaskCreate, TaskResponse

# Base de datos temporal en memoria
fake_tasks_db: list[dict] = []

def get_all_tasks() -> list[dict]:
    return fake_tasks_db

def create_task(task_data: TaskCreate) -> dict:
    new_task = task_data.model_dump()
    new_task["id"] = len(fake_tasks_db) + 1
    fake_tasks_db.append(new_task)
    return new_task