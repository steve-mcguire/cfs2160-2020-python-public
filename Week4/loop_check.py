#!/usr/bin/python3
""".loop_check.py, checks to see if inputted data is equal to required value"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

# loop n times until a condition is met
password = "password"

while True:
    user_input = input("Please enter your password").lower()
    if user_input == password:
        print("inputs match")
        break
    else:
        print("Inputs do not match, please try again")

print("Loop ended as condition found")
