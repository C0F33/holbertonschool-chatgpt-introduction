#!/usr/bin/python3
import sys

"""
Calculate the factorial of a non-negative integer.

@param n (int): The integer for which the factorial will be calculated.
@return int: The factorial of the input integer 'n'.
@return str: Error message if 'n' is negative.
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)