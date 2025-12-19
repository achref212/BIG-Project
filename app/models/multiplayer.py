from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class MultiplayerRoom(Base):
    __tablename__ = "multiplayer_rooms"

    id = Column(Integer, primary_key=True)
    code = Column(String(10), unique=True)
    status = Column(String(20))
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class MultiplayerRoomUser(Base):
    __tablename__ = "multiplayer_room_users"

    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey("multiplayer_rooms.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    score = Column(Integer, default=0)
    joined_at = Column(DateTime(timezone=True), server_default=func.now())
