import math

# Arithmetic Operations
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        raise ValueError("Division By Zero not possible")
    return a/b
def floor_divide(a,b):
    if b==0:
        raise ValueError("Division By Zero not possible")
    return a//b
def modulus(a,b):
    if b==0:
        raise ValueError("Division By Zero not possible")
    return a%b
def power(a,b):
    return math.pow(a,b)
def factorial(value):
    if not isinstance(value, int):
        raise ValueError("Factorial only works with integers")

    if value < 0:
        raise ValueError("Factorial not defined for negative numbers")
    return math.factorial(value)

#Dictionaries to map operators to functions
un_ops={"sqrt": math.sqrt,"abs": abs,"sin": math.sin,"cos": math.cos,"tan": math.tan,"fact": factorial}
bin_ops={'+':add, '-': subtract, '*': multiply, '/': divide,'//': floor_divide, '%':modulus, '^': power, '**': power}