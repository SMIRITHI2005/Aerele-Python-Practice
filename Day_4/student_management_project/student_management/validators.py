from .exceptions import InvalidAgeError

def validate_student(student):
    if student.age < 17:
        raise InvalidAgeError("Student must be at least 17 years old.")