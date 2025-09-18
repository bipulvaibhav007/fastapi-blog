from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.post import PostCreate, PostOut   # ✅ direct import
from app.crud import post as post_crud
from app.db.session import get_db
from app.api.deps import get_current_user
from app.models import User

router = APIRouter()

@router.post("/", response_model=PostOut)
def create_post(
    post: PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return post_crud.create_post(db, post, user_id=current_user.id)

@router.get("/", response_model=list[PostOut])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return post_crud.get_posts(db, skip=skip, limit=limit)
