"""Loggin Decorator"""
def logger(func):
    def wrapper():
        print("Starting function...")
        func()
        print("Function finished.")
    return wrapper

"""Meaning greet=logger(greet)"""
@logger
def greet():
    print("Hello")


greet()

"""Time Decorator"""
import time

"""Decorator along with closure"""
def timer(func):
    def wrapper():
        start = time.time()

        func()

        end = time.time()

        print(f"Time: {end-start:.4f} seconds")

    return wrapper


@timer
def work():
    for _ in range(1000000):
        pass


work()

"""Uppercase Decorator"""
def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper


@uppercase
def greet():
    return "hello ammu"


print(greet())

"""Repeat Decorator"""
def repeat(times):
    def decorator(func):
        def wrapper():
            for _ in range(times):
                func()
        return wrapper
    return decorator


@repeat(3)
def hello():
    print("Hello")


hello()