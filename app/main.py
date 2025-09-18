from fastapi import FastAPI
from app.db.session import Base, engine
from app.api.v1 import user, post, auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Blog")

app.include_router(user.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(post.router, prefix="/api/v1/posts", tags=["Posts"])

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI Blog!"}
