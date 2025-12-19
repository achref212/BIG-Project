from fastapi import APIRouter, Depends
from app.core.dependencies import admin_required
from app.models.user import User

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/health")
def health(_: User = Depends(admin_required)):
    return {"status": "OK"}
