from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

    first_name = Column(String(100))
    last_name = Column(String(100))
    birth_date = Column(Date)
    avatar_url = Column(String(255))

    current_level_id = Column(Integer, ForeignKey("levels.id"))

    user = relationship("User", back_populates="profile")
    current_level = relationship("Level")
