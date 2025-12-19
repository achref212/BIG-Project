from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    role: str

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    role: str | None = None
    is_active: bool | None = None

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
