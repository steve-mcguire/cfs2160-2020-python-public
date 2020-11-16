#!/usr/bin/python3
"""weather_station_better.py, basic implementation of loops with input and outputs"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

readings = []

number_of_readings = int(input("enter number of readings"))

for r in range(number_of_readings):
    readings.append(float(input("Please enter temp " + str(r + 1) + ": ")))


print("Min is " + str(min(readings)))
print("Max is ", max(readings))
print("AVG is", round(sum(readings) / len(readings), 2))