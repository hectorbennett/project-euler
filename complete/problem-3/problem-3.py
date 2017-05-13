"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

x = 600851475143

def primeSieve(n):
	primeList = []
	
	isPrime = [True]*n
	isPrime[0] = isPrime[1] = False
	
	for i in range(n):
		if isPrime[i] == True:
			primeList.append(i)
			for k in range(2*i,n,i):
				isPrime[k] = False
			
	return(primeList)

for i in reversed(primeSieve(int(x ** 0.5))):
	if x % i == 0:
		print(i)
		break
