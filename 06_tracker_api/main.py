from fastapi import FastAPI, HTTPException
from typing import List
from schemas import UserCreate, User, TaskCreate, Task
from storage import USERS, TASKS

app = FastAPI()

# IDs as module-level state
import storage
user_id_seq = storage.user_id_seq
task_id_seq = storage.task_id_seq

# ---- User Endpoints ----

@app.post("/users/", response_model=User)
def create_user(user: UserCreate):
    global user_id_seq
    for u in USERS.values():
        if u.email == user.email:
            raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(id=user_id_seq, **user.dict())
    USERS[user_id_seq] = new_user
    user_id_seq += 1
    return new_user

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# ---- Task Endpoints ----

@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    global task_id_seq
    if task.user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    new_task = Task(id=task_id_seq, status="pending", **task.dict())
    TASKS[task_id_seq] = new_task
    task_id_seq += 1
    return new_task

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task_status(task_id: int, status: str):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if status not in {"pending", "in_progress", "completed"}:
        raise HTTPException(status_code=400, detail="Invalid status")
    task.status = status
    return task

@app.get("/users/{user_id}/tasks", response_model=List[Task])
def list_user_tasks(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")
    return [t for t in TASKS.values() if t.user_id == user_id]
