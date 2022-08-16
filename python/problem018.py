"""
COMPLETE

By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
"""

TRIANGLE = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


def convert_triangle_to_list(triangle):
    """
    Converts a big triangle string of numbers into a usable list of
    lists of integers
    """
    triangle = triangle.splitlines()

    return [[int(value) for value in row.split()] for row in triangle]


TRIANGLE_LIST = convert_triangle_to_list(TRIANGLE)


def find_maximum_path(lis):
    """
    working backwards from the penultimate line, to each number we add
    the largest of the two adjacent numbers in the line below
    """
    for i in range(len(lis) - 2, -1, -1):
        for j in range(len(lis[i])):
            lis[i][j] += max(lis[i + 1][j], lis[i + 1][j + 1])

    return lis[0][0]


print(find_maximum_path(TRIANGLE_LIST))
