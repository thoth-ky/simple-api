from sqlalchemy import Boolean, Column, Integer, String
from database.database import Base

class ToDo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    done = Column(Boolean, default=False)
