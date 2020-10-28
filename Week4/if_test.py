#!/usr/bin/python3
"""if_test.py, simple if test and demo"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

i = int(input("Please enter a number greater than zero"))

if i >= 0:
    print(i, "is greater than zero")
else:
    print(i, "is less than zero!")
