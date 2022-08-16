"""
COMPLETE

From Wolfram alpha:

The number of digits in the repeating portion of the
decimal expansion of a rational number can also be
found directly from the multiplicative order of its denominator.

The period of a recurring decimal fraction
1/d is equal to the multiplicative order of 10 mod d.
"""
from utils import multiplicative_order

max_d = 0
max = 0
for d in range(2, 1000):
    m = multiplicative_order(10, d)
    if m > max:
        max = m
        max_d = d

print(max_d)
