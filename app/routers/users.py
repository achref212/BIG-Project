from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserOut, UserUpdate
from app.core.dependencies import get_db, get_current_user, admin_required

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me", response_model=UserOut)
def me(user = Depends(get_current_user)):
    return user

@router.get("", response_model=list[UserOut])
def get_all(db: Session = Depends(get_db), _=Depends(admin_required)):
    return db.query(User).all()

@router.put("/{user_id}", response_model=UserOut)
def update_user(
    user_id: int,
    data: UserUpdate,
    db: Session = Depends(get_db),
    _=Depends(admin_required)
):
    user = db.query(User).get(user_id)
    for k, v in data.dict(exclude_unset=True).items():
        setattr(user, k, v)
    db.commit()
    return user

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), _=Depends(admin_required)):
    db.delete(db.query(User).get(user_id))
    db.commit()
    return {"deleted": True}
