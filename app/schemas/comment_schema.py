from pydantic import BaseModel


class CommentCreate(BaseModel):
    task_id: int
    user_id: int
    comment_text: str


class CommentResponse(BaseModel):
    id: int
    comment_text: str

    class Config:
        from_attributes = True
