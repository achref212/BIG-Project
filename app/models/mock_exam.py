from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class MockExam(Base):
    __tablename__ = "mock_exams"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(500))
    level_id = Column(Integer, ForeignKey("levels.id"))

    level = relationship("Level", back_populates="mock_exams")
    parts = relationship("MockExamPart", back_populates="mock_exam")


class MockExamPart(Base):
    __tablename__ = "mock_exam_parts"

    id = Column(Integer, primary_key=True)
    mock_exam_id = Column(Integer, ForeignKey("mock_exams.id"))
    part_type = Column(String(50))
    instructions = Column(Text)
    order_index = Column(Integer)

    mock_exam = relationship("MockExam", back_populates="parts")
