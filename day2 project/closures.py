"""Greeting Closures"""
def greeting(message):
    def greet(name):
        return f"{message}, {name}!"
    return greet


hello = greeting("Hello")

print(hello("Ammu"))

"""Multiplier Closures"""

def multiplier(x):
    def multiply(y):
        return x * y
    return multiply


double = multiplier(2)

print(double(10))

"""Counting closure"""

def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


c = counter()

print(c())
print(c())
print(c())