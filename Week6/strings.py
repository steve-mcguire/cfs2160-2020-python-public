#!/usr/bin/python3
"""strings.py, "some examples of string slice and usage"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

message = "Hello. World"

reading = "35p"

print(message)
print(message[0])

print(message[0:5])
print(message[:-3])

print(reading[:-1])

print(type(reading[:-1]))