from pydantic import BaseModel
from datetime import datetime

class ProgressOut(BaseModel):
    id: int
    user_id: int
    level_id: int
    xp_points: int
    lessons_completed: int
    quizzes_completed: int
    mock_exams_completed: int
    last_activity_at: datetime

    class Config:
        orm_mode = True
