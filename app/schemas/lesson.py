from pydantic import BaseModel

class LessonBase(BaseModel):
    title: str
    description: str | None = None
    level_id: int
    subject_id: int
    content_html: str | None = None
    estimated_duration_minutes: int | None = None
    is_published: bool = False

class LessonCreate(LessonBase):
    pass

class LessonUpdate(LessonBase):
    pass

class LessonOut(LessonBase):
    id: int

    class Config:
        orm_mode = True
