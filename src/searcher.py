#!/usr/bin/env python
from __future__ import division

from subprocess import call

def run_with(n):
    exit_code = call(["./solar.py", str(n)])
    return False if exit_code == 0 else True

current = 100

max_value = None
min_value = 0

# Establish our upper bound
while not max_value:
    if run_with(current):
        max_value = current
    else:
        current *= 10

while not (-10 < max_value - min_value < 10):
    print current
    current = (max_value + min_value) / 2
    if run_with(int(current)):
        max_value = current
    else:
        min_value = current

print max_value
