from fastapi import Depends, HTTPException, status
from app.dependencies.auth import get_current_user

def admin_required(user = Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return user
