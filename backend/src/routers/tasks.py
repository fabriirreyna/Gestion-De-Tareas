from fastapi import APIRouter, status
from src.schemas.task import TaskCreate, TaskResponse
from src.services import task_service

router = APIRouter(prefix="/api/tasks", tags=["Tasks"])

@router.get("/", response_model=list[TaskResponse])
def list_tasks():
    return task_service.get_all_tasks()

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def add_task(task: TaskCreate):
    return task_service.create_task(task)