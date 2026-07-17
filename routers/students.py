from fastapi import HTTPException, APIRouter
from FASTAPI.SMS.models.student import Student
from FASTAPI.SMS.database import database
from typing import Optional

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.post("/", status_code=201)
def create_student(student_id: int, student: Student):
    if student_id not in database:
        database[student_id] = {
            "name": student.name,
            "age": student.age,
            "course": student.course
    }
        return {"Message": "Your Data is Stored Successfully."}
    raise HTTPException(
        status_code=409,
        detail="Student already exists."
    )

@router.get("/")
def get_students(
    course: Optional[str] = None,
    age: Optional[int] = None,
    name: Optional[str] = None
):
    filtered_students = {
        sid: student
        for sid, student in database.items()
        if (course is None or student["course"].lower() == course.lower())
        and (age is None or student["age"] == age)
        and (name is None or student["name"].lower() == name.lower())
    }

    return {"DataBase": filtered_students}

@router.get("/{student_id}")
def details(student_id: int):
    if student_id in database:
        return{
            "details": database[student_id]
        }
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
    
@router.put("/{student_id}")
def edit_details(student_id : int, student: Student):
    if student_id in database:
        database[student_id] = {
            "name": student.name,
            "age": student.age,
            "course": student.course
        }
        return {
            "message": "Details Update Successfully. "
        }
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
    

@router.delete("/{student_id}")
def delete_student(student_id : int):
    if student_id in database:
        del database[student_id]
        return{
            "message": f"{student_id} succesfully deleted"
        }
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
