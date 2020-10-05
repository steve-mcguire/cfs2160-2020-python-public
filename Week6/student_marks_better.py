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


