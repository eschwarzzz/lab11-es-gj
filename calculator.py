"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def add(a, b):
        return a + b

def sub(a, b):
        return a - b

def mul(a, b):
        return a * b

def div(a, b):
        try:
                return b / a
        except:
                raise ZeroDivisionError("Cannot divide by zero")

def log(a, b):
        try:
                return math.log(b, a)
        except:
                raise ValueError("Cannot have a value less than or equal to 0")

def exp(a, b):
        return a ** b


def square_root(a):
    if a < 0:
        raise ValueError("Cannot have a value less than 0")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)