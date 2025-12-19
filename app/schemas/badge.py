from pydantic import BaseModel
from datetime import datetime

class BadgeBase(BaseModel):
    name: str
    code: str
    description: str
    icon_url: str | None = None

class BadgeCreate(BadgeBase):
    pass

class BadgeOut(BadgeBase):
    id: int

    class Config:
        orm_mode = True


class UserBadgeOut(BaseModel):
    id: int
    badge_id: int
    earned_at: datetime

    class Config:
        orm_mode = True
