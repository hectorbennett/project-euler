"""
Taking three different letters from the 26 letters of the alphabet,
character strings of length three can be formed. Examples are 'abc',
'hat' and 'zyx'. When we study these three examples we see that for
'abc' two characters come lexicographically after its neighbour to the
left. For 'hat' there is exactly one character that comes
lexicographically after its neighbour to the left. For 'zyx' there are
zero characters that come lexicographically after its neighbour to the
left. In all there are 10400 strings of length 3 for which exactly one
character comes lexicographically after its neighbour to the left.

We now consider strings of n ≤ 26 different characters from the
alphabet. For every n, p(n) is the number of strings of length n for
which exactly one character comes lexicographically after its neighbour
to the left.

What is the maximum value of p(n)?
"""

ALPHA = []
for i in range(26):
    ALPHA.append(i)

LIS = [0, 0, 0]
A = 0
while LIS != [25, 25, 25]:
    A = (A + 1) % 26

    for i in range(len(LIS) - 1):
        if LIS[i + 1] == 25:
            LIS[i] += 1

    LIS[-1] = A

    print(LIS)
