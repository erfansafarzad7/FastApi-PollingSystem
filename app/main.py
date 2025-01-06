from fastapi import FastAPI
from app.routes import auth, polls, users, options, votes

# Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(polls.router)
app.include_router(users.router)
app.include_router(options.router)
app.include_router(votes.router)
app.include_router(auth.router)
