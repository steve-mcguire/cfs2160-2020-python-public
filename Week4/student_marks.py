#!/usr/bin/python3
"""student_marks.py, example of bad programme"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"
name = input("What is your name? ")

mark_1 = int(input("Enter mark 1: "))
mark_2 = int(input("Enter mark 2: "))
mark_3 = int(input("Enter mark 3: "))
mark_4 = int(input("Enter mark 4: "))
mark_5 = int(input("Enter mark 5: "))

total_mark = mark_1 + mark_2 + mark_3 + mark_4 + mark_5

avg_mark = total_mark / 5

print("The average mark for " + name + " is " + str(avg_mark))

if avg_mark >= 50:
    print("Well done " + name + " your mark of " + str(avg_mark)
          + " is greater than 50 so you have passed")
else:
    print(name + " your mark of " + str(avg_mark)
          + " is less than 50 so you have not passed")
