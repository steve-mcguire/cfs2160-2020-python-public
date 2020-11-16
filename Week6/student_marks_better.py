#!/usr/bin/python3
"""student_marks_better.py, a better implementation of the student marks system"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"
marks = []
number_of_marks = 6


def has_passed(student_mark, pass_mark):
    return student_mark >= pass_mark


for count in range(number_of_marks):

    while True:
        mark = int(input("Enter mark " + str(count + 1) + ": "))

        if mark in range(0, 101):
            marks.append(mark)
            # print("Mark accepted")
            break
        else:
            print("Mark out of range")


avg = round(sum(marks) / len(marks), 1)

print("Average mark is " + str(avg))
if has_passed(avg, 40):
    print("You have passed")
else:
    print("You have not reached the pass mark")



