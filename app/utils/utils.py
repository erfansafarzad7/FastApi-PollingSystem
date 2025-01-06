from fastapi import Depends, HTTPException, status
from app.security.security import get_current_user
from app import models


def get_current_active_user(current_user: models.User = Depends(get_current_user)):
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    return current_user
