from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    summary = Column(String(500))

    level_id = Column(Integer, ForeignKey("levels.id"))
    cover_image_url = Column(String)
    text_html = Column(Text)
    audio_url = Column(String)
    estimated_duration = Column(Integer)

    level = relationship("Level", back_populates="stories")
