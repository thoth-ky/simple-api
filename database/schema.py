from pydantic import BaseModel

class TodoBase(BaseModel):
    name: str
    done: bool = False


class Todo(TodoBase):
    id: int

    class Config:
        orm_mode = True

class TodoCreate(TodoBase):
    pass