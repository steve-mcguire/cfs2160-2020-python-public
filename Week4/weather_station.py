#!/usr/bin/python3
"""weather_station.py, basic implementation of loops with input and outputs"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

readings = []

number_of_readings = int(input("enter number of readings"))

for r in range(number_of_readings):
    # readings.append(float(input("Please enter temp " + str(r + 1) + ": ")))
    # get input as string
    # slice temp and scale
    # normalise data to C or F
    # add to list
    reading = input("Please enter temp " + str(r + 1) + ": ")
    temp = float(reading[:-1])
    scale = reading[-1]
    if scale == 'f':
        # convert to c and add to list
        temp_c = (temp - 32) * 5/9
        readings.append(temp_c)
    elif scale == 'c':
        readings.append(temp)
    else:
        print("Error in input")



print("Min is " + str(min(readings)))
print("Max is ", max(readings))
print("AVG is" + str(round(sum(readings) / len(readings), 2)) + "b")
