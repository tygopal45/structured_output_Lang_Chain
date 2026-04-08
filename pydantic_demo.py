from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name : str = "Adiiii"
    age : Optional[int] = None
    # buildin validation
    email : EmailStr
    cgpa : float = Field(gt=0, lt=10, default=5.0, description="CGPA must be between 0 and 10")


# email validation
# new_student = {'name': 'John Doe', 'age': 32, 'email': 'john.doe'}
#  value is not a valid email address: An email address must have an @-sign. [type=value_error, input_value='john.doe', input_type=str]

new_student = {'name': 'John Doe', 'age': 32, 'email': 'john.doe@example.com', 'cgpa': 8.5}



# implicit type conversion -> coerce the value to the expected type
# new_student = {'age': '32'}
# pydantic detects '32' string and converts it to an integer 32 for the age field


# new_student = {'age': 32}
# name='Adiiii' age=32


# new_student = {"name": 32}
# throws an error because the value of name is not a string

# setting default values
# new_student = {}

student = Student(**new_student)


print(type(student))
print(student)


# converting to dictionary
student_dict = dict(student)

print(student_dict['age'])
print(student_dict['cgpa'])
print(student_dict['name'])

# converting to json
student_json = student.model_dump_json()
print(student_json)