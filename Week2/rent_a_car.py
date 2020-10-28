#!/usr/bin/python3
"""rent_a_car.py, demo of input with checks and output"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

age = int(input("Please enter your age? "))

has_driving_license = input("Do you have a valid driving license? (YES / NO)")

if age >= 21 and has_driving_license == "YES":
    print("You can rent a car from us")
else:
    print("You cannot rent a car from us")