from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.params import Body

# using the JSON Compatible Encoder from FastAPI 
# to convert our models into a format that's JSON compatible.

from app.server.database import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
)
from app.server.models.student import (
    ErrorResponseModel,
    ResponseModel,
    StudentSchema,
    UpdateStudentModel,
)

router = APIRouter()

@router.post("/", response_description="Student data added into the database")
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, "Student added successfully.")

# So, the route expects a payload that matches the format of StudentSchema. Example:
# {
#     "fullname": "John Doe",
#     "email": "jdoe@x.edu.ng",
#     "course_of_study": "Water resources engineering",
#     "year": 2,
#     "gpa": "3.0",
# }