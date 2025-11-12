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
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        return b / a 

def log(a, b): 
    if a <= 0 or a == 1:
        raise ValueError("Cannot have a value less than or equal to 1")
    if b <= 0:
        raise ValueError("Cannot have a value less than or equal to 0")
    return math.log(a, b)

def exp(a, b):
    return a ** b
