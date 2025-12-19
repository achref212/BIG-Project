from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.mock_exam import MockExam
from app.schemas.mock_exam import MockExamCreate, MockExamUpdate, MockExamOut
from app.core.dependencies import get_db, admin_required

router = APIRouter(prefix="/mock-exams", tags=["Mock Exams"])

@router.post("", response_model=MockExamOut)
def create(data: MockExamCreate, db: Session = Depends(get_db), _=Depends(admin_required)):
    obj = MockExam(**data.dict())
    db.add(obj)
    db.commit()
    return obj

@router.get("", response_model=list[MockExamOut])
def get_all(db: Session = Depends(get_db)):
    return db.query(MockExam).all()

@router.put("/{id}", response_model=MockExamOut)
def update(id: int, data: MockExamUpdate, db: Session = Depends(get_db), _=Depends(admin_required)):
    obj = db.query(MockExam).get(id)
    for k, v in data.dict(exclude_unset=True).items():
        setattr(obj, k, v)
    db.commit()
    return obj

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db), _=Depends(admin_required)):
    db.delete(db.query(MockExam).get(id))
    db.commit()
    return {"deleted": True}
