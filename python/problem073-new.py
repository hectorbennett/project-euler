"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
"""
	
"""
first we need to find the LCM of all numbers ≤ 12,000 as we are
going to multiply all our fractions by this number to attain a list of
integers
"""

def HCF(a, b):
	if b == 0:
		return(a)
	else:
		return(HCF(b, a % b))

def LCM(a,b):
	return(abs(a * b) // HCF(a,b))

#returns LCM of a list
def LCMlist(lis):
	h = LCM(lis[0],lis[1])
	for i in lis[2:]:
		h = LCM(h, i)
	return(h)

#returns LCM of all numbers ≤ i
def megaVal(i):
	return LCMlist(list(range(1,i+1)))

#lists the amount of reduced proper fractions between 1/3 and 1/2 for d ≤ i
def fracList(i):
	megaList = []
	for d in range(i,1,-1):
		for n in range(1,d):
			if HCF(n,d) == 1:
				megaList.append(n / d)

	return(megaList)
	
	
print(fracList(1200))
