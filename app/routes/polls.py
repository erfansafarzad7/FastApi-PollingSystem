from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.dependencies import get_db
from app.schemas import polls
from app import models
from app.utils.utils import get_current_active_user

router = APIRouter(prefix="/polls", tags=["polls"])


@router.post("/create", response_model=polls.Poll)
def create_poll(
        poll: polls.PollCreate,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_active_user)
):
    try:
        if len(poll.options) < 2:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="At least two options are required"
            )

        db_poll = models.Poll(
            question=poll.question,
            owner_id=current_user.id
        )
        db.add(db_poll)
        db.commit()
        db.refresh(db_poll)

        for option in poll.options:
            db_option = models.Option(
                text=option.text,
                poll_id=db_poll.id
            )
            db.add(db_option)

        db.commit()
        db.refresh(db_poll)
        return db_poll

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{poll_id}", response_model=polls.Poll)
def read_poll(
        poll_id: int,
        db: Session = Depends(get_db)
):
    poll = db.query(models.Poll).filter(models.Poll.id == poll_id).first()

    if poll is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Poll not found"
        )

    return poll


@router.get("/", response_model=List[polls.Poll])
def get_all_polls(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    all_polls = db.query(models.Poll).offset(skip).limit(limit).all()
    return all_polls
