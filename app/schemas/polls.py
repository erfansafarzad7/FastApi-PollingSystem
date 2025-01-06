from pydantic import BaseModel
from typing import List
from pydantic import BaseModel, Field, field_validator
from .options import Option, OptionCreate
from .votes import Vote


class PollBase(BaseModel):
    question: str


class PollCreate(PollBase):
    options: List[OptionCreate] = Field(..., min_items=2)

    @field_validator('options')
    def validate_options(cls, v):
        if len(v) < 2:
            raise ValueError("At least two options are required")
        return v


class Poll(PollBase):
    id: int
    owner_id: int
    options: List[Option] = []

    class Config:
        from_attributes = True
