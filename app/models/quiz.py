from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    type = Column(String(20))  # quiz / exercise
    difficulty = Column(String(20))

    level_id = Column(Integer, ForeignKey("levels.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    level = relationship("Level", back_populates="quizzes")
    subject = relationship("Subject", back_populates="quizzes")
    questions = relationship("Question", back_populates="quiz")

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    question_type = Column(String(30))
    statement = Column(Text)
    extra_data = Column(Text)
    explanation = Column(Text)
    order_index = Column(Integer)

    quiz = relationship("Quiz", back_populates="questions")
    choices = relationship("QuestionChoice", back_populates="question")


class QuestionChoice(Base):
    __tablename__ = "question_choices"

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    label = Column(String(255))
    is_correct = Column(Boolean)

    question = relationship("Question", back_populates="choices")
