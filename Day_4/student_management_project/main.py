from student_management.api import add_student
from student_management.repository import get_all

add_student("Ammu", 20, "CSBS")
add_student("Rahul", 21, "CSE")

print(get_all())