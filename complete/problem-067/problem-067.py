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

data = open("problem-067-data.txt", "r")
triangle = data.read()

def tri2List(tri):
	tri = tri.splitlines()
	
	lis = [] #empty list we're about to fill
	
	for i in tri:
		lis.append(i.split())
	
	for i in range(len(lis)):
		for x in range(len(lis[i])):
			lis[i][x] = int(lis[i][x])
				
	return(lis)

triangle = tri2List(triangle)

#working backwards from the penultimate line, to each number we add the 
#largest of the two adjacent numbers in the line below
def algSum(lis):
	for i in range(len(lis) - 2, -1, -1):
		for j in range(len(lis[i])):
			lis[i][j] += max(lis[i+1][j], lis[i+1][j+1])
			
	return(lis[0][0])

print(algSum(triangle))
