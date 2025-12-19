from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Text,
    Boolean
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    type = Column(String(20), nullable=False)  # quiz / exercise
    difficulty = Column(String(20), nullable=True)

    level_id = Column(Integer, ForeignKey("levels.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    level = relationship("Level", back_populates="quizzes")
    subject = relationship("Subject", back_populates="quizzes")
    questions = relationship(
        "Question",
        back_populates="quiz",
        cascade="all, delete-orphan"
    )


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"), nullable=False)

    question_type = Column(String(30), nullable=False)
    statement = Column(Text, nullable=False)
    extra_data = Column(Text, nullable=True)
    explanation = Column(Text, nullable=True)
    order_index = Column(Integer, nullable=True)

    quiz = relationship("Quiz", back_populates="questions")
    choices = relationship(
        "QuestionChoice",
        back_populates="question",
        cascade="all, delete-orphan"
    )


class QuestionChoice(Base):
    __tablename__ = "question_choices"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)

    label = Column(String(255), nullable=False)
    is_correct = Column(Boolean, default=False)

    question = relationship("Question", back_populates="choices")
