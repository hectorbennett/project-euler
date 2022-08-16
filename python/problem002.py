"""
COMPLETE

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will
be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
"""

FIB = [1, 2]
TOTAL = 0

while FIB[-1] < 4000000:
    FIB.append(FIB[-1] + FIB[-2])

for i in FIB:
    if i % 2 == 0:
        TOTAL += i

print(TOTAL)