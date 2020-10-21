readings = []

number_of_readings = int(input("enter numebr of readings"))

for r in range(number_of_readings):
    readings.append(float(input("Please enter temp " + str(r + 1) + ": ")))


print("Min is " + str(min(readings)))
print("Max is ", max(readings))
print("AVG is", round(sum(readings) / len(readings), 2))


