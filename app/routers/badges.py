from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.badge import Badge
from app.models.user import User
from app.core.dependencies import get_db, admin_required
from app.schemas.badge import BadgeCreate, BadgeOut

router = APIRouter(prefix="/badges", tags=["Badges"])

@router.post("/", response_model=BadgeOut)
def create_badge(
    data: BadgeCreate,
    db: Session = Depends(get_db),
    _: User = Depends(admin_required)
):
    badge = Badge(**data.model_dump())
    db.add(badge)
    db.commit()
    db.refresh(badge)
    return badge

@router.get("")
def get_all(db: Session = Depends(get_db)):
    return db.query(Badge).all()

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db), _: User = Depends(admin_required)):
    db.delete(db.query(Badge).get(id))
    db.commit()
    return {"deleted": True}
@router.put("/{id}", response_model=BadgeOut)
def update(id: int, data: BadgeCreate, db: Session = Depends(get_db), _=Depends(admin_required)):
    obj = db.query(Badge).get(id)
    for k, v in data.dict(exclude_unset=True).items():
        setattr(obj, k, v)
    db.commit()
    return obj