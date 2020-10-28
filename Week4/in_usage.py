#!/usr/bin/python3
"""in_usage.py, simple demo of in keyword with usage"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

tutors = ["Ilias", "Steve", "Kevin", "Rubiya"]

while True:
    tutor_name = input("Please enter a tutor name").capitalize()

    if tutor_name in tutors:
        print(tutor_name, "is a member of staff in CFS2160")
        break
    else:
        print(tutor_name, "is not a member of staff in CFS2160")

print("Programme terminated")