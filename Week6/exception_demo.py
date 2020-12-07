#!/usr/bin/python3
"""exception_demo.py, dealign with an exception that is raised when converting a string with non numeric
characters to an int"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

try:
    reading = int(input("Please enter a number: "))
    print(reading)
except ValueError:
    print("Error with input")
