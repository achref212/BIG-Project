from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class MockExam(Base):
    __tablename__ = "mock_exams"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)

    level_id = Column(Integer, ForeignKey("levels.id"))

    level = relationship("Level", back_populates="mock_exams")
    parts = relationship("MockExamPart", back_populates="mock_exam", cascade="all, delete-orphan")


class MockExamPart(Base):
    __tablename__ = "mock_exam_parts"

    id = Column(Integer, primary_key=True, index=True)
    mock_exam_id = Column(Integer, ForeignKey("mock_exams.id"))

    part_type = Column(String(50))
    instructions = Column(Text)

    mock_exam = relationship("MockExam", back_populates="parts")
