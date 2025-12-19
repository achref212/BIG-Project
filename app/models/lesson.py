from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text)

    level_id = Column(Integer, ForeignKey("levels.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))

    level = relationship("Level", back_populates="lessons")
    subject = relationship("Subject", back_populates="lessons")
