from pydantic import BaseModel, EmailStr, constr


class UserLogin(BaseModel):
    username: constr(min_length=5, max_length=30)
    password: constr(min_length=8)


class UserBase(BaseModel):
    username: constr(min_length=5, max_length=30)
    email: EmailStr


class UserCreate(UserBase):
    password: constr(min_length=8)


class User(UserBase):
    id: int

    class Config:
        from_attributes = True
