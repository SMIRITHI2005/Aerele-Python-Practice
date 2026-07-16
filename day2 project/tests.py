"""
Simple test cases for the project.
"""

from student import (
    is_pass,
    calculate_grade,
    find_topper,
    average_marks
)

from utils import (
    capitalize_name,
    calculate_percentage
)


def run_tests():

    # is_pass()
    assert is_pass(50) is True
    assert is_pass(20) is False

    # calculate_grade()
    assert calculate_grade(95) == "A"
    assert calculate_grade(80) == "B"
    assert calculate_grade(65) == "C"
    assert calculate_grade(45) == "D"
    assert calculate_grade(20) == "F"

    # average_marks()
    assert average_marks([80, 90, 100]) == 90

    # find_topper()
    students = {
        "Ammu": 95,
        "Rahul": 80,
        "Priya": 90
    }

    assert find_topper(students) == "Ammu"

    # capitalize_name()
    assert capitalize_name("ammu") == "Ammu"

    # calculate_percentage()
    assert calculate_percentage(450, 500) == 90.0

    print("✅ All tests passed successfully!")


if __name__ == "__main__":
    run_tests()