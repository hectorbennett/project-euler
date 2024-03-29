"""
COMPLETE

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper
divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is
a perfect number.

A number n is called deficient if the sum of its proper divisors is less
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
smallest number that can be written as the sum of two abundant numbers
is 24. By mathematical analysis, it can be shown that all integers
greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even
though it is known that the greatest number that cannot be expressed as
the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the
sum of two abundant numbers.
"""

MAXIMUM = 28124
ABUNDANTS = []
LIST_OF_ABUNDANT_SUMS = [False] * MAXIMUM


def is_abundant(number):
    return(sum(i for i in range(1, number) if number % i == 0) > number)


for i in range(1, MAXIMUM):
    if is_abundant(i):
        ABUNDANTS.append(i)
        print(i)

for i in range(len(ABUNDANTS)):
    for j in range(i, len(ABUNDANTS)):
        Sum = ABUNDANTS[i] + ABUNDANTS[j]
        if Sum >= MAXIMUM:
            break
        else:
            LIST_OF_ABUNDANT_SUMS[Sum] = True

print(sum([i for i in range(len(LIST_OF_ABUNDANT_SUMS)) if LIST_OF_ABUNDANT_SUMS[i] == False]))
