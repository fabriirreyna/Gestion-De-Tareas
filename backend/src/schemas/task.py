from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    DONE = "done"

class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

# Esquema para crear una tarea
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100, examples=["Implementar login"])
    description: Optional[str] = Field(None, max_length=500)
    status: TaskStatus = TaskStatus.PENDING
    priority: TaskPriority = TaskPriority.MEDIUM

# Esquema para devolver una tarea
class TaskResponse(TaskCreate):
    id: int