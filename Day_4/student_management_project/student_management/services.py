from .validators import validate_student
from .repository import save

def register_student(student):
    validate_student(student)
    save(student)