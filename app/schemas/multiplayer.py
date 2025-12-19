from pydantic import BaseModel, ConfigDict
from datetime import datetime


class MultiplayerRoomBase(BaseModel):
    code: str
    status: str


class MultiplayerRoomCreate(MultiplayerRoomBase):
    pass


class MultiplayerRoomOut(MultiplayerRoomBase):
    id: int
    created_by: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
