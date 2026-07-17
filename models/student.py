from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String
from database.db import Base


class Student(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., ge=0, le=120)
    course: str



class Student_table(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(50), nullable = False)
    course = Column(String(60), nullable = False)
    age = Column(Integer, nullable = False)