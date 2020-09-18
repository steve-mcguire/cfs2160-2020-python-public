age = int(input("Please enter your age? "))

has_driving_license = input("Do you have a valid driving license? (YES / NO)")

if age >= 21 and has_driving_license == "YES":
    print("You can rent a car from us")
else:
    print("You cannot rent a car from us")