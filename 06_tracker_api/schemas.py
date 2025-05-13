from pydantic import BaseModel, EmailStr, constr, validator
from typing import Annotated, Optional
from datetime import date

# Reusable type alias for constrained string
UsernameStr = Annotated[str, constr(min_length=3, max_length=20)]

# -----------------------
# 👤 User Models
# -----------------------

class UserCreate(BaseModel):
    username: UsernameStr
    email: EmailStr

class User(UserCreate):
    id: int

# -----------------------
# ✅ Task Models
# -----------------------

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: date

    @validator("due_date")
    def validate_due_date(cls, v):
        if v < date.today():
            raise ValueError("Due date must be today or later")
        return v

class TaskCreate(TaskBase):
    user_id: int

class Task(TaskBase):
    id: int
    user_id: int
    status: str

    @validator("status")
    def validate_status(cls, v):
        allowed = {"pending", "in_progress", "completed"}
        if v not in allowed:
            raise ValueError(f"Status must be one of: {allowed}")
        return v
