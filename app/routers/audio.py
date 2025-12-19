from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, get_current_user

router = APIRouter(
    prefix="/audio",
    tags=["Audio"]
)

@router.post("/upload")
def upload_audio(
    file: UploadFile = File(...),
    user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Upload d'un enregistrement audio (prononciation, oral, lecture)
    """
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "user_id": user.id
    }
