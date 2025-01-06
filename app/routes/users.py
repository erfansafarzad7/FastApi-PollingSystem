from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas import users
from app.security.security import get_password_hash
from app import models

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=users.User)
def create_user(
        user: users.UserCreate,
        db: Session = Depends(get_db)
):
    db_user = models.User(
        username=user.username,
        email=user.email
    )
    db_user.hashed_password = get_password_hash(user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get('/{user_id}', response_model=users.User)
def get_user(
        user_id: int,
        db: Session = Depends(get_db)
):
    user = db.query(models.User).filter(models.User.username == user_id).first()

    if not user:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user
