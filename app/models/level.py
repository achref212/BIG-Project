from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Level(Base):
    __tablename__ = "levels"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    code = Column(String(10), nullable=False, unique=True)
    order_index = Column(Integer, nullable=False)

    lessons = relationship("Lesson", back_populates="level")
    quizzes = relationship("Quiz", back_populates="level")
    stories = relationship("Story", back_populates="level")
    mock_exams = relationship("MockExam", back_populates="level")
