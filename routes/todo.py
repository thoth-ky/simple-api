from fastapi import APIRouter, Depends, Request,status, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List
from sqlalchemy.orm import  Session


from database.database import SessionLocal, engine
from database.schema import  TodoCreate, Todo
from database.crud import get_todos, create_todos, update_todo_done

router = APIRouter(tags=["ToDO"])

templates = Jinja2Templates(directory="templates")

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

@router.put("/{todo_id}/done/", response_model=Todo)
async def mark_todo_done(todo_id: int,  db: Session = Depends(get_db)):
    return update_todo_done(db, todo_id)

@router.get('/fe', response_class=HTMLResponse)
async def display_todos(request: Request, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = get_todos(db, skip=skip, limit=limit)
    return templates.TemplateResponse("todo.html", { "request": request, "todos": todos})
