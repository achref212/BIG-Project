from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.multiplayer import MultiplayerRoom
from app.schemas.multiplayer import MultiplayerRoomCreate, MultiplayerRoomOut
from app.core.dependencies import get_db, get_current_user

router = APIRouter(
    prefix="/multiplayer",
    tags=["Multiplayer"]
)


@router.post("/", response_model=MultiplayerRoomOut)
def create_room(
    data: MultiplayerRoomCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    room = MultiplayerRoom(
        **data.model_dump(),
        created_by=user.id
    )
    db.add(room)
    db.commit()
    db.refresh(room)
    return room


@router.put("/{id}", response_model=MultiplayerRoomOut)
def update_room(
    id: int,
    data: MultiplayerRoomCreate,
    db: Session = Depends(get_db)
):
    room = db.query(MultiplayerRoom).filter(MultiplayerRoom.id == id).first()
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    for key, value in data.model_dump().items():
        setattr(room, key, value)

    db.commit()
    db.refresh(room)
    return room
