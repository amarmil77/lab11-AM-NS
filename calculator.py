"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def add(a, b): 
    a+b

def substract(a, b):
    a-b

def multiply(a, b):
    a*b

def divide(a, b):
    b/a
    if a == 0:
        raise ZeroDivisionError ("Cannot divide by zero.")

def logarithm(a, b):
    #log a(b)
    math.log(b, a)

    if b<0:
        raise ValueError("Cannot raise to negative power")

def exponent(a, b):
    #a**b
    math.pow(a, b)



