#!/usr/bin/python3
"""loopy.py, some example of loops"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

list_of_int = [1, 3, 2, 4, 5, 3, 2, 4, 5]

for i in list_of_int:
    print(i)

to_check = 10
while True:
    var_1 = int(input("Enter a number"))
    if var_1 == to_check:
        print("Number correct")
        break
    else:
        print("Try again")


#print(list_of_int)




message = "steve-hud.ac.uk"

s = message.split("-")
print(s[1])

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
