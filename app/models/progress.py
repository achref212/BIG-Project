from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class UserProgress(Base):
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    xp_points = Column(Integer, default=0)
    lessons_completed = Column(Integer, default=0)
    quizzes_completed = Column(Integer, default=0)

    last_activity_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="progress")
