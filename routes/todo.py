from fastapi import APIRouter, Depends
from sqlalchemy.orm import  Session
from fastapi import FastAPI, File, UploadFile, Form, status, Response
from typing import List


from database.database import SessionLocal, engine
from database.schema import  TodoCreate, Todo
from database.crud import get_todos, create_todos, update_todo_done

router = APIRouter(tags=["ToDO"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[Todo])
async def get_todos_list(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = get_todos(db, skip=skip, limit=limit)
    return todos

@router.post("/", response_model=Todo, status_code=status.HTTP_201_CREATED)
async def create_todo_record(todo: TodoCreate, db: Session = Depends(get_db)):
    return create_todos(db, todo)

@router.put("/{todo_id}/done", response_model=Todo)
async def mark_todo_done(todo_id: int,  db: Session = Depends(get_db)):
    return update_todo_done(db, todo_id)
