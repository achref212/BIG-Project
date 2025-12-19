from pydantic import BaseModel
from datetime import date

class PlanBase(BaseModel):
    name: str
    price_monthly: int
    price_yearly: int
    features_json: str

class PlanCreate(PlanBase):
    pass

class PlanOut(PlanBase):
    id: int

    class Config:
        orm_mode = True


class SubscriptionOut(BaseModel):
    id: int
    user_id: int
    plan_id: int
    status: str
    start_date: date
    end_date: date

    class Config:
        orm_mode = True
