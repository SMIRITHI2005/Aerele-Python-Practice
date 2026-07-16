"""
Main entry point of the project.

This file imports functions from different modules
and demonstrates how they work together.
"""

from student import (
    is_pass,
    calculate_grade,
    find_topper,
    average_marks,
)

from utils import (
    capitalize_name,
    calculate_percentage,
    print_heading
)


def main():
    print_heading("Student Management System")

    students = {
        "ammu": 95,
        "rahul": 82,
        "priya": 90
    }

    print("Student Names")
    for name in students:
        print(capitalize_name(name))

    print()

    print("Topper:", find_topper(students))

    average = average_marks(list(students.values()))
    print("Average Marks:", average)

    mark = 95

    print("Passed:", is_pass(mark))
    print("Grade:", calculate_grade(mark))

    percentage = calculate_percentage(450, 500)
    print(f"Percentage: {percentage:.2f}%")

    print_heading("Program Finished")


if __name__ == "__main__":
    main()