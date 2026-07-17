"""Classes and Objects"""


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ammu", 20)

print(s1.name)
print(s1.age)

"""__init__ & self & Instance Attributes"""

class Dog:

    def __init__(self, name):
        self.name = name

dog1 = Dog("Tommy")
dog2 = Dog("Rocky")

"""Class Attributes"""

class Student:

    school = "KPRIET"

    def __init__(self, name):
        self.name = name

s1 = Student("Alice")
s2 = Student("Bob")

print(s1.school)
print(s2.school)

"""Inheritance"""

class Animal:

    def sound(self):
        print("Animal sound")

class Dog(Animal):

    def bark(self):
        print("Woof")

"""Composition"""


class Engine:

    def start(self):
        print("Engine started")

class Car:

    def __init__(self):
        self.engine = Engine()

car = Car()
car.engine.start()

"""Order of Method Execution"""

class A:
    def show(self):
        print("A")

class B(A):
    pass

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()



