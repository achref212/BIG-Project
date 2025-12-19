from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.subject import Subject
from app.schemas.subject import SubjectCreate, SubjectUpdate, SubjectOut
from app.core.dependencies import get_db, admin_required

router = APIRouter(prefix="/subjects", tags=["Subjects"])

@router.post("", response_model=SubjectOut)
def create(data: SubjectCreate, db: Session = Depends(get_db), _=Depends(admin_required)):
    obj = Subject(**data.dict())
    db.add(obj)
    db.commit()
    return obj

@router.get("", response_model=list[SubjectOut])
def get_all(db: Session = Depends(get_db)):
    return db.query(Subject).all()

@router.put("/{id}", response_model=SubjectOut)
def update(id: int, data: SubjectUpdate, db: Session = Depends(get_db), _=Depends(admin_required)):
    obj = db.query(Subject).get(id)
    for k, v in data.dict(exclude_unset=True).items():
        setattr(obj, k, v)
    db.commit()
    return obj

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db), _=Depends(admin_required)):
    db.delete(db.query(Subject).get(id))
    db.commit()
    return {"deleted": True}
