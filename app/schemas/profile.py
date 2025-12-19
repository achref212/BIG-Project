from pydantic import BaseModel
from datetime import date

class ProfileBase(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    birth_date: date | None = None
    country: str | None = None
    avatar_url: str | None = None
    current_level_id: int | None = None

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    pass

class ProfileOut(ProfileBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
