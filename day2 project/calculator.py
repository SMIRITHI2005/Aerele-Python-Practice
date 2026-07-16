"""Function calling another function"""
def calculate(operation, x, y):
    return operation(x, y)
def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a:int ,b:int):
  return a*b
def divide(a:int ,b:int ):
  return a/b
print(calculate(multiply,3,7))


"""One Function = One Job"""
print(add(3,6))
print(subtract(6,4))
print(multiply(4,9))
print(divide(6,3))

"""Closures"""
def multiplier(x):

    def multiply(y):
        return x * y

    return multiply
d=multiplier(3)
print(d(4))

