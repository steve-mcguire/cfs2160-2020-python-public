#!/usr/bin/python3
"""calc_function.py, sample function to multiply 2 numbers"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"


def multiply(v1, v2):
    return v1 * v2


def addition(v1, v2):
    return v1 + v2


value_1 = float(input("Enter number 1"))
value_2 = float(input("Enter number 1"))

result = multiply(value_1, value_2)
print(result)


