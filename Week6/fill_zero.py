#!/usr/bin/python3
"""fill_zero.py, sample code that fills a decimal number as a binary representation with a number of zeros"""

__author__ = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

d = 6

print(format(d, "b").zfill(8))

print("Steve", str(d) + " has {} balloons {}.".format(5, "Hello"))
