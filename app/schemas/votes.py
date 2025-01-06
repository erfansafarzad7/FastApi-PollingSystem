from pydantic import BaseModel


class VoteBase(BaseModel):
    option_id: int


class VoteCreate(VoteBase):
    pass


class Vote(VoteBase):
    id: int
    poll_id: int
    voter_id: int

    class Config:
        from_attributes = True
