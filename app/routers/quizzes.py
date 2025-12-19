from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.quiz import Quiz
from app.schemas.quiz import QuizCreate, QuizUpdate, QuizOut
from app.core.dependencies import get_db, admin_required

router = APIRouter(prefix="/quizzes", tags=["Quizzes"])

@router.post("", response_model=QuizOut)
def create(data: QuizCreate, db: Session = Depends(get_db), _=Depends(admin_required)):
    quiz = Quiz(**data.dict())
    db.add(quiz)
    db.commit()
    return quiz

@router.get("", response_model=list[QuizOut])
def get_all(db: Session = Depends(get_db)):
    return db.query(Quiz).all()

@router.put("/{id}", response_model=QuizOut)
def update(id: int, data: QuizUpdate, db: Session = Depends(get_db), _=Depends(admin_required)):
    quiz = db.query(Quiz).get(id)
    for k, v in data.dict(exclude_unset=True).items():
        setattr(quiz, k, v)
    db.commit()
    return quiz

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db), _=Depends(admin_required)):
    db.delete(db.query(Quiz).get(id))
    db.commit()
    return {"deleted": True}
