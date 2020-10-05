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



