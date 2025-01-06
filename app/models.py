from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    polls = relationship('Poll', back_populates="owner")
    votes = relationship('Vote', back_populates="voter")


class Poll(Base):
    __tablename__ = "polls"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship('User', back_populates='polls')
    options = relationship('Option', back_populates='poll')
    votes = relationship('Vote', back_populates='poll')


class Option(Base):
    __tablename__ = "options"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    poll_id = Column(Integer, ForeignKey('polls.id'))
    vote_count = Column(Integer, default=0)

    poll = relationship('Poll', back_populates='options')
    votes = relationship('Vote', back_populates='option')


class Vote(Base):
    __tablename__ = "votes"
    id = Column(Integer, primary_key=True, index=True)
    poll_id = Column(Integer, ForeignKey("polls.id"))
    option_id = Column(Integer, ForeignKey("options.id"))
    voter_id = Column(Integer, ForeignKey("users.id"))

    poll = relationship('Poll', back_populates='votes')
    option = relationship('Option', back_populates='votes')
    voter = relationship('User', back_populates='votes')





