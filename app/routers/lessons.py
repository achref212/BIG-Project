from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.lesson import Lesson
from app.schemas.lesson import LessonCreate, LessonUpdate, LessonOut
from app.core.dependencies import get_db, admin_required

router = APIRouter(prefix="/lessons", tags=["Lessons"])

@router.post("", response_model=LessonOut)
def create(data: LessonCreate, db: Session = Depends(get_db), _=Depends(admin_required)):
    obj = Lesson(**data.dict())
    db.add(obj)
    db.commit()
    return obj

@router.get("", response_model=list[LessonOut])
def get_all(db: Session = Depends(get_db)):
    return db.query(Lesson).all()

@router.put("/{id}", response_model=LessonOut)
def update(id: int, data: LessonUpdate, db: Session = Depends(get_db), _=Depends(admin_required)):
    obj = db.query(Lesson).get(id)
    for k, v in data.dict(exclude_unset=True).items():
        setattr(obj, k, v)
    db.commit()
    return obj

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db), _=Depends(admin_required)):
    db.delete(db.query(Lesson).get(id))
    db.commit()
    return {"deleted": True}
