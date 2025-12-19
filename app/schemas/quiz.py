from pydantic import BaseModel

class QuizBase(BaseModel):
    title: str
    type: str
    difficulty: str
    level_id: int
    subject_id: int

class QuizCreate(QuizBase):
    pass

class QuizUpdate(QuizBase):
    pass

class QuizOut(QuizBase):
    id: int

    class Config:
        orm_mode = True
