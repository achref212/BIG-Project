from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.story import Story
from app.schemas.story import StoryCreate, StoryUpdate, StoryOut
from app.core.dependencies import get_db, admin_required

router = APIRouter(prefix="/stories", tags=["Stories"])

@router.post("", response_model=StoryOut)
def create(data: StoryCreate, db: Session = Depends(get_db), _=Depends(admin_required)):
    obj = Story(**data.dict())
    db.add(obj)
    db.commit()
    return obj

@router.get("", response_model=list[StoryOut])
def get_all(db: Session = Depends(get_db)):
    return db.query(Story).all()

@router.put("/{id}", response_model=StoryOut)
def update(id: int, data: StoryUpdate, db: Session = Depends(get_db), _=Depends(admin_required)):
    obj = db.query(Story).get(id)
    for k, v in data.dict(exclude_unset=True).items():
        setattr(obj, k, v)
    db.commit()
    return obj

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db), _=Depends(admin_required)):
    db.delete(db.query(Story).get(id))
    db.commit()
    return {"deleted": True}
