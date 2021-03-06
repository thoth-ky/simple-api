from sqlalchemy.orm import  Session
from  . import  schema, models


def get_todos(db: Session, skip: int =0, limit: int=200 ):
    return db.query(models.ToDo).offset(skip).limit(limit).all()

def get_todo(db: Session, todo_id: int):
    todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    return todo

def create_todos(db:Session, todo: schema.TodoCreate):
    todo_item = models.ToDo(**todo.dict())
    db.add(todo_item)
    db.commit()
    db.refresh(todo_item)
    return todo_item

def update_todo_done(db: Session, todo_id: int):
    todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).update({'done': True})
    db.commit()
    return get_todo(db, todo_id)
