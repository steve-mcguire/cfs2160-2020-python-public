#!/usr/bin/python3
"""loopy.py, some example of loops"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

message = "Hello. World"

for c in message:
    print('')

staff_member = ["Ilias", "Steve", "Rubiya", "Kevin"]
print(len(staff_member))
staff_member.append("Tony")
print(len(staff_member))

number_of_staff = 2

for s in range(number_of_staff):
    staff_member.append(input("Add staff member"))

for staff in staff_member:
    print(staff)

for i in range(0, 10):# 0,1,2,3,4,5,6,7,8,9
    print("")

i = 0
x = 10
while i < x:
    #print(i)
    i += 1
