#!/usr/bin/python3
"""tuple.py, tuple demo and usage"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

staff = ("Ilias", "Steve", "Rubiya", "Kevin")

print(len(staff))

print(staff[:-1])

new_staff = ("Tony",)

all_staff = new_staff + staff

print(all_staff)

print("Steve" in staff)



required_staff = input("Type staff name ").capitalize()

if required_staff in staff:
    print("Your staff member exists")
else:
    print("Your staff member does not exists")



