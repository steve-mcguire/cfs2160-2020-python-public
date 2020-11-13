#!/usr/bin/python3
"""student_marks_loop.py, example of better programme"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"


def has_passed(student_mark, pass_mark):
    if student_mark not in range(0, 101):
        raise ValueError("Mark not in range")

    return student_mark >= pass_mark

try:
    print(has_passed(150, 40))
except ValueError as error:
    print(error)

grades = []
name = input("Enter student name")
for x in range(2):
    # get input and check it is in range
    grade = int(input("Please enter grade " + str(x) + ": "))
    if grade in range(0, 101):
        grades.append(grade)
    else:
        # if out of range
        print("Grade not between 1 and 100%")

avg_mark = sum(grades) / len(grades)

if has_passed(avg_mark, 40):
    print("Well done " + name + " your mark of " + str(avg_mark)
          + " is greater than 40 so you have passed")
else:
    print(name + " your mark of " + str(avg_mark)
          + " is less than 50 so you have not passed")

