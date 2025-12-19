from sqlalchemy import Column, Integer, String
from app.database import Base


class MultiplayerRoom(Base):
    __tablename__ = "multiplayer_rooms"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String(10), unique=True)
    status = Column(String(20))  # waiting / in_progress / finished
