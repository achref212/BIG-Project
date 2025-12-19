from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.subscription import Plan
from app.core.dependencies import get_db, admin_required
from app.models.user import User
from app.schemas.subscription import PlanOut, PlanCreate

router = APIRouter(prefix="/subscriptions", tags=["Subscriptions"])

@router.post("/plans")
def create_plan(data: dict, db: Session = Depends(get_db), _: User = Depends(admin_required)):
    plan = Plan(**data)
    db.add(plan)
    db.commit()
    return plan

@router.get("/plans")
def list_plans(db: Session = Depends(get_db)):
    return db.query(Plan).all()

@router.delete("/plans/{id}")
def delete_plan(id: int, db: Session = Depends(get_db), _: User = Depends(admin_required)):
    db.delete(db.query(Plan).get(id))
    db.commit()
    return {"deleted": True}
@router.put("/plans/{id}", response_model=PlanOut)
def update_plan(id: int, data: PlanCreate, db: Session = Depends(get_db), _=Depends(admin_required)):
    plan = db.query(Plan).get(id)
    for k, v in data.dict(exclude_unset=True).items():
        setattr(plan, k, v)
    db.commit()
    return plan