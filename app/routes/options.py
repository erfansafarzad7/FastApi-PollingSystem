from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas import options
from app import models
from app.utils.utils import get_current_active_user

router = APIRouter(prefix="/options", tags=["options"])


# @router.patch("/{option_id}", response_model=options.Option)
# def update_options(
#         option_id: int,
#         option: options.OptionEdit,
#         db: Session = Depends(get_db),
#         current_user: models.User = Depends(get_current_active_user)
# ):
#     db_option = db.query(models.Option).filter(models.Option.id == option_id).first()
#     if not db_option:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Option not found"
#         )
#
#     db_poll = db.query(models.Poll).filter(models.Poll.id == db_option.poll_id).first()
#     if not db_poll:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Poll not found"
#         )
#
#     if db_poll.owner_id != current_user.id:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="You are not the owner of this poll"
#         )
#
#     db_option.text = option.text
#     db.commit()
#     db.refresh(db_option)
#     return db_option


@router.get("/{option_id}", response_model=options.Option)
def read_option(
        option_id: int,
        db: Session = Depends(get_db)
):
    option = db.query(models.Option).filter(models.Option.id == option_id).first()

    if option is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Option not found"
        )

    return option
