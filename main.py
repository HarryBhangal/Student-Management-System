from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models.student import Student_table
from database.db import engine, Base

app = FastAPI()

@app.get("/")
def welcome():
    return{"Student Managment System is running"}

@app.get("/about")
def about():
    return{
        "Project":"Student managment System ",
        "Version": "1.0"
    }

Base.metadata.create_all(bind=engine)

