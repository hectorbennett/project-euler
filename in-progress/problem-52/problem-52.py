"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

def sameDigits(n,m):
	nList = list(str(n))
	nList = [int(x) for x in nList]
	nList.sort()
	mList = list(str(m))
	mList = [int(x) for x in mList]
	mList.sort()
	if nList == mList:
		return True
	else:
		return False
	
i = 1
j = 1
a=True

while a == True:
	if j > 6:
		print(i)
		a = False
	if sameDigits(i, i*j) == True:
		j += 1
	else:
		j = 1
		i +=1
