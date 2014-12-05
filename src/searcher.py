#!/usr/bin/env python
from subprocess import call

def run_with(n):
    exit_code = call(["./test_search.py", str(n)])
    return False if exit_code == 0 else True

current = 10

max_value = None
min_value = None

# Establish our upper bound
while not max_value:
    if run_with(current):
        max_value = current
        min_value = current / 10
    else:
        current *= 10

while min_value + 1 < max_value:
    current = (max_value + min_value) / 2
    print current
    if run_with(current):
        max_value = current
    else:
        min_value = current


print max_value
