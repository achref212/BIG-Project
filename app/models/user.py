from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False, default="child")

    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relations
    profile = relationship("Profile", back_populates="user", uselist=False)
    progress = relationship("UserProgress", back_populates="user", uselist=False)
    quiz_attempts = relationship("UserQuizAttempt", back_populates="user")
    story_attempts = relationship("UserStoryAttempt", back_populates="user")
    mock_exam_attempts = relationship("MockExamAttempt", back_populates="user")
    badges = relationship("UserBadge", back_populates="user")
    subscriptions = relationship("Subscription", back_populates="user")
