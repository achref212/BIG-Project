from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    content = Column(Text)
    audio_url = Column(String(255))

    level_id = Column(Integer, ForeignKey("levels.id"))

    level = relationship("Level", back_populates="stories")
