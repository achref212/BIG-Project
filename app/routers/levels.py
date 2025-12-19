from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.level import Level
from app.schemas.level import LevelCreate, LevelUpdate, LevelOut
from app.core.dependencies import get_db, admin_required

router = APIRouter(prefix="/levels", tags=["Levels"])

@router.post("", response_model=LevelOut)
def create(data: LevelCreate, db: Session = Depends(get_db), _=Depends(admin_required)):
    level = Level(**data.dict())
    db.add(level)
    db.commit()
    return level

@router.get("", response_model=list[LevelOut])
def get_all(db: Session = Depends(get_db)):
    return db.query(Level).all()

@router.get("/{id}", response_model=LevelOut)
def get_one(id: int, db: Session = Depends(get_db)):
    return db.query(Level).get(id)

@router.put("/{id}", response_model=LevelOut)
def update(id: int, data: LevelUpdate, db: Session = Depends(get_db), _=Depends(admin_required)):
    level = db.query(Level).get(id)
    for k, v in data.dict(exclude_unset=True).items():
        setattr(level, k, v)
    db.commit()
    return level

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db), _=Depends(admin_required)):
    db.delete(db.query(Level).get(id))
    db.commit()
    return {"deleted": True}
