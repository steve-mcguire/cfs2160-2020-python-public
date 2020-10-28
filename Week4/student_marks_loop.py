#!/usr/bin/python3
"""student_marks_loop.py, example of better programme"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"
grades = []
while True:
    try:# this is a try block which deals with an exception,
        # it is used to purposely deal with incorrect input from the user

        # get input and check it is in range
        grade = int(input("Enter a grade"))
        if grade in range(0, 101):
            grades.append(grade)
        else:
            # if out of range
            print("Grade not between 1 and 100%")
    # what happens if the use enters a wrong input
    except ValueError:
        print("You did not enter a valid input, programme terminated")
        break

# printing of report ommited
print(grades)
