#!/usr/bin/python3
"""student_marks_better.py, a better implementation of the student marks system"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"
marks = []
number_of_marks = 20000
for count in range(number_of_marks):

    while True:
        mark = int(input("Enter mark "))

        if mark in range(0, 101):
            marks.append(mark)
            print("Mark accepted")
            break
        else:
            print("Mark out of range")

print(sum(marks))

print("Average mark is " + str(sum(marks) / len(marks)))


