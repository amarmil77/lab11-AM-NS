"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b/a

def log(a, b):
    if a <= 0 or a==1 or b<=0:
        raise ValueError
    else:
        return math.log(b,a)

def exp(a, b):
    return a ** b




def substract(a, b):
    a-b

def multiply(a, b):
    a*b



def logarithm(a, b):
    #log a(b)git
    math.log(b, a)

    if b<0:
        raise ValueError("Cannot raise to negative power")

def exponent(a, b):
    #a**b
    math.pow(a, b)




