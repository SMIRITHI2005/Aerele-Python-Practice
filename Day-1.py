
squares = [i*i for i in range(10)]
# List comprehension
numbers = [n * n for n in range(1, 6)]
print(numbers)

# Context manager
with open("demo.txt", "w") as file:
    file.write("Hello from Python!")

# Tuple unpacking
person = ("Ammu", 21)
name, age = person
print(name, age)

# enumerate
languages = ["Python", "Java", "C++"]
for index, language in enumerate(languages, start=1):
    print(index, language)

# zip
students = ["Asha", "Rahul", "Kiran"]
scores = [92, 85, 88]
for student, score in zip(students, scores):
    print(f"{student} scored {score}")

def add_item(item, cart=None):

    if cart is None:
        cart = []

    cart.append(item)

    return cart
print(add_item("Apple"))