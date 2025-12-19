from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    type = Column(String(20))  # quiz / exercise
    difficulty = Column(String(20))

    level_id = Column(Integer, ForeignKey("levels.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))

    level = relationship("Level", back_populates="quizzes")
    subject = relationship("Subject", back_populates="quizzes")
    questions = relationship("Question", back_populates="quiz", cascade="all, delete-orphan")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))

    question_type = Column(String(50))
    statement = Column(Text)
    explanation = Column(Text)

    quiz = relationship("Quiz", back_populates="questions")
    choices = relationship("QuestionChoice", back_populates="question", cascade="all, delete-orphan")


class QuestionChoice(Base):
    __tablename__ = "question_choices"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer, ForeignKey("questions.id"))

    label = Column(String(255))
    is_correct = Column(Boolean)

    question = relationship("Question", back_populates="choices")
