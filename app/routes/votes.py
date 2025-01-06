from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.utils.utils import get_current_active_user
from app.schemas import votes
from app import models

router = APIRouter(prefix="/votes", tags=["votes"])


@router.post("/create", response_model=votes.Vote)
def create_vote(
        vote: votes.VoteCreate,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_active_user)
):
    db_option = db.query(models.Option).filter(models.Option.id == vote.option_id).first()
    if not db_option:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Option not found"
        )

    db_vote = models.Vote(vote.option_id)
    db_vote.poll_id = db_option.poll_id
    db_vote.voter_id = current_user.id
    db_vote.option.vote_count += 1

    db.add(db_vote)
    db.commit()
    db.refresh(db_vote)
    return db_vote


@router.get("/{vote_id}", response_model=votes.Vote)
def read_vote(
        vote_id: int,
        db: Session = Depends(get_db)
):
    vote = db.query(models.Vote).filter(models.Vote.id == vote_id).first()

    if vote is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Vote not found"
        )

    return vote
