from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(500))

    level_id = Column(Integer, ForeignKey("levels.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))

    content_html = Column(Text)
    estimated_duration_minutes = Column(Integer)
    is_published = Column(Boolean, default=False)

    level = relationship("Level", back_populates="lessons")
    subject = relationship("Subject", back_populates="lessons")
