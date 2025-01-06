from pydantic import BaseModel


class OptionBase(BaseModel):
    text: str


class OptionCreate(OptionBase):
    pass


class OptionEdit(OptionBase):
    pass


class Option(OptionBase):
    id: int
    vote_count: int

    class Config:
        from_attributes = True
