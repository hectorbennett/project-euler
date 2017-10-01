"""
By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click
and 'Save Link/Target As...'), a 15K text file containing a triangle
with one-hundred rows.
"""

DATA = open("problem067-data.txt", "r")
TRIANGLE = DATA.read()


def convert_triangle_to_list(triangle):
    """
    Converts a big triangle string of numbers into a usable list of
    lists of integers
    """
    triangle = triangle.splitlines()

    return [[int(value) for value in row.split()] for row in triangle]


TRIANGLE = convert_triangle_to_list(TRIANGLE)


def find_maximum_path(lis):
    """
    working backwards from the penultimate line, to each number we add
    the largest of the two adjacent numbers in the line below
    """
    for i in range(len(lis) - 2, -1, -1):
        for j in range(len(lis[i])):
            lis[i][j] += max(lis[i + 1][j], lis[i + 1][j + 1])

    return lis[0][0]


print(find_maximum_path(TRIANGLE))
