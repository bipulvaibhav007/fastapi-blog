from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class PostOut(BaseModel):
    id: int
    title: str
    content: str

    model_config = {
        "from_attributes": True
    }
