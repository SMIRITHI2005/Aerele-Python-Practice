"""One function=One task"""
"""How to use functions,parameters and return values"""
"""How to use type hints and docstring"""
"""How to organize related functions into one module"""
def is_pass(mark: int) -> bool:
    """Return True if the student passed."""
    return mark >= 40


def calculate_grade(mark: int) -> str:
    """Return the grade based on the mark."""
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 40:
        return "D"
    return "F"


def find_topper(students: dict[str, int]) -> str:
    """Return the name of the student with the highest mark."""
    return max(students, key=students.get)


def average_marks(marks: list[int]) -> float:
    """Return the average of all marks."""
    return sum(marks) / len(marks)
students = {
    "Ammu": 95,
    "Rahul": 82,
    "Priya": 90
}

print(is_pass(35))
print(calculate_grade(91))
print(find_topper(students))
print(average_marks([95, 82, 90]))