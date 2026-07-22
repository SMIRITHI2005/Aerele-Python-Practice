from .models import Student
from .services import register_student

def add_student(name, age, department):
    student = Student(name, age, department)
    register_student(student)