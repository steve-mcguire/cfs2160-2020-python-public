#!/usr/bin/python3
"""weather_station.py, basic implementation of loops with input and outputs"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

readings = []


number_of_readings = int(input("enter number of readings"))

for r in range(number_of_readings):
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


print("Min is (C) ", min(readings), "/ (F) ", min(readings) * 1.8 + 32)
print("Max is (C)", max(readings), "/ (F)", min(readings) * 1.8 + 32)
print("AVG is (C) ", sum(readings) / len(readings), "/ (F) "
      , (sum(readings) / len(readings)) * 1.8 + 32)
