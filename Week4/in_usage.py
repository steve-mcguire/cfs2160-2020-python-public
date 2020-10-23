# details how to use the in keyword

tutors = ["Ilias", "Steve", "Kevin", "Rubiya"]

while True:
    tutor_name = input("Please enter a tutor name").capitalize()

    if tutor_name in tutors:
        print(tutor_name, "is a member of staff in CFS2160")
        break
    else:
        print(tutor_name, "is not a member of staff in CFS2160")

print("Programme terminated")