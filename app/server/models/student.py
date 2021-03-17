from typing import Optimal, Optional
from pydantic import BaseModel, EmailStr, Field


#In the code above, we defined a Pydantic Schema called StudentSchema 
#that represents how the student data will be stored in your MongoDB database.

# In Pydantic, the ellipsis, ..., indicates that a Field is required.
# It could be replaced with None or a default value. 
# In StudentSchema, each field has an ellipsis, since each field is important and the program shouldn't proceed without having the values set.

#FastAPI uses Pyantic Schemas to automatically document data models in conjunction with Json Schema.
#Swagger UI then renders the data from the generated data models. 
# You can read more about how FastAPI generates API documentation
# https://fastapi.tiangolo.com/features/#automatic-docs

#Since we used EmailStr, we need to install email-validator.
# Be sure, email-validator is installed or present in you requirements file.


class StudentSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., le=4.0)

    class Config:
        schema_extra = {
            "example":{
                "fullname" : "John Doe",
                "email" : "jdoe@mail.mail",
                "course_of_study" : "Bioinformatics",
                "year" : 2,
                "gpa" : "3.0",
            }
        }

class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {
            "example":{
                "fullname" : "John Doe",
                "email" : "jdoe@mail.mail",
                "course_of_study" : "Bioinformatics",
                "year" : 2,
                "gpa" : "3.0",
            }
        }

def ResponseModel(data, message):
    return{
        "data":[data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}