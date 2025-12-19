from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Text
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class MockExam(Base):
    __tablename__ = "mock_exams"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

    level_id = Column(Integer, ForeignKey("levels.id"), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    parts = relationship(
        "MockExamPart",
        back_populates="mock_exam",
        cascade="all, delete-orphan"
    )


class MockExamPart(Base):
    __tablename__ = "mock_exam_parts"

    id = Column(Integer, primary_key=True, index=True)
    mock_exam_id = Column(Integer, ForeignKey("mock_exams.id"), nullable=False)

    part_type = Column(String(50), nullable=False)
    instructions = Column(Text, nullable=False)
    order_index = Column(Integer, nullable=True)

    mock_exam = relationship("MockExam", back_populates="parts")
