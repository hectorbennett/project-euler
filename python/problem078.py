"""
Let p(n) represent the number of different ways in which n coins can be 
separated into piles. For example, five coins can be separated into 
piles in exactly seven different ways, so p(5)=7.
OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
"""

"""
We shall use the pentagonal number theorem
"""

def pent(n):
	return((3 * (n ** 2) - n) // 2)

def genPent(n):
	if n == 0:
		return(1)
	else:
		n = n + 1
		m = int(n/2) * ((-1) ** (n)) # converts [0,1,2,3,4,...] to [0,1,-1,2,-2,3,-3,4,-3,..]
		return(pent(m))
	
n = 1

print(genPent(0))
print(genPent(1))
print(genPent(2))
print(genPent(3))


while True:
	if genPent(n) % 1000000 == 0:
		#print(n)
		break
	n += 1
