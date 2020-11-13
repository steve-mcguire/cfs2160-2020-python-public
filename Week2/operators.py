#!/usr/bin/python3
"""operator.py, a demo of some common python operators and their usage"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

import math
seats_on_bus = 24
passengers = 25

# print(x * y)

print("you will need",  math.ceil(passengers / seats_on_bus), "busses")

print(seats_on_bus // passengers) # floor division, returns the whole number only

print(seats_on_bus % passengers) # 25 % 24 = 1



name = "Steve"

age = 42

print(name, age)
print(name + " " + str(age))

print(name * 3)

print("Some text", age)
