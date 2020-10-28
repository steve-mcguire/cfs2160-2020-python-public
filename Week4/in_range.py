#!/usr/bin/python3
"""in_range.py, simple demo of range with usage"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

user_number = int(input("enter a number"))

# the user value is with zero and 100

if user_number in range(101):
    print("Number is in range of 0 to 100")
else:
    print("Number not in range")


for x in range(0, 6):
    print(x)